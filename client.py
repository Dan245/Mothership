import pygame
from constants import *
from classes.screen import Window
from classes.ui import InputBox
from screens.title import title
from screens.host import host
from screens.find import joinn
from ipcoder import get_ip_from_code
import game
from classes.network import Server, Client
import threading
import socket

screens = [title, host, joinn]

LAN_server = Server(CLIENT_IP, PORT)
LAN_client = Client(CLIENT_IP, PORT)
server_thread = threading.Thread(target=LAN_server.start, daemon=True)

window = Window.screen

clock = pygame.time.Clock()

playing = TITLE
last_screen = playing

while playing:
    playing = Window.update(playing, screens[playing - 1].elements)
    if not playing:
        continue
    if playing == HOST and playing != last_screen:
        server_thread = threading.Thread(target=LAN_server.start, daemon=True)
        server_thread.start()
        LAN_client.endpoint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        LAN_client.connect()
    elif playing == TITLE and playing != last_screen:
        try:
            LAN_client.send(DISCONNECT_MESSAGE)
            LAN_client.disconnect()

        except KeyboardInterrupt:
            pass
    elif playing == GAME and last_screen == JOIN:
        try:
            LAN_client = Client(get_ip_from_code(InputBox.ip_code), PORT)
            LAN_client.endpoint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            LAN_client.connect()
        except:
            LAN_client = Client(CLIENT_IP, PORT)
            playing = TITLE
            last_screen = playing
            continue
    elif playing == TITLE and last_screen == GAME:
        LAN_client.send(DISCONNECT_MESSAGE)
        LAN_client.disconnect()
    if playing != GAME:
        screens[playing - 1].run(last_screen)
    else:
        game.run()
    pygame.display.flip()
    last_screen = playing
    clock.tick(FPS)
    print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 2}")
pygame.quit()
