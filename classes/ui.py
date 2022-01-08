import pygame


class Window:
    pygame.display.set_caption("Mothership")
    a = pygame.image.load('assets\\window_logo.png')
    pygame.display.set_icon(a)
    window = pygame.display.Info()
    size = (window.current_w/2, window.current_h/2)
    aspect_ratio = size[0]/size[1]
    flags = pygame.SCALED | pygame.RESIZABLE
    screen = pygame.display.set_mode(size, flags)
    pygame.init()

    def update(self):



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
        text = self.font_obj.render(self.text, True, self.color)

        text_rect = text.get_rect()
        text_rect.center = self.get_pos()

        Window.screen.blit(text, text_rect)


class Button(pygame.sprite.Sprite):
    def __init__(self, text, font, text_color, text_pos_ratio, text_size_ratio, rect_color, rect_pos_ratio, rect_size_ratio):
        super().__init__()

        self.text = Text(text, font, text_color, text_pos_ratio, text_size_ratio)

        self.image = pygame.Surface([width, height])
        self.color = rect_color
        self.image.fill(self.color)
        self.alpha = 0

        self.rect = self.image.get_rect()

    def get_color(self):
        pass

    def update(self):

        self.image = pygame.Surface([width, height])
        self.image.set_alpha(self.alpha)
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.center = (center_x, center_y)
