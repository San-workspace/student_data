import json
import jsonpath
import requests

#
def test_create_stdn():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\Personal\\API_activity\\stdn_api\\req_json.json", 'r')
    inp_json = file.read()
    req_json = json.loads(inp_json)
    print(req_json)
    response = requests.post(url, req_json)
    res_json = response.json()
    print(res_json)
    assert req_json['first_name'] == res_json['first_name']


def test_update_std():
    url = "https://thetestingworldapi.com/api/studentsDetails/7697178"
    file = open("C:\\Personal\\API_activity\\stdn_api\\req_update.json", 'r')
    inp_json = file.read()
    req_json = json.loads(inp_json)
    # print(req_json)
    response = requests.put(url, req_json)
    res_json = response.json()
    print(res_json)
    assert res_json['status'] == 'tru'
    assert res_json['msg'] == 'update  data success'


def test_get_std():
    url = "https://thetestingworldapi.com/api/studentsDetails/7697178"
    response = requests.get(url)
    res_json = json.loads(response.text)
    print(res_json)
#     data = res_json['data']
# #     assert data['first_name'] == 'a'


def test_del_std():
    url = "https://thetestingworldapi.com/api/studentsDetails/7697178"
    response = requests.delete(url)
    res_json = json.loads(response.text)
    print(res_json)


