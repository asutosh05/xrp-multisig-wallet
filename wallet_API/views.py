from django.shortcuts import render
import json
import requests
# Create your views here.

def generateWallateAddress(request):
    server='http://127.0.0.1:5005'
    reqjson={
        "method": "wallet_propose",
        "params": []
    }
    response =requests.post(server,json=reqjson)
    result=json.loads(response.text)
    print(result)
    address={'address':result}
    return render(request,'index.html',result)
    

    
