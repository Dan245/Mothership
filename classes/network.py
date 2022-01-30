# imports
import threading
from constants import *


# base network class
class Network:
    # constants
    hdr = HEADER
    frmt = FORMAT
    dc_msg = DISCONNECT_MESSAGE

    def __init__(self, server_ip, port, kill_msg=None):
        # setting up socket stuff
        self.server_ip = server_ip  # target ip
        self.port = port  # port number
        self.addr = (server_ip, port)
        self.endpoint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # new instance of socket
        self.kill_msg = kill_msg  # admin kill message

    # send function
    def send(self, msg, endpoint=None, addr=None):
        # get the desired endpoint
        endpoint = self.endpoint if not endpoint else endpoint

        # encode message in bytes format
        message = msg.encode(Network.frmt)

        # get length of message and pad it into a variable of fixed length
        msg_length = len(message)
        send_length = str(msg_length).encode(Network.frmt)
        send_length += b' ' * (Network.hdr - len(send_length))

        # send the length of message and message to the other end of socket
        endpoint.send(send_length)
        endpoint.send(message)

    # receive function
    def recv(self, endpoint=None, addr=None):
        # get desired endpoint
        endpoint = self.endpoint if not endpoint else endpoint

        # grab the message length
        msg_length = endpoint.recv(Network.hdr).decode(Network.frmt)

        # if there was a message length, wait for new message with that length, and print message to console
        if msg_length:
            msg_length = int(msg_length)
            msg = endpoint.recv(msg_length).decode(Network.frmt)
            print(f"[{addr}] {msg}")
            # return the message
            return msg
        else:
            return False


# server class
class Server(Network):
    def __init__(self, server_ip, port):
        super().__init__(server_ip, port)  # init base class
        # init bool
        self.active = False

    # start server function
    def start(self):
        # init the server socket endpoint
        self.endpoint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.endpoint.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # allow the address to be reused
        self.endpoint.settimeout(1)  # set it in timeout mode
        self.endpoint.bind(self.addr)  # set address of socket

        # start listening for connections
        self.active = True
        self.endpoint.listen()
        print(f"[LISTENING] Server is listening on {self.server_ip}")

        while self.active:
            # while server is running, accept new connections
            try:
                client_endpoint, address = self.endpoint.accept()
                # start new daemon thread to handle the client
                new_thread = threading.Thread(target=self.handle_client, args=(client_endpoint, address), daemon=True)
                new_thread.start()
                print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 2}")
            except:
                pass
        # close server socket once server is no longer running
        print("[CLOSING] Server closing")
        self.endpoint.close()

    # handling client function
    def handle_client(self, cl_endpoint, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:
            # continuously receive messages
            # this would look very different if I'd set up the game code
            msg = self.recv(cl_endpoint, addr)
            if msg:
                # quit loop if error occurs or user sends disconnect message
                try:
                    if msg == DISCONNECT_MESSAGE:  # stop server if someone sends the stop server command
                        connected = False
                        self.active = False
                        continue
                except ConnectionResetError:
                    connected = False
        # close endpoint once user disconnects
        print(f"[CONNECTION LOST] {addr} has disconnected")
        cl_endpoint.close()


# client class
class Client(Network):
    def __init__(self, server_ip, port):
        super().__init__(server_ip, port)  # init base class

    # connect to the desired address
    def connect(self):
        print(self.addr)
        self.endpoint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.endpoint.connect(self.addr)

    # disconnect from server
    def disconnect(self):
        self.endpoint.close()
