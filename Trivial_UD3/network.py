import socket
import pickle

#pickle decomposes object data into bytes "0""1"

class Network():
    def __init__(self):
        self.client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server="192.168.68.106"
        self.port=5555
        self.addr=(self.server, self.port)
        self.p=self.connect()

    def getP(self):
        return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode() #returns something once connected

        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)


