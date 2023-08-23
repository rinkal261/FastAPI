import requests,json
payload = json.dumps({
    "age" : 10,
    "gender" : "M"
})
response = requests.put("http://http://127.0.0.1:8000/predict" , data = payload)
print(response.json())