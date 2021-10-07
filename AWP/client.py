import socket
import json

from .logger import getLogger

_logger = getLogger('avalonclient')

class notConnectedError(Exception):
    pass

class Client:
    def __init__(self, address, port = 5001):
        self.socket = socket.socket()
        self.address = address
        self.port = port

    def request(self, rType = 'GET', path = '/', data = None, buffersize = 4096):

        data = data if data else {}

        self.connect()

        self.socket.send(
            json.dumps(
                {
                    "type" : rType.upper(),
                    "path" : path, 
                    "data" : data
                }
            ).encode()
        )

        resp = self._receive(buffersize)

        self.socket.close()

        return resp
    
    def _receive(self, buffersize = 4096):
        rresp = self.socket.recv(buffersize).decode()
        
        resp = json.loads(rresp)

        code = resp['code'] if 'code' in resp else 500
        data = resp['data'] if 'data' in resp else {}
        text = resp['doc'] if 'doc' in resp else "<t>No Response</t>"

        return code, text, data
    
    def get(self, *args, **kwargs):
        return self.request('GET', *args, **kwargs)

    def connect(self):
        self.socket.connect((self.address, self.port))