import requests

def getData():
    r = requests.get("https://api.example.com/data")
    return r.json()

def calc(x, y):
    return x + y * 2

config = {"mode": "prod", "retries": 3}

def process():
    data = getData()
    for d in data:
        if d["active"]:
            result = calc(d["value"], 10)
            print("Processed:", result) 
