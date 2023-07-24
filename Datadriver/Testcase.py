import json

import requests


from Datadriver import library


def test_std_updatedata():
    # apiurl
    url = "https://thetestingworldapi.com/api/studentsDetails"

    # req_json
    file = open("C:\\Personal\\API_activity\\stdn_api\\req_json.json", 'r')
    inp_json = file.read()
    req_json = json.loads(inp_json)

    # xldata
    filepath = "C:/Users/fsn3kor/PycharmProjects/pythonProject1/Student_database/student_data.xlsx"
    sheetname = "Sheet1"
    obj = library.base(filepath, sheetname)

    col_count = obj.fetch_col_count()
    row_count = obj.fetch_row_count()
    key_names = obj.fetch_keynames()
    print(key_names)

    for i in range(2, row_count + 1):
        updated_json_req = obj.update_reqjson_with_data(i, req_json,
                                                        key_names)  # so far we preparing input json request as dynamically
        response = requests.post(url, updated_json_req)
        res_json = json.loads(response.text)
        print(res_json)
