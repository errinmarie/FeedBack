import requests

response = requests.get('https://api.exchangeratesapi.io/latest?base=USD')
data = response.json()

print(data)
