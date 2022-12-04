from json.decoder import JSONDecodeError
import requests

response = requests.get("https://playground.learnqa.ru/api/get_text")
print(response.text)
try:
    parse_json = response.json()
    print(parse_json)
except JSONDecodeError:
    print("Noooo")
