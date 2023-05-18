import requests
import csv
import json
from datetime import datetime

#TestPhrases = [
#    {"test_phrase":"hello", "expected_intent":"Hello"},
#    {"test_phrase":"good morning", "expected_intent":"Hello"}
#]

TestPhrases = []
with open("test_phrases.csv", encoding='utf-8') as csvf: 
    reader = csv.DictReader(csvf, delimiter=';', skipinitialspace=True, strict=True)
    for row in reader: TestPhrases.append(row)
    #print(TestPhrases)

# mSpy Live bot NLUv2
nlu_model_id=9067

# mSpy Test bot NLUv3
nlu_model_id=10385
# mSpy JWT
jwt="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg0NDc4Mzc4LCJpYXQiOjE2ODQzOTE5NzgsImp0aSI6IjlhOTUxM2RiOTJiNTQ3M2ViNDZlNDQ4ZDhmMTY0ZjA0IiwidXNlcl9pZCI6NTI3OCwidXNlcm5hbWUiOiJ0ZXN0ZXIubXNweUBjZXJ0YWlubHkuaW8iLCJlbWFpbCI6InRlc3Rlci5tc3B5QGNlcnRhaW5seS5pbyJ9.bRjzJtaagtrSxYXrE2cImHuWkR4fXP7Tl-0T-XoJVis"

with open(f'NLU_Quality_Check_{datetime.now().strftime("%Y%m%d-%H%M%S")}.csv', mode='w', encoding='utf-8', newline='') as out_file:
    out_writer = csv.writer(out_file, delimiter=';')
    out_writer.writerow(['test_phrase', 'detected_status', 'expected_intent', 'primary_intent', 'all_intents'])
    with requests.Session() as rsession:
        for ph in TestPhrases:
            response = rsession.get(f'https://app.certainly.io/api/nlu/predict/{nlu_model_id}/?q={ph["test_phrase"]}', headers={'Content-Type': 'application/json', 'Authorization': f'JWT {jwt}'})
            #print(response.status_code)
            
            if response.status_code != 200:
                print(f"Error {response.status_code}, skipping test_phrase: {ph['test_phrase']}")
                continue

            data = response.json()
            #print(data)

            if len(data['intents']) > 0:
                intents=sorted(data['intents'], key=lambda k: k['confidence'], reverse=True)
                #print(ph)
                primary_intent = ""
                detected_intents = ""
                if ph['expected_intent']:
                    detected_status = "Failed"
                else:
                    detected_status = "Unknown"
                if intents[0]['confidence'] > 0.5: primary_intent = intents[0]['name']
                for i in intents:
                    if i['confidence'] > 0.5: 
                        detected_intents += f"{i['name']}-{i['confidence']} "
                        if ph['expected_intent'] and (ph['expected_intent'].lower() in i['name'].lower()): 
                            if i==intents[0]:
                                detected_status = "OK Primary"
                            else:
                                detected_status = "OK Secondary"
                print(f"{ph['test_phrase']}; {detected_status}; {ph['expected_intent']}; {primary_intent}; {detected_intents}")
                out_writer.writerow([ph['test_phrase'], detected_status, ph['expected_intent'], primary_intent, detected_intents])