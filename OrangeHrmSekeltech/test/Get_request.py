import requests
import json

def get_request():
    uri="https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&sortOrder=ASC"
    response=requests.get(uri)
    print(response.status_code)
    assert response.status_code == "200"

    json_response = json.loads(response.text)
    print(json_response)
    assert json_response.get("id") == "1"
    assert json_response.get("userName")=="Admin"
    assert json_response.get("empNumber")=="7"
    assert json_response.get("employeeId")=="muser"
    assert json_response.get("firstName")=="manda"
    assert json_response.get("middleName")=="akhil"
    assert json_response.get("lastName")=="user"
    assert json_response.get("status") == "true"
    #"middleName": "akhil",
                #"lastName": "user",

get_request()
