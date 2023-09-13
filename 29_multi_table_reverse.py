import requests

url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

if response.status_code == 200:
    test = response.json()

    print(test['setup'])
    print(test['punchline'])
else:
    print(f"Failed to download file. Status code: {response.status_code}")
