import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/"

get_response = requests.get(endpoint, json={"query": "Hello World!"}) #HTTP Request
print(get_response.text) # Print RAW Text Response
print(get_response.status_code)

print(get_response.json())