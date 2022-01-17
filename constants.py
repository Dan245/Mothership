import socket
import pygame

# server stuff
HEADER = 256
PORT = 49009
CLIENT_IP = socket.gethostbyname(socket.gethostname())
CLIENT_ADDR = (CLIENT_IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
RECEIVED_MESSAGE = "!RECEIVED"

# game client
FPS = 60
CAPTION = "Mothership"

# colors
WHITE = (255, 255, 255, 255)
GREEN = (0, 204, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 165, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
LIGHT_SLATE_GREY = (119, 136, 153)

# fonts
GINGA_INTER = "assets\\fonts\\Font_GINGA_INTER.ttf"
MEDABOTS = "assets\\fonts\\Medabots.otf"

# screens
TITLE = 0
HOST = 1
FIND = 2
HOW2PLAY = 3
OPTIONS = 4
LOBBY = 5
GAME = 6

# images
GAME_LOGO = "assets\\window_logo.png"
