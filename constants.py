import socket

# server stuff
HEADER = 256
PORT = 49009
CLIENT_IP = socket.gethostbyname(socket.gethostname())
CLIENT_ADDR = (CLIENT_IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

# game client
FPS = 60
CAPTION = "Mothership"

# colors
WHITE = (255, 255, 255)
GREEN = (0, 204, 0)
ORANGE = (255, 165, 0)
BLUE = (0, 165, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
RED = (255, 0, 0)
LIGHT_SLATE_GREY = (33, 33, 33)
BRIGHT_GREY = (120, 120, 120)
GREY = (105, 105, 105)
DARK_WHITE = (235, 235, 235)
LIGHT_CYAN = (100, 255, 255)
BRIGHT_GREEN = (0, 184, 0)

# fonts
GINGA_INTER = "assets\\fonts\\Font_GINGA_INTER.ttf"
MEDABOTS = "assets\\fonts\\Medabots.otf"

# screens
QUIT = "QUIT"
TITLE = 1
HOST = 2
JOIN = 3
HOW2PLAY = 4
OPTIONS = 5
GAME = 6

# images
GAME_LOGO = "assets\\window_logo.png"
