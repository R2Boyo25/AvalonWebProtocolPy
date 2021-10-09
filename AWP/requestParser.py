import json
import pkg_resources
from .getCode import getCode
from .compress import compress, decompress

avalonversion = pkg_resources.require("AWP")[0].version

def parseVersion(verstr) -> str:
    return verstr.split('/')[1]

def parseRequest(request) -> (str, str, str, dict or list):
    request = decompress(request)

    lines = request.split('\n')
    rtype, path, rver = lines[0].split()
    ver = parseVersion(rver)

    rdata = lines[1:]
    data = json.loads("\n".join(rdata))

    return rtype, path, ver, data

def formatRequest(rtype, path, data) -> str:
    return compress(
            "{type} {path} AWP/{ver}\n{data}".format(
            type = rtype, 
            path = path, 
            data = json.dumps(data), 
            ver = avalonversion
        )
    )

def formatResponse(code, doc, data) -> str:
    return compress(
            "AWP/{ver} {code} {codeText}\n{doc}\n{data}".format(
            code = code, 
            codeText = getCode(code), 
            ver = avalonversion, 
            doc = doc, 
            data = json.dumps(data)
        )
    )

def parseResponse(resp) -> (str, str, str, str, list or dict):
    resp = decompress(resp)

    lines = resp.split('\n')
    for i, line in enumerate(lines):
        if line.strip().startswith('{'):
            datastart = i
    
    ver, code, *lcodeText = lines[0].split()
    codeText = " ".join(lcodeText)

    ldoc = lines[1:datastart]
    doc = '\n'.join(ldoc)

    ldata = lines[datastart:]
    rdata = '\n'.join(ldata)
    data = json.loads(rdata)

    return ver, code, codeText, doc, data