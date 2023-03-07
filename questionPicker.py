import random
import json
import string


with open('QnA.json') as listOfquestions:
    data = listOfquestions.read()
questions = json.loads(data)

print(questions[1])