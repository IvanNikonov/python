import requests

data = requests.get("https://kudago.com/public-api/v1.4/locations")
if data.status_code == 200:
    print(data.json())