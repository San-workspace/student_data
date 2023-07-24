import json

import requests
import jsonpath

# URI
url = "https://reqres.in/api/users"


def test_getuser():
    # response
    response = requests.get("https://reqres.in/api/users?page=2")

    json_response = json.loads(response.text)
    print(type(json_response))

    # response as list
    pages = jsonpath.jsonpath(json_response, 'total_pages')
    print(pages)
    assert pages[0] == 2

    data = jsonpath.jsonpath(json_response, 'data')
    # print(data[0])

    for i in range(0, 3):
        data = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].email')
        print(data[0])
    assert data[0] == 'michael.lawson@reqres.in' or 'lindsay.ferguson@reqres.in' or 'tobias.funke@reqres.in'




#
