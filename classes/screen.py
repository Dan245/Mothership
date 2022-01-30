# imports
import pygame


# window class
class Window:
    # init pygame caption and icon
    pygame.display.set_caption("Mothership")
    icon = pygame.image.load('assets\\window_logo.png')
    pygame.display.set_icon(icon)

    # init pygame display
    monitor = pygame.display.Info()
    size = (monitor.current_w / 2, monitor.current_h / 2)
    flags = pygame.RESIZABLE
    screen = pygame.display.set_mode(size, flags)
    pygame.init()

    # init bools
    fullscreen = False
    free = True

    # update function
    @staticmethod
    def update(current_screen, elements=None):
        # for event in pygame
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:  # quit game
                return False
            elif event.type == pygame.VIDEORESIZE and not Window.fullscreen:  # redraw window at new window size
                Window.size = (event.w, event.h)
                Window.screen = pygame.display.set_mode(Window.size, Window.flags)
                # redraw elements
                if elements:
                    for element in elements:
                        element.update()
            elif event.type == pygame.KEYDOWN:
                # check if input box is active (if it is block other keyboard functions)
                for element in elements:
                    try:
                        if element.active:
                            Window.free = False
                            break
                        else:
                            Window.free = True
                    except:
                        continue
                if event.key == pygame.K_q and Window.free:  # quit game
                    return False
                elif event.key == pygame.K_f and Window.free:  # toggle fullscreen
                    Window.fullscreen = not Window.fullscreen
                    if Window.fullscreen:
                        Window.flags = pygame.FULLSCREEN
                        size = (Window.monitor.current_w, Window.monitor.current_h)
                        Window.screen = pygame.display.set_mode(size, Window.flags)

                    else:
                        Window.flags = pygame.RESIZABLE
                        Window.screen = pygame.display.set_mode(Window.size, Window.flags)

                    # update elements
                    if elements:
                        for element in elements:
                            element.update()
                elif event.key == pygame.K_ESCAPE and Window.fullscreen:  # get out of fullscreen
                    Window.fullscreen = not Window.fullscreen
                    Window.flags = pygame.RESIZABLE
                    Window.screen = pygame.display.set_mode(Window.size, Window.flags)

                    # update elements
                    if elements:
                        for element in elements:
                            element.update()
            # run event check function for every element onscreen
            if elements:
                for element in elements:
                    link = element.check_events(event)
                    if link:
                        # return link if button pressed
                        return 0 if link == "QUIT" else link
        # return the current screen
        return current_screen


# screen class
class Screen:

    def __init__(self, elements, screen_id, background):
        # init vars
        self.elements = elements
        self.bg = background
        self.screen_id = screen_id
        self.next_screen = self.screen_id

    def run(self, l_s):
        # grab pygame display
        s = Window.screen

        # fill screen
        s.fill(self.bg)

        # if first time running screen update elements
        if l_s != self.screen_id:
            for element in self.elements:
                element.update()

        # draw all elements
        for element in self.elements:
            element.deraw()
