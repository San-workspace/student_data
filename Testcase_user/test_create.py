import json

import pytest
import requests
import jsonpath
import time

url = "https://reqres.in/api/users"

@pytest.fixture(scope='module')
def start_execution():

    global response
    global req_json
    file = open("C:\Personal\API_activity\create_user.json", 'r')
    # getting the file
    input_json = file.read()
    # parsing the json
    req_json = json.loads(input_json)
    # post the request and get the response
    start = time.time()
    # print("start reqeust",start)
    response = requests.post(url, req_json)
    end = time.time()
    # print("get response",end)
    # print("start of execution")

    yield
    elapsed_time = response.elapsed
    print("elapsed time is:", elapsed_time)
    ttl_time=end-start
    print("ttl time",ttl_time)
    print("closure execution")



@pytest.mark.regression
def test_stscode(start_execution):
    res_code = response.status_code
    assert res_code == 201


def test_header(start_execution):  # validate header
    res_header = response.headers
    res_contlnth = res_header.get('Content-Length')
    assert res_contlnth == '84' or '83'


@pytest.mark.regression
def test_json(start_execution):
    # res_json = json.loads(response.text)
    res_json = response.json()
    # print(res_json['name'])
    res_name = jsonpath.jsonpath(res_json, 'name')
    print(res_name[0])
    assert res_name[0] == 'morpheus'
    print(res_json)



