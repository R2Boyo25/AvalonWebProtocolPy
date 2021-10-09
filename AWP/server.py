import socket
import json

from .logger import getLogger
from .requestParser import parseRequest, formatResponse

_logger = getLogger('avalonserver')

class Server:
    def __init__(self, address = '0.0.0.0', port=5001):
        self.socket = socket.socket()
        self.routes = []
        self.address = address
        self.port = port

    def route(self, path):
        def route_decorator(function):
            self.routes.append(
                {
                    'path' : path, 
                    'func' : function
                }
            )

            _logger.debug('Added route ' + path)
            
        return route_decorator

    def _receive(self, conn, buffersize = 4096):
        res = conn.recv(buffersize)

        return parseRequest(res)

    def serve(self, backlog = 5):
        _logger.debug('Binding to ' + str((self.address, self.port)))

        self.socket.bind((self.address, self.port))

        _logger.debug('Bound to ' + str((self.address, self.port)))
        
        _logger.debug('Listening on ' + str((self.address, self.port)) + ' with backlog of ' + str(backlog))

        self.socket.listen(backlog)

        while True:
            conn, addr = self.socket.accept()
            
            _logger.debug('Request from ' + str(addr))

            rType, rPath, rVer, rData = self._receive(conn)

            for route in self.routes:
                if route['path'] == rPath:
                    res = route['func'](rType, rPath, rData)
                    if type(res) == str:
                        reCode = 200
                        reData = {}
                        reDoc = res

                    else:
                        reCode = res[0]
                        reData = res[1]
                        reDoc = res[2]

                    conn.send(formatResponse(reCode, reDoc, reData))

                    _logger.info(str(addr) + ": " + rType + " " + rPath + " " + str(reCode))

