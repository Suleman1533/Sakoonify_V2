import requests

url = "https://api.github.com/repos/Suleman1533/Sakoonify_V2/contents/"
response = requests.get(url)

print(response.status_code)
print(response.json())