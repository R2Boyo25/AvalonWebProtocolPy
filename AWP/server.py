import socket

class Server:
    def __init__(self, port):
        self.socket = socket.socket()