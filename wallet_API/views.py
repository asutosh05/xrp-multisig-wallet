from django.shortcuts import render
import json
import requests
from .forms import WalletForm
from rest_framework.generics import LISTAPIView,CreateAPIView
from .serializers import WalletSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
ADMIN_SERVER='http://127.0.0.1:5005'
@api_view(["POST"])
def generateWallateAddress(request):
    reqjson={
        "method": "wallet_propose",
        "params": []
    }
    response =requests.post(ADMIN_SERVER,json=reqjson)
    result=json.loads(response.text)
    serializer = WalletSerializer(result)
    if serializer.is_valid():
        serializer.save()
        print("saved in db")
        return Response({"result":result})
    else:
        message={"message":"erron in datasave",
                    "error":"some error contact admin"
        }
        return Response(message)

    


    
