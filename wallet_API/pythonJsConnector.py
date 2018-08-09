from Naked.toolshed.shell import execute_js, muterun_js
import sys

def generateAddress():
    response = muterun_js('nodeApp/index.js')
    return response.stdout.rstrip()
       