# ui/control_panel.py

import pygame
import pygame.gfxdraw  
from ui.text_input_box import InputBox
from ui.button_type1 import ButtonType1

class ControlPanel:
    def __init__(self, screen, control_panel_frame, simulation):
        self.screen = screen
        self.control_panel_frame = control_panel_frame
        self.button_width = 70
        self.button_height = 30
        self.simulation = simulation
        self.event_log = simulation.event_log 

        # Create instances of ButtonType1 for different buttons
        self.run_button = ButtonType1(self.screen, "Run", pygame.Rect(control_panel_frame.left + 10, control_panel_frame.top + 10, self.button_width, self.button_height), self.simulation.run)
        self.pause_button = ButtonType1(self.screen, "Pause", pygame.Rect(self.run_button.rect.right + 10, self.run_button.rect.top, self.button_width, self.button_height))
        self.stop_button = ButtonType1(self.screen, "Stop", pygame.Rect(self.pause_button.rect.right + 10, self.run_button.rect.top, self.button_width, self.button_height), self.simulation.stop)
        self.show_logs_button = ButtonType1(self.screen, "Print Events", pygame.Rect(control_panel_frame.left + 10, self.run_button.rect.bottom + 10, self.stop_button.rect.right - self.run_button.rect.left, self.button_height + 5), self.event_log.print_all_logs)

        # Decrease the width of the event log box and add padding to the right
        self.event_log_box = pygame.Rect(self.stop_button.rect.right + 10, control_panel_frame.top + 10, control_panel_frame.width // 2 + 75, 80)

        # Create an instance of InputBox for the text input
        self.text_input_box = InputBox(self.event_log_box.right + 10, control_panel_frame.top + 10, 155, 32, placeholder="Enter Dispatch Loc")

        # Dispatch button
        self.dispatch_button = ButtonType1(self.screen, "Dispatch", pygame.Rect(self.event_log_box.right + 10, self.text_input_box.rect.bottom + 10, 155, self.button_height + 5), self.text_input_box.get_text)

    def handle_events(self, event):
        # Handle events for buttons
        self.run_button.handle_event(event)
        self.pause_button.handle_event(event)
        self.stop_button.handle_event(event)
        self.show_logs_button.handle_event(event)
        self.dispatch_button.handle_event(event)

        # Handle events for the text input box
        self.text_input_box.handle_event(event)

    def draw_control_panel(self):
        # Draw buttons
        self.run_button.draw()
        self.pause_button.draw()
        self.stop_button.draw()
        self.show_logs_button.draw()
        self.dispatch_button.draw()

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