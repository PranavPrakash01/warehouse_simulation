# ui/control_panel.py

import pygame
import pygame.gfxdraw  # Import pygame.gfxdraw for drawing rounded rectangles

class ControlPanel:
    def __init__(self, screen, control_panel_frame):
        self.screen = screen
        self.control_panel_frame = control_panel_frame
        self.button_width = 70
        self.button_height = 30
        self.button_radius = 5  # Radius for rounded corners

        # Play button
        self.play_button = pygame.Rect(control_panel_frame.left + 10, control_panel_frame.top + (control_panel_frame.height - self.button_height) // 2, self.button_width, self.button_height)

        # Pause button
        self.pause_button = pygame.Rect(self.play_button.right + 10, self.play_button.top, self.button_width, self.button_height)

        # Stop button
        self.stop_button = pygame.Rect(self.pause_button.right + 10, self.play_button.top, self.button_width, self.button_height)

        # Decrease the width of the event log box and add padding to the right
        padding_right = 10
        self.event_log_box = pygame.Rect(self.stop_button.right + 10, self.play_button.top, control_panel_frame.width - (self.stop_button.right + 10) - padding_right, 50)

        self.event_log_font = pygame.font.Font(None, 20)
        self.event_log = []

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.play_button.collidepoint(mouse_pos):
                print("Play button clicked")
                # Add your play button logic here

            elif self.pause_button.collidepoint(mouse_pos):
                print("Pause button clicked")
                # Add your pause button logic here

            elif self.stop_button.collidepoint(mouse_pos):
                print("Stop button clicked")
                # Add your stop button logic here

    def draw_control_panel(self):
        # Draw buttons with rounded corners
        pygame.draw.rect(self.screen, (95, 95, 95), self.play_button, border_radius=self.button_radius)
        pygame.draw.rect(self.screen, (95, 95, 95), self.pause_button, border_radius=self.button_radius)
        pygame.draw.rect(self.screen, (95, 95, 95), self.stop_button, border_radius=self.button_radius)

        # Draw text on buttons
        self.draw_text("Play", self.play_button)
        self.draw_text("Pause", self.pause_button)
        self.draw_text("Stop", self.stop_button)

        # Draw event log box
        pygame.draw.rect(self.screen, (75, 75, 75), self.event_log_box, border_radius=4)
        self.draw_event_log()

    def draw_text(self, text, button_rect):
        font = pygame.font.Font(None, 24)
        text_surface = font.render(text, True, (255, 255, 255))  # Set text color to white
        text_rect = text_surface.get_rect(center=button_rect.center)
        self.screen.blit(text_surface, text_rect)

    def draw_event_log(self):
        for i, log_entry in enumerate(self.event_log):
            text_surface = self.event_log_font.render(log_entry, True, (0, 0, 0))
            text_rect = text_surface.get_rect(topleft=(self.event_log_box.left + 10, self.event_log_box.top + 10 + i * 30))
            self.screen.blit(text_surface, text_rect)
