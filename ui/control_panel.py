# ui/control_panel.py

import pygame
import pygame.gfxdraw  # Import pygame.gfxdraw for drawing rounded rectangles

class ControlPanel:
    def __init__(self, screen, control_panel_frame, simulation):
        self.screen = screen
        self.control_panel_frame = control_panel_frame
        self.button_width = 70
        self.button_height = 30
        self.button_radius = 5  # Radius for rounded corners
        self.simulation = simulation

        # Play button
        self.run_button = pygame.Rect(control_panel_frame.left + 10, control_panel_frame.top + 10, self.button_width, self.button_height)

        # Pause button
        self.pause_button = pygame.Rect(self.run_button.right + 10, self.run_button.top, self.button_width, self.button_height)

        # Stop button
        self.stop_button = pygame.Rect(self.pause_button.right + 10, self.run_button.top, self.button_width, self.button_height)

        # Print all logs
        self.show_logs_button = pygame.Rect(control_panel_frame.left + 10, self.run_button.bottom + 10, self.stop_button.right - self.run_button.left, self.button_height + 5)

        # Decrease the width of the event log box and add padding to the right
        padding_right = 10
        self.event_log_box = pygame.Rect(self.stop_button.right + 10, control_panel_frame.top+10 , control_panel_frame.width - (self.stop_button.right + 10) - padding_right, 80)

        self.event_log_font = pygame.font.Font(None, 20)
        self.event_log = simulation.event_log 

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()

            if self.run_button.collidepoint(mouse_pos):
                self.simulation.run()

            elif self.pause_button.collidepoint(mouse_pos):
                print("Pause button clicked")
                # Add your pause button logic here

            elif self.stop_button.collidepoint(mouse_pos):
                self.simulation.running = False
                self.event_log.add_entry(f"Simulation Stopped: Click Run to restart")

            elif self.show_logs_button.collidepoint(mouse_pos):
                print(self.event_log.all_logs)
                # Add your pause button logic here

    def draw_control_panel(self):
        # Draw buttons with rounded corners
        pygame.draw.rect(self.screen, (50, 50, 50), self.run_button, border_radius=self.button_radius)
        pygame.draw.rect(self.screen, (50, 50, 50), self.pause_button, border_radius=self.button_radius)
        pygame.draw.rect(self.screen, (50, 50, 50), self.stop_button, border_radius=self.button_radius)
        pygame.draw.rect(self.screen, (50, 50, 50), self.show_logs_button, border_radius=self.button_radius)

        # Draw grey borders around the buttons
        pygame.draw.rect(self.screen, (100, 100, 100), self.run_button, border_radius=self.button_radius, width=1)
        pygame.draw.rect(self.screen, (100, 100, 100), self.pause_button, border_radius=self.button_radius, width=1)
        pygame.draw.rect(self.screen, (100, 100, 100), self.stop_button, border_radius=self.button_radius, width=1)
        pygame.draw.rect(self.screen, (100, 100, 100), self.show_logs_button, border_radius=self.button_radius, width=1)

        # Draw text on buttons
        self.draw_text("Run", self.run_button)
        self.draw_text("Pause", self.pause_button)
        self.draw_text("Stop", self.stop_button)
        self.draw_text("Print Events", self.show_logs_button)

        # Draw event log box
        pygame.draw.rect(self.screen, (25, 25, 25), self.event_log_box, border_radius=4)
        pygame.draw.rect(self.screen, (100, 100, 100), self.event_log_box, border_radius=4, width=1)
        self.draw_event_log()

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