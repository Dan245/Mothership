import pygame


class Window:                                               # WINDOW CLASS
    pygame.display.set_caption("Mothership")                # Set caption and icon for the window
    icon = pygame.image.load('assets\\window_logo.png')     # *
    pygame.display.set_icon(icon)                           # *
    monitor = pygame.display.Info()                         # get starting size of window
    size = (monitor.current_w/2, monitor.current_h/2)       # *
    flags = pygame.RESIZABLE                                # starting flags
    fullscreen = False                                      # bool for controlling fullscreen
    screen = pygame.display.set_mode(size, flags)           # Set the display
    pygame.init()                                           # Start pygame

    @staticmethod
    def update(elements=None):                              # UPDATE function
        for event in pygame.event.get():                    # for each event
            if event.type == pygame.QUIT:                   # quit if quit event occurs or user presses 'q'
                return False                                # *
            elif event.type == pygame.KEYDOWN:              # *
                if event.key == pygame.K_q:                 # *
                    return False                            # *
            if event.type == pygame.VIDEORESIZE and not Window.fullscreen:
                Window.size = (event.w, event.h)
                Window.screen = pygame.display.set_mode(Window.size, Window.flags)
                if elements:
                    for element in elements:
                        element.update()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_f:
                    Window.fullscreen = not Window.fullscreen
                    if Window.fullscreen:
                        Window.flags = pygame.FULLSCREEN
                        size = (Window.monitor.current_w, Window.monitor.current_h)
                        Window.screen = pygame.display.set_mode(size, Window.flags)

                    else:
                        Window.flags = pygame.RESIZABLE
                        Window.screen = pygame.display.set_mode(Window.size, Window.flags)
                    if elements:
                        for element in elements:
                            element.update()
            if elements:
                for element in elements:
                    function = element.check_events(event)
                    if function:
                        return function

        return True


class Screen:
    screen = Window.screen
    def __init__(self, elements, screen_id, background):
        self.elements = elements
        self.bg = background
        self.screen_id = screen_id
        self.next_screen = self.screen_id

    def run(self):
        s = Screen.screen
        s.fill(self.bg)
        for element in self.elements:
            element.draw()
