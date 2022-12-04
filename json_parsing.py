import json

string_as_json = '{"answer": "User"}'
obj = json.loads(string_as_json)

key = "answer2"

if key in obj:
    print(obj[key])
else:
    print(f"Ключа {key} нет")

