responseCodes = {
    200 : "Success",
    404 : "Not Found"
}

def getCode(code):
    return responseCodes[code] if code in responseCodes else "Unknown"