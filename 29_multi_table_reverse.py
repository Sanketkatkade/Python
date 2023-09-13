# import requests

# url = "https://official-joke-api.appspot.com/random_joke"

# response = requests.get(url)

# if response.status_code == 200:
#     test = response.json()

#     print(test['setup'])
#     print(test['punchline'])
# else:
#     print(f"Failed to download file. Status code: {response.status_code}")


import requests

url = "https://www.facebook.com"
response = requests.get(url)
print(response.text)

with open("index.html",'w') as f:
    f.write(url.text)