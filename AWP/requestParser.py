import json
import pkg_resources
from .getCode import getCode

avalonversion = pkg_resources.require("AWP")[0].version

def parseVersion(verstr) -> str:
    return verstr.split('/')[1]

def parseRequest(request) -> str, str, str, dict or list:
    lines = request.split('\n')
    rtype, path, rver = lines[0].split()
    ver = parseVersion(rver)

    rdata = lines[1:]
    data = json.loads("\n".join(rdata))

    return rtype, path, ver, data


def formatRequest(rtype, path, data) -> str:
    return "{type} {path} AWP/{ver}\n{data}".format(
        type = rtype, 
        path = path, 
        data = json.dumps(data), 
        ver = avalonversion
    )

def formatResponse(code, doc, data) -> str:
    return "AWP/{ver} {code} {codeText}\n{doc}\n{data}".format(
        code = code, 
        codeText = getCode(code), 
        ver = avalonversion, 
        doc = doc, 
        data = json.dumps(data)
    )