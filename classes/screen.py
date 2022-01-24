import pygame


class Window:
    pygame.display.set_caption("Mothership")
    icon = pygame.image.load('assets\\window_logo.png')
    pygame.display.set_icon(icon)
    monitor = pygame.display.Info()
    size = (monitor.current_w / 2, monitor.current_h / 2)
    flags = pygame.RESIZABLE
    fullscreen = False
    screen = pygame.display.set_mode(size, flags)
    pygame.init()
    free = True

    @staticmethod
    def update(elements=None):
        for event in pygame.event.get():
            if event.type == pygame.WINDOWCLOSE or event.type == pygame.QUIT:
                return False
            elif event.type == pygame.VIDEORESIZE and not Window.fullscreen:
                Window.size = (event.w, event.h)
                Window.screen = pygame.display.set_mode(Window.size, Window.flags)
                if elements:
                    for element in elements:
                        element.update()
            elif event.type == pygame.KEYDOWN:
                for element in elements:
                    try:
                        if element.active:
                            Window.free = False
                            break
                        else:
                            Window.free = True
                    except:
                        continue
                if event.key == pygame.K_q and Window.free:
                    return False
                elif event.key == pygame.K_f and Window.free:
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
            element.deraw()
