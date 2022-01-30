# import 3rd party libs and other files
import pygame
import threading
from constants import *
from classes.screen import Window
from classes.ui import InputBox
from screens.title import title
from screens.host import host
from screens.find import joinn
from ipcoder import get_ip_from_code
import game
from classes.network import Server, Client

# list of screens
screens = [title, host, joinn, title]

# create server and client objects
LAN_server = Server(CLIENT_IP, PORT)
LAN_client = Client(CLIENT_IP, PORT)
# create server thread
server_thread = threading.Thread(target=LAN_server.start, daemon=True)

# init starting screen
playing = TITLE
last_screen = playing

# init clock
clock = pygame.time.Clock()

# game loop
while playing:
    # run update function and get the next screen
    playing = Window.update(playing, screens[playing - 1].elements)
    if not playing:
        # if no screen skip loop
        continue
        # if player just switched to home screen
    if playing == HOST and playing != last_screen:
        # restate new thread
        server_thread = threading.Thread(target=LAN_server.start, daemon=True)
        # start thread
        server_thread.start()
        # restate client endpoint socket
        LAN_client.endpoint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # connect to server socket
        LAN_client.connect()
    elif playing == TITLE and playing != last_screen:  # if player just swithced to title screen
        # attempt to disconnect from server (will fail if no one has connected to the server)
        try:
            LAN_client.send(DISCONNECT_MESSAGE)
            LAN_client.disconnect()

        except OSError:
            pass
    elif playing == GAME and last_screen == JOIN:  # if player just switched to game screen from join
        # try to connect to server using the code the user entered, if failed go back to title screen
        try:
            LAN_client = Client(get_ip_from_code(InputBox.ip_code), PORT)
            LAN_client.endpoint = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            LAN_client.connect()
        except:
            LAN_client = Client(CLIENT_IP, PORT)
            playing = TITLE
            last_screen = playing
            continue
    elif playing == TITLE and last_screen == GAME:  # If player just quit the game and went to title screen
        # disconnect from server
        LAN_client.disconnect()
    # run the run function of a ui screen if player is not on the game screen, otherwise run the game function
    if playing != GAME:
        screens[playing - 1].run(last_screen)
    else:
        game.run()
    # update display & last screen, tick the clock
    pygame.display.flip()
    last_screen = playing
    clock.tick(FPS)
# quit pygame
pygame.quit()
