import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)
if response.status_code == 200:
    vitsi = response.json()["value"]
    print(f"{vitsi}")