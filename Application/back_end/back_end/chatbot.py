import requests
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def get_access_token():
    base_url = "https://aip.baidubce.com/oauth/2.0/token"
    grant_type = "client_credentials"
    client_id = "OAAjlDI4Wn79biQD5s4XbjTe"
    client_secret = "qrrwGg36FZ9BBARaGDd1G2j0g4isnRct"
    url = base_url + '?' + "grant_type=" + grant_type + '&' + "client_id=" + client_id + '&' + "client_secret=" + client_secret

    response = requests.post(url).json()
    return (response["access_token"])


@csrf_exempt
def chat(request):
    base_url = "https://aip.baidubce.com/rpc/2.0/unit/bot/chat"
    url = base_url + "?access_token=" + get_access_token()
    req_body = str(request.body, encoding="utf-8")
    req_body = eval(req_body)
    body = {
        "log_id": "1234567890",
        "version": "2.0",
        "skill_id": "1097583",
        "session_id": "",
        "request": {
            "query": req_body["query"],
            "user_id": "1234567890"
        },
        "dialog_state": {
            "contexts": {
                "SYS_REMEMBERED_SKILLS": [
                    ""
                ]
            }
        }
    }
    response = requests.post(url, data=json.dumps(body)).json()
    print(response)
    print(response["result"]["response"]["action_list"][0]["say"])
    return JsonResponse({"result": response["result"]["response"]["action_list"][0]["say"]})
