import json
import requests

response = requests.get("https://api-colombia.com/api/v1/Department")

departments = json.loads(response.content)

print(departments)