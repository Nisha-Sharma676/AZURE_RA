import requests

url = "http://localhost:7071/api/analyze"

data = {
    "text": "The product is amazing but delivery was slow"
}

res = requests.post(url, json=data)

print(res.json())