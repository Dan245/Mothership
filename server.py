from classes.network import Server
from constants import *

server = Server(CLIENT_IP, PORT)


print("[STARTING] server is starting...")
server.start()
