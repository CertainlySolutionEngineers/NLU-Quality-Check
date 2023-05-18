# NLU-Quality-Check
Checks the quality of NLU performance by running NLU prediction API call for every test phrase from test_phrases.csv

This python script expects the following CSV file as input:
|test_phrase|expected_intent|
|---|---|
|hello|Hello|
|Good morning|Hello|
|human|Speak To a Human|

