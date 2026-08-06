import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=32.08&longitude=72.67&current=temperature_2m"

response = requests.get(url)

print("Status Code:", response.status_code)

if response.status_code == 200:
    data = response.json()

    temperature = data["current"]["temperature_2m"]

    print("Current Temperature:", temperature, "°C")

else:
    print("Request Failed!")