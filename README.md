# NLU-Quality-Check
Checks the quality of NLU performance by running NLU prediction API call for every test phrase from test_phrases.csv

This python script expects the following CSV file as input:
|test_phrase|expected_intent|
|---|---|
|hello|Hello|
|Good morning|Hello|
|human|Speak To a Human|

and produces the following CSV as output
|test_phrase|	detected_status|	expected_intent|	primary_intent|	all_intents|
|---|---|---|---|---|
|hello|	OK Primary|	Hello|	1434-Hello|	1434-Hello-0.9656 
|Good morning|	OK Primary|	Hello|	1434-Hello|	1434-Hello-0.7265 28621-Compliment-0.6147 
|can i listen to the calls of  target device|	Failed|	Features		
|can I try it before payment|	Failed|	trial|	1086-Payment Failed|	1086-Payment Failed-0.9257 
|Bro if you give me trail then i will pay|	Failed|	trial|	1086-Payment Failed|	1086-Payment Failed-0.6854 
|Error|	Unknown|	|	1086-Payment Failed|	1086-Payment Failed-0.7709 
|how to make payment|	Unknown|	|	1086-Payment Failed|	1086-Payment Failed-0.929 
|Robot|	Unknown	| |		
|Not helpful|	Unknown|	|	28621-Compliment|	28621-Compliment-0.6997 1440-No-0.6457 
|How to start the app|	OK Secondary|	how it works|	31244-Installation issues|	31244-Installation issues-0.6466 29826-Main Menu-0.5825 31674-How it works-0.5546 
|All|	Unknown	

detected_status can be one of:
- OK Primary - intent is recognized with highest confidence level
- OK Seconday - intent is recognized with confidence level >0.5 but it is not the highest
- Failed - wrongly recognized
- Unknown - input file does not have expected intent for this test phrase
