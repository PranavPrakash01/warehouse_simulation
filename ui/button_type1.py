# button_type1.py
import pygame

class ButtonType1:
    def __init__(self, screen, text, rect, callback=None, callback_args=None):
        self.screen = screen
        self.text = text
        self.rect = rect
        self.callback = callback
        self.callback_args = callback_args
        self.button_color = (50, 50, 50)
        self.original_color_border = (100, 100, 100)
        self.hover_color_border = (255, 255, 255)
        self.click_color = (150, 150, 150)
        self.button_radius = 5
        self.hovered = False
        self.clicked = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(mouse_pos) and self.callback:
                self.clicked = True
                if self.callback_args:
                    self.callback(self.callback_args())
                else:
                    self.callback()
        elif event.type == pygame.MOUSEBUTTONUP:
            self.clicked = False
        elif event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)

    def draw(self):
        if self.clicked:
            border_color = self.original_color_border
            button_color = self.click_color
        elif self.hovered:
            border_color = self.hover_color_border
            button_color = self.button_color
        else:
            border_color = self.original_color_border
            button_color = self.button_color

        pygame.draw.rect(self.screen, button_color, self.rect, border_radius=self.button_radius)
        pygame.draw.rect(self.screen, border_color, self.rect, border_radius=self.button_radius, width=1)
        self.draw_text()

    def draw_text(self):
        font = pygame.font.Font(None, 22)
        text_surface = font.render(self.text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=self.rect.center)
        text_with_antialias = pygame.Surface(text_rect.size, pygame.SRCALPHA)
        text_with_antialias.blit(text_surface, (0, 0))
        self.screen.blit(text_with_antialias, text_rect)
