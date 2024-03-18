# sidebar_panel.py

import pygame
from ui.button_type1 import ButtonType1

class SidebarPanel:
    def __init__(self, screen, sidebar_frame):
        self.screen = screen
        self.sidebar_frame = sidebar_frame
        self.button_width = 200
        self.button_height = 30

        # Create instances of ButtonType1 for sidebar buttons
        self.sidebar_button1 = ButtonType1(self.screen, "Sidebar Button 1", pygame.Rect(sidebar_frame.left + 10, sidebar_frame.top + 10, self.button_width, self.button_height))
        self.sidebar_button2 = ButtonType1(self.screen, "Sidebar Button 2", pygame.Rect(sidebar_frame.left + 10, self.sidebar_button1.rect.bottom + 10, self.button_width, self.button_height))
        # Add more buttons as needed

    def handle_events(self, event):
        # Handle events for sidebar buttons
        self.sidebar_button1.handle_event(event)
        self.sidebar_button2.handle_event(event)
        # Handle events for additional sidebar buttons

    def draw_sidebar_panel(self):
        # Draw sidebar buttons
        self.sidebar_button1.draw()
        self.sidebar_button2.draw()
        # Draw additional sidebar buttons as needed
