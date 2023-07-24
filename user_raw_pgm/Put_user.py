import json

import requests
import jsonpath

# URL
url = "https://reqres.in/api/users/2"

# getting the file
file = open("C:\Personal\API_activity\create_user_update.json", 'r')
input_json = file.read()
# parsing the json
req_json = json.loads(input_json)

# PUT request and get the response
response = requests.put(url, req_json)

# validate response code

res_code = response.status_code
assert res_code == 200

# validate header

res_header = response.headers
print(res_header.get("Content-Type"))

# response content validation
res_json = json.loads(response.text)
name = jsonpath.jsonpath(res_json, 'name')
print(type(name))
assert name[0] == "morpheus_updated"
