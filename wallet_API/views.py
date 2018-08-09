from django.shortcuts import render
from .pythonJsConnector import generateAddress
# Create your views here.

def generateWallateAddress(request):
    address=generateAddress()
    result={"address":address}
    print(result)
    return render(request,'index.html',result)
    
    
