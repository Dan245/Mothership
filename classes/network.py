import threading
from constants import *


class Network:
    hdr = HEADER
    frmt = FORMAT
    dc_msg = DISCONNECT_MESSAGE
    rcv_msg = RECEIVED_MESSAGE

    def __init__(self, server_ip, port, kill_msg=None):
        self.server_ip = server_ip
        self.port = port
        self.addr = (server_ip, port)
        self.endpoint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.kill_msg = kill_msg

    def send(self, msg, endpoint=None, addr=None):
        endpoint = self.endpoint if not endpoint else endpoint

        message = msg.encode(Network.frmt)
        msg_length = len(message)

        send_length = str(msg_length).encode(Network.frmt)
        send_length += b' ' * (Network.hdr - len(send_length))

        endpoint.send(send_length)
        endpoint.send(message)
        if msg != Network.rcv_msg:
            self.recv(endpoint, addr)

    def recv(self, endpoint=None, addr=None):
        endpoint = self.endpoint if not endpoint else endpoint
        msg_length = endpoint.recv(Network.hdr).decode(Network.frmt)

        if msg_length:
            msg_length = int(msg_length)
            msg = endpoint.recv(msg_length).decode(Network.frmt)
            print(f"[{addr}] {msg}")
            if msg != Network.rcv_msg:
                print("Sending Received Message")
                self.send(Network.rcv_msg, endpoint, addr)
                return msg
        else:
            return False


class Server(Network):
    def __init__(self, server_ip, port):
        super().__init__(server_ip, port)

    def start(self):
        self.endpoint.bind(self.addr)
        self.endpoint.listen()
        print(f"[LISTENING] Server is listening on {self.server_ip}")
        while True:
            client_endpoint, address = self.endpoint.accept()
            new_thread = threading.Thread(target=self.handle_client, args=(client_endpoint, address))
            new_thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    def handle_client(self, cl_endpoint, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:
            msg = self.recv(cl_endpoint, addr)
            if msg:
                try:
                    self.send("blah", cl_endpoint, addr)
                    if msg == Network.dc_msg:
                        connected = False
                except ConnectionResetError:
                    connected = False
        print(f"[CONNECTION LOST] {addr} has disconnected")
        cl_endpoint.close()


class Client(Network):
    def __init__(self, server_ip, port):
        super().__init__(server_ip, port)

    def connect(self):
        self.endpoint.connect(self.addr)

    def disconnect(self):
        self.endpoint.close()
