# necessary imports
import pygame
from classes.screen import Window
from constants import *


# base element class
class Element:
    # init function
    def __init__(self):
        # some default values to avoid errors for the default functions
        self.x_r, self.y_r, self.w_r, self.h_r = (1, 1, 1, 1)
        self.rect = pygame.Rect(1, 1, 1, 1)

    # get raw screen position based off of a formula (i.e. a screen with a width of 100px and a formula of 0.2 would return 20)
    def get_pos(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        return s_w * self.x_r, s_h * self.y_r

    # get raw size of object based off of formula
    def get_size(self):
        s_w = Window.screen.get_width()
        s_h = Window.screen.get_height()
        return [s_w * self.w_r, s_h * self.h_r]

    # default check event function
    def check_events(self, event):
        # update element if the mouse moves
        if event.type == pygame.MOUSEMOTION:
            self.update()

    # check if mouse is touching an element
    def check_mouse(self):
        return True if self.rect.collidepoint(pygame.mouse.get_pos()) else False

    # default update function
    def update(self):
        return

    # default draw function
    def deraw(self):
        return


# text class
class Text(Element):
    def __init__(self, text, font, color, pos_ratio, size_ratio):
        super().__init__()  # init element class
        # init vars from params
        self.text = text
        self.font = font
        self.color = color
        self.x_r, self.y_r = pos_ratio
        self.s_r = size_ratio
        self.size = 1
        # initialize the text
        self.update()

    # custom get size function because text is scaled with one num instead of two
    def get_size(self):
        # get w/h ratio of text
        ratio = self.get_ratio()
        # get screen size
        s_size = [Window.screen.get_width(), Window.screen.get_height()]
        # get the actual font width and height for the desired size
        font_size = []
        for i in range(len(s_size)):
            font_size.append((s_size[i] * self.s_r[i]) / ratio[i])
        # set the size to the smaller of the two numbers (to ensure no overlap)
        self.size = round(min(font_size))

    # get the width/height ratio
    def get_ratio(self):
        # make a sample font with the given text and return it's width and height
        sample_font = pygame.font.Font(self.font, 1)
        width, height = sample_font.size(self.text)
        return width, height

    # update function
    def update(self):
        # create new font object with the current size of screen
        self.get_size()
        self.font_obj = pygame.font.Font(self.font, self.size)
        self.text_render = self.font_obj.render(self.text, True, self.color)

        self.text_rect = self.text_render.get_rect()
        self.text_rect.center = self.get_pos()

    # draw function
    def deraw(self):
        # blit the text to the screen
        Window.screen.blit(self.text_render, self.text_rect)


# button class
class Button(pygame.sprite.Sprite, Element):
    def __init__(self, text, font, text_color, rect_color, pos_ratio, size_ratio, link):
        super().__init__()  # init sprite and element class

        # what screen the button will actually go to
        self.link = link

        # create text object
        text_size_ratio = (size_ratio[0] * 0.8, size_ratio[1] * 0.8)
        text_pos_ratio = (pos_ratio[0], pos_ratio[1])
        self.text = Text(text, font, text_color, text_pos_ratio, text_size_ratio)

        # create Surface object
        self.x_r, self.y_r = pos_ratio
        self.w_r, self.h_r = size_ratio
        self.image = pygame.Surface(self.get_size())
        self.color = rect_color
        self.image.fill(self.color)
        self.alpha = 0
        self.rect = self.image.get_rect()

        # create sprite group (necessary for blitting to the screen)
        self.group = pygame.sprite.GroupSingle()
        self.group.add(self)

        # update button
        self.update()

    # function for creating buttons in a list
    @staticmethod
    def create_buttons(button_texts, font, text_color, rect_color, start_pos, size_ratio, links):
        '''create a bunch of buttons, each with it's own text and link,
        and position them directly beneath one another'''
        buttons = []
        for button in range(len(button_texts)):
            pos = start_pos if not button else (start_pos[0], start_pos[1] + size_ratio[1] * len(buttons))
            new_button = Button(button_texts[button], font, text_color, rect_color, pos, size_ratio, links[button])
            buttons.append(new_button)
        # return the list of buttons
        return buttons

    # check events function
    def check_events(self, event):
        if event.type == pygame.MOUSEMOTION:  # change alpha of button if mouse is hovering over it
            self.alpha = 50 if self.check_mouse() else 0
            self.update()
        if event.type == pygame.MOUSEBUTTONDOWN:  # change alpha of button if mouse clicks on it
            self.alpha = 150 if self.check_mouse() else 0
            self.update()
        if event.type == pygame.MOUSEBUTTONUP:  # return the button's link if mouse pressed down and up on button
            if self.alpha == 150 and self.check_mouse():
                self.update()
                return self.link
            else:  # reset the button's alpha if it wasn't pressed
                self.alpha = 0
                self.update()

    # update function
    def update(self):
        # recreate the surface with new size
        self.image = pygame.Surface(self.get_size())
        self.image.set_alpha(self.alpha)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = self.get_pos()

        # update text object
        self.text.update()

    def deraw(self):
        # draw the surface and the text
        self.group.draw(Window.screen)
        self.text.deraw()


# input box class
class InputBox(Element):
    # global ip code var
    ip_code = ""

    def __init__(self, base_text, font, pos_ratio, size_ratio):
        super().__init__()  # init element class

        # constant colors (didn't bother implementing them as params since I'm only using one
        self.colors = [BRIGHT_GREY, GREY]
        self.text_colors = [BRIGHT_GREEN, GREEN]

        # init some vars
        self.active = False
        self.color = self.colors[self.active]
        self.base_text = base_text
        self.font = font

        # create text object with default message
        self.t_s_r = (size_ratio[0] * 0.6, size_ratio[1] * 0.6)
        self.t_p_r = (pos_ratio[0], pos_ratio[1])
        self.start_text = base_text
        self.text = Text(self.start_text, font, self.text_colors[0], self.t_p_r, self.t_s_r)

        # create rect object
        self.x_r, self.y_r = pos_ratio
        self.w_r, self.h_r = size_ratio
        self.rect = pygame.Rect(self.get_pos(), self.get_size())
        self.rect.center = self.get_pos()

    # check events function
    def check_events(self, event):
        super().check_events(event)  # check events of base class
        if event.type == pygame.MOUSEBUTTONDOWN:  # toggle typing mode on or off depending on where the user clicks
            temp = self.active
            if self.check_mouse():
                self.active = True
            else:
                self.active = False
                # set the ipcode to the inputted text when the user is done
                InputBox.ip_code = self.text.text
            if temp != self.active:
                # update if the state changes
                self.update()

        elif event.type == pygame.KEYDOWN and self.active:  # if user is typing in box
            if event.key == pygame.K_RETURN:  # stop typing, update code var and update text
                self.active = False
                InputBox.ip_code = self.text.text
                self.update()
            elif event.key == pygame.K_BACKSPACE:  # remove last character in string
                if self.text.text != self.base_text:
                    self.text.text = self.text.text[:-1]
                if self.text.text == "":  # set text to base text if string becomes empty
                    self.text.text = self.base_text
            elif event.unicode and ord(event.unicode.upper()) <= 90 and ord(event.unicode.upper()) >= 65:
                # if user types a letter, add it to the string
                if self.text.text == self.base_text:
                    # set the string to nothing if only the base text is there
                    self.text.text = ""
                if len(self.text.text) == 5:  # add hyphen in the middle
                    self.text.text += "-"
                if len(self.text.text) < 11:  # only allow 10 characters to be typed
                    self.text.text += event.unicode.upper()
            # update elements
            self.update()

    def update(self):
        # reinit rect
        self.color = self.colors[self.active]
        self.rect = pygame.Rect(self.get_pos(), self.get_size())
        self.rect.center = self.get_pos()

        # reinit text object
        self.text.update()

    def deraw(self):
        # draw rectangle
        pygame.draw.rect(Window.screen, self.color, self.rect, 15)

        # draw text
        self.text.deraw()
