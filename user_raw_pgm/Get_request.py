import json
from itertools import count

import requests
import jsonpath

# URI
# url = url = "https://reqres.in/api/users"

# response
response = requests.get("https://reqres.in/api/users?page=2")

# Parsing json obj
# res = response.json()
# print(type(res))
# print(res)

# or

json_response = json.loads(response.text)
print(type(json_response))

# # header validation
# print(response.headers)
# print(response.headers.get("date"))
# print(response.cookies)
# print(response.elapsed)
# print(response.encoding)

# response as list
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages)
assert pages[0] == 2

data = jsonpath.jsonpath(json_response, 'data')
# print(data[0])
# print(data[0][0]['email'])

for i in range(0, 3):
    data = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].email')
    print(data)

    assert data == ['michael.lawson@reqres.in'] and ['lindsay.ferguson@reqres.in'] and ['tobias.funke@reqres.in']



#
