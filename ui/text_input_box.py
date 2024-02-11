# text_input_box.py
import pygame as pg

pg.init()
COLOR_INACTIVE = pg.Color('black')  # Change inactive color to grey
COLOR_ACTIVE = pg.Color('white')  # Change active color to white
COLOR_BACKGROUND = pg.Color('black')
FONT = pg.font.Font(None, 22)


class InputBox:
    def __init__(self, x, y, w, h, text='', placeholder=""):
        self.rect = pg.Rect(x, y, w, h)
        self.color_inactive = COLOR_INACTIVE
        self.color_active = COLOR_ACTIVE
        self.color = self.color_inactive
        self.color_background = COLOR_BACKGROUND
        self.text = text
        self.placeholder = placeholder
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    pass
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def get_text(self):
        temp = self.text
        self.text = ''
        self.active = not self.active
        print(temp)
        #return temp

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        # Set background color to black
        pg.draw.rect(screen, (0, 0, 0), self.rect, border_radius=4)
        
        # Draw rounded rectangle for the input box with border color change
        pg.draw.rect(screen, (255, 255, 255) if self.active else (100, 100, 100), self.rect, border_radius=4, width=1)

        # If the text is empty, draw the placeholder text
        if not self.text:
            placeholder_surface = FONT.render(self.placeholder, True, (150, 150, 150))
            screen.blit(placeholder_surface, (self.rect.x + 5, self.rect.y + 10))
        else:
            screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 10))

