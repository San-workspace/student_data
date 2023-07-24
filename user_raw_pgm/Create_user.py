import json

import requests
import jsonpath

# URL
url = "https://reqres.in/api/users"

# getting the file
file = open("C:\Personal\API_activity\create_user.json", 'r')
input_json = file.read()
# parsing the json
req_json = json.loads(input_json)

# post the request and get the response
response = requests.post(url, req_json)

# validate response code

res_code = response.status_code
assert res_code == 201

# validate header

res_header = response.headers
print(res_header.get("Content-Length"))

# response content validation
res_json = json.loads(response.text)
print(res_json)
res_name= jsonpath.jsonpath(res_json, 'name')
print(res_name[0])
