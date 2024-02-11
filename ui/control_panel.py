# ui/control_panel.py

import pygame
import pygame.gfxdraw  
from ui.text_input_box import InputBox

class ControlPanel:
    def __init__(self, screen, control_panel_frame, simulation):
        self.screen = screen
        self.control_panel_frame = control_panel_frame
        self.button_width = 70
        self.button_height = 30
        self.button_radius = 5  # Radius for rounded corners
        self.simulation = simulation
        self.button_color = (50, 50, 50)
        self.button_color_border = (100, 100, 100)
        self.event_log = simulation.event_log 

        # Play button
        self.run_button = pygame.Rect(control_panel_frame.left + 10, control_panel_frame.top + 10, self.button_width, self.button_height)

        # Pause button
        self.pause_button = pygame.Rect(self.run_button.right + 10, self.run_button.top, self.button_width, self.button_height)

        # Stop button
        self.stop_button = pygame.Rect(self.pause_button.right + 10, self.run_button.top, self.button_width, self.button_height)

        # Print all logs
        self.show_logs_button = pygame.Rect(control_panel_frame.left + 10, self.run_button.bottom + 10, self.stop_button.right - self.run_button.left, self.button_height + 5)

        # Decrease the width of the event log box and add padding to the right

        self.event_log_box = pygame.Rect(self.stop_button.right + 10, control_panel_frame.top+10 , control_panel_frame.width//2 + 75, 80)

        # Create an instance of InputBox for the text input
        self.text_input_box = InputBox(self.event_log_box.right + 10, control_panel_frame.top + 10, 155, 32, placeholder="Enter Dispatch Loc")

        # Dispatch buttom
        self.dispatch_button = pygame.Rect(self.event_log_box.right  + 10, self.text_input_box.rect.bottom + 10, 155, self.button_height + 5)

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.run_button.collidepoint(mouse_pos):
                self.simulation.run()

            elif self.pause_button.collidepoint(mouse_pos):
                print("Pause button clicked")
                # Add your pause button logic here

            elif self.stop_button.collidepoint(mouse_pos):
                self.simulation.stop()

            elif self.show_logs_button.collidepoint(mouse_pos):
                for log in self.event_log.all_logs:
                    print(log)

            elif self.dispatch_button.collidepoint(mouse_pos):
                print(self.text_input_box.get_text())

        # Handle events for the text input box
        self.text_input_box.handle_event(event)

    def draw_control_panel(self):
        # Draw buttons with rounded corners
        pygame.draw.rect(self.screen, self.button_color, self.run_button, border_radius=self.button_radius)
        pygame.draw.rect(self.screen, self.button_color, self.pause_button, border_radius=self.button_radius)
        pygame.draw.rect(self.screen, self.button_color, self.stop_button, border_radius=self.button_radius)
        pygame.draw.rect(self.screen, self.button_color, self.show_logs_button, border_radius=self.button_radius)
        pygame.draw.rect(self.screen, self.button_color, self.dispatch_button, border_radius=self.button_radius)

        # Draw grey borders around the buttons
        pygame.draw.rect(self.screen, self.button_color_border, self.run_button, border_radius=self.button_radius, width=1)
        pygame.draw.rect(self.screen, self.button_color_border, self.pause_button, border_radius=self.button_radius, width=1)
        pygame.draw.rect(self.screen, self.button_color_border, self.stop_button, border_radius=self.button_radius, width=1)
        pygame.draw.rect(self.screen, self.button_color_border, self.show_logs_button, border_radius=self.button_radius, width=1)
        pygame.draw.rect(self.screen, self.button_color_border, self.dispatch_button, border_radius=self.button_radius, width=1)

        # Draw text on buttons
        self.draw_text("Run", self.run_button)
        self.draw_text("Pause", self.pause_button)
        self.draw_text("Stop", self.stop_button)
        self.draw_text("Print Events", self.show_logs_button)
        self.draw_text("Dispatch", self.dispatch_button)

        # Draw event log box
        pygame.draw.rect(self.screen, (25, 25, 25), self.event_log_box, border_radius=4)
        pygame.draw.rect(self.screen, (100, 100, 100), self.event_log_box, border_radius=4, width=1)
        self.draw_event_log()

        # Draw the text input box
        self.text_input_box.draw(self.screen)

    def draw_text(self, text, button_rect):
        font = pygame.font.Font(None, 22)
        text_surface = font.render(text, True, (255, 255, 255))  # Set text color to white
        text_rect = text_surface.get_rect(center=button_rect.center)

        # Create a new surface with per-pixel alpha for anti-aliasing
        text_with_antialias = pygame.Surface(text_rect.size, pygame.SRCALPHA)
        text_with_antialias.blit(text_surface, (0, 0))

        self.screen.blit(text_with_antialias, text_rect)

    def draw_event_log(self):
        self.event_log.draw_event_log(self.screen, self.event_log_box)