import json
import jsonpath
import requests


def test_create_stdn():
    url = "https://thetestingworldapi.com/api/studentsDetails"
    file = open("C:\\Personal\\API_activity\\stdn_api\\req_json.json", 'r')
    inp_json = file.read()
    req_json = json.loads(inp_json)
    print(req_json)
    response = requests.post(url, req_json)
    print("*****creating***")
    print(response.text)
    print("*****creating***")
    id = jsonpath.jsonpath(response.json(), 'id')
    print(id[0])

    tech_url = 'https://thetestingworldapi.com/api/technicalskills'
    file = open("C:\\Personal\\API_activity\\stdn_api\\tech_dtl.json", 'r')
    req_json = json.loads(file.read())
    req_json['id']=int(id[0])
    req_json['st_id']=id[0]

    response = requests.post(tech_url, req_json)
    print("*****tech_update***")
    print(response.text)
    print("*****tech_update***")

    addr_url = 'https://thetestingworldapi.com/api/addresses'
    file = open("C:\\Personal\\API_activity\\stdn_api\\addr_dtl.json", 'r')
    req_json = json.loads(file.read())
    req_json['stId'] = id[0]
    response = requests.post(addr_url, req_json)
    print("*****addr_update***")
    print(response.text)
    print("*****addr_update***")

    final_dtl_url='https://thetestingworldapi.com/api/FinalStudentDetails/'+str(id[0])
    response=requests.get(final_dtl_url)
    print("*****fina_get***")
    print(response.text)
    print("*****final_get***")