from django.shortcuts import render
import json
import requests
from .forms import WalletForm
# Create your views here.
ADMIN_SERVER='http://127.0.0.1:5005'
def generateWallateAddress(request):
    reqjson={
        "method": "wallet_propose",
        "params": []
    }
    response =requests.post(ADMIN_SERVER,json=reqjson)
    result=json.loads(response.text)
    address={'address':result}
    walletForm=WalletForm(result)
    if walletForm.is_valid():
        walletForm.save()
        print("saved")
    return render(request,'index.html',address)
    

    
