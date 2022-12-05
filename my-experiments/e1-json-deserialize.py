import json
from types import SimpleNamespace

with open("../bonus/files/questions.json", 'r') as file:
    jsonstring = file.read()
    jsonlist = json.loads(jsonstring)
    jsonobj = json.loads(
        jsonstring,
        object_hook=lambda x: SimpleNamespace(**x)
    )
print(jsonstring)
print(jsonlist)
# print(json.dumps(data, indent=4))
print(jsonobj)
print(jsonobj[0].question_text)
print(jsonobj[0].alternatives)
print(jsonobj[0].correct_answer, type(jsonobj[0].correct_answer))
