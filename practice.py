import requests

api_key = 'd182ab73-0646-4e8b-a774-f8f88f31f8a4'
word = 'potato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definitions in definitions:
    print(definitions)