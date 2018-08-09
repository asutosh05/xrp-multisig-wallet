from django.shortcuts import render
from .pythonJsConnector import *
# Create your views here.
def generateWallateAddress(request):
    address=generateAddress()
    result={"address":address}
    return render(request,'index.html',result)
    
    
    