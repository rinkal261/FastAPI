import requests

age = 15
gender = "F"

response = requests.get(f"http://127.0.0.1:8000/predict?age={age}&gender={gender}")
output = response.json()
print(output)