import pygame


class Window:
    pygame.display.set_caption("Mothership")
    icon = pygame.image.load('assets\\window_logo.png')
    pygame.display.set_icon(icon)
    monitor = pygame.display.Info()
    size = (monitor.current_w/2, monitor.current_h/2)
    flags = pygame.RESIZABLE
    fullscreen = False
    screen = pygame.display.set_mode(size, flags)
    pygame.init()

    @staticmethod
    def update():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.VIDEORESIZE and not Window.fullscreen:
                Window.size = (event.w, event.h)
                Window.screen = pygame.display.set_mode(Window.size, Window.flags)
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




        return True


class Text:
    def __init__(self, text, font, color, pos_ratio, size_ratio):
        self.text = text
        self.font = font
        self.color = color
        self.x_r, self.y_r = pos_ratio
        self.s_r = size_ratio
        self.font_obj = pygame.font.Font(self.font, self.get_size())

    def get_size(self):
        ratio = self.get_ratio()
        s_size = [Window.screen.get_width(), Window.screen.get_height()]
        font_size = []
        for i in range(len(s_size)):
            font_size.append((s_size[i]/(self.s_r[i]-0.3))/ratio[i])

        return round(min(font_size))

    def get_ratio(self):
        sample_font = pygame.font.Font(self.font, 1)
        width, height = sample_font.size(self.text)
        return width, height

    def get_pos(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        return s_w/self.x_r, s_h/self.y_r


    def update(self):
        self.font_obj = pygame.font.Font(self.font, self.get_size())
        text = self.font_obj.render(self.text, True, self.color)

        text_rect = text.get_rect()
        text_rect.center = self.get_pos()

        Window.screen.blit(text, text_rect)


class Button(pygame.sprite.Sprite):
    def __init__(self, text, font, text_color, rect_color, pos_ratio, size_ratio):
        super().__init__()
        text_size_ratio = (size_ratio[0]*0.8, size_ratio[1]*0.8)
        text_pos_ratio = (pos_ratio[0], pos_ratio[1])
        self.text = Text(text, font, text_color, text_pos_ratio, text_size_ratio)

        self.x_r, self.y_r = pos_ratio
        self.w_r, self.h_r = size_ratio

        self.image = pygame.Surface(self.get_size())
        self.color = rect_color
        self.image.fill(self.color)
        self.alpha = 0

        self.rect = self.image.get_rect()

        self.group = pygame.sprite.GroupSingle()
        self.group.add(self)

    def get_pos(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        return s_w / self.x_r, s_h / self.y_r

    def get_size(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        return [s_w / self.w_r, s_h / self.h_r]

    def check_mouse(self):
        return True if self.rect.collidepoint(pygame.mouse.get_pos()) else False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                if self.check_mouse():
                    self.alpha = 50
                else:
                    self.alpha = 0


        self.image = pygame.Surface(self.get_size())
        self.image.set_alpha(self.alpha)
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.center = self.get_pos()
        self.group.draw(Window.screen)
        self.text.update()

