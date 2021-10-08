import socket
import json

from .logger import getLogger
from .requestParser import parseResponse, formatRequest

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

        self.socket.send(formatRequest(rType.upper(), path, data))

        resp = self._receive(buffersize)

        self.socket.close()
        self.socket = socket.socket()

        return resp
    
    def _receive(self, buffersize = 4096):
        resp = self.socket.recv(buffersize).decode()

        ver, code, codeText, text, data = parseResponse(resp)

        return code, text, data
    
    def get(self, *args, **kwargs):
        return self.request('GET', *args, **kwargs)

    def connect(self):
        self.socket.connect((self.address, self.port))