import socket

class Client:
    def __init__(self, address, port):
        self.socket = socket.socket()

    def connect(self):
