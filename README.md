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
|can i listen to the calls of  target device|	Failed|	features		
|can I try it before payment|	Failed|	trial|	1086-Payment Failed|	1086-Payment Failed-0.9257 
|Should I pay first then call you or what|	Failed|	trial|	1086-Payment| Failed|	1086-Payment Failed-0.7612 
|I'm worried my kid will see the app and try deleting it would that be a problem?|	Failed|	detect|
|If I buy for one year and Mspy is no working, can I reclaim my payment?|	Failed|	trial|	1086-Payment Failed|	1086-Payment Failed-0.6073 
|I am trying to use Wi-Fi connection.  I tried to download onto my laptop but I'm getting an error message that says the app cannot be opened because my computer can't tell if it's free of malware.|Failed|installation		
|the program is not working, what should be done, maybe you can help|	Failed|	not working		
|Bro i need trail if you give me then i pay you|	Failed|	trial|	1086-Payment| Failed	1086-Payment Failed-0.5388 
|Bro if you give me trail then i will pay|	Failed|	trial|	1086-Payment| Failed|	1086-Payment Failed-0.6854 
|Error|	Unknown|		1086-Payment Failed|	1086-Payment| Failed-0.7709 
|how to make payment|	Unknown|		1086-Payment Failed|	1086-Payment Failed-0.929 
|Robot|	Unknown			
|Not helpful|	Unknown|		28621-Compliment|	28621-Compliment-0.6997 1440-No-0.6457 
|How to start the app|	OK Secondary|	how it works|	31244-Installation issues|	31244-Installation issues-0.6466 29826-Main Menu-0.5825 31674-How it works-0.5546 
|All|	Unknown			

