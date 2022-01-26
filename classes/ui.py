import pygame
from classes.screen import Window
from constants import *


class Element:
    def __init__(self):
        self.x_r, self.y_r, self.w_r, self.h_r = (1, 1, 1, 1)
        self.rect = pygame.Rect(1, 1, 1, 1)

    def get_pos(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        return s_w * self.x_r, s_h * self.y_r

    def get_size(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        return [s_w * self.w_r, s_h * self.h_r]

    def check_events(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.update()

    def check_mouse(self):
        return True if self.rect.collidepoint(pygame.mouse.get_pos()) else False

    def update(self):
        return

    def deraw(self):
        return


class Text(Element):
    def __init__(self, text, font, color, pos_ratio, size_ratio):
        super().__init__()
        self.text = text
        self.font = font
        self.color = color
        self.x_r, self.y_r = pos_ratio
        self.s_r = size_ratio
        self.size = 1
        self.get_size()
        self.font_obj = pygame.font.Font(self.font, self.size)
        self.text_render = self.font_obj.render(self.text, True, self.color)

        self.text_rect = self.text_render.get_rect()
        self.update()

    def get_size(self):
        ratio = self.get_ratio()
        s_size = [Window.screen.get_width(), Window.screen.get_height()]
        font_size = []
        for i in range(len(s_size)):
            font_size.append((s_size[i] * self.s_r[i]) / ratio[i])

        self.size = round(min(font_size))

    def get_ratio(self):
        sample_font = pygame.font.Font(self.font, 1)
        width, height = sample_font.size(self.text)
        return width, height

    def get_pos(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        return s_w * self.x_r, s_h * self.y_r

    def update(self):
        self.get_size()
        self.font_obj = pygame.font.Font(self.font, self.size)
        self.text_render = self.font_obj.render(self.text, True, self.color)

        self.text_rect = self.text_render.get_rect()
        self.text_rect.center = self.get_pos()

    def deraw(self):
        Window.screen.blit(self.text_render, self.text_rect)


class Button(pygame.sprite.Sprite, Element):
    def __init__(self, text, font, text_color, rect_color, pos_ratio, size_ratio, link):
        super().__init__()

        self.link = link

        text_size_ratio = (size_ratio[0] * 0.8, size_ratio[1] * 0.8)
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
        self.update()

    @staticmethod
    def create_buttons(button_texts, font, text_color, rect_color, start_pos, size_ratio, links):
        buttons = []
        for button in range(len(button_texts)):
            pos = start_pos if not button else (start_pos[0], start_pos[1] + size_ratio[1] * len(buttons))
            new_button = Button(button_texts[button], font, text_color, rect_color, pos, size_ratio, links[button])
            buttons.append(new_button)
        return buttons

    def get_pos(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        return s_w * self.x_r, s_h * self.y_r

    def get_size(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        return [s_w * self.w_r, s_h * self.h_r]

    def check_events(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.alpha = 50 if self.check_mouse() else 0
            self.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.alpha = 150 if self.check_mouse() else 0
            self.update()
        if event.type == pygame.MOUSEBUTTONUP:
            if self.alpha == 150 and self.check_mouse():
                self.update()
                return self.link
            else:
                self.alpha = 0
                self.update()

    def update(self):
        self.image = pygame.Surface(self.get_size())
        self.image.set_alpha(self.alpha)
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.center = self.get_pos()
        self.text.update()

    def deraw(self):
        self.group.draw(Window.screen)
        self.text.deraw()


class InputBox(Element):
    ip_code = ""
    def __init__(self, base_text, font, pos_ratio, size_ratio):
        super().__init__()
        self.colors = [BRIGHT_GREY, GREY]
        self.text_colors = [BRIGHT_GREEN, GREEN]
        self.active = False
        self.color = self.colors[self.active]
        self.base_text = base_text
        self.font = font

        self.t_s_r = (size_ratio[0] * 0.6, size_ratio[1] * 0.6)
        self.t_p_r = (pos_ratio[0], pos_ratio[1])
        self.start_text = base_text
        self.text = Text(self.start_text, font, self.text_colors[0], self.t_p_r, self.t_s_r)
        self.x_r, self.y_r = pos_ratio
        self.w_r, self.h_r = size_ratio
        self.rect = pygame.Rect(self.get_pos(), self.get_size())
        self.rect.center = self.get_pos()
        self.delete = False

    def check_events(self, event):
        super().check_events(event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            temp = self.active
            if self.check_mouse():
                self.active = True
            else:
                self.active = False
                InputBox.ip_code = self.text.text
            if temp != self.active:
                self.text = Text(self.text.text, self.font, self.text_colors[self.active], self.t_p_r, self.t_s_r)
                self.update()

        elif event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_RETURN:
                self.active = False
                InputBox.ip_code = self.text.text
                self.text = Text(self.text.text, self.font, self.text_colors[self.active], self.t_p_r, self.t_s_r)
            elif event.key == pygame.K_BACKSPACE:
                if self.text.text != self.base_text:
                    self.text.text = self.text.text[:-1]
                if self.text.text == "":
                    self.text.text = self.base_text
            elif event.unicode and ord(event.unicode.upper()) <= 90 and ord(event.unicode.upper()) >= 65:
                if self.text.text == self.base_text:
                    self.text.text = ""
                if len(self.text.text) < 11:
                    self.text.text += event.unicode.upper()
                if len(self.text.text) == 5:
                    self.text.text += "-"
            self.update()

    def update(self):
        self.color = self.colors[self.active]
        self.rect = pygame.Rect(self.get_pos(), self.get_size())
        self.rect.center = self.get_pos()
        self.text.update()

    def deraw(self):
        pygame.draw.rect(Window.screen, self.color, self.rect, 15)
        self.text.deraw()



