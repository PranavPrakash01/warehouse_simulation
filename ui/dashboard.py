# ui/dashboard.py

import pygame
from ui.display import Display
from ui.control_panel import ControlPanel

class Dashboard:
    def __init__(self, warehouse_layout, inlets, outlets, sorting_areas, storage_areas, conveyors, simulation):
        
        self.warehouse_layout = warehouse_layout
        self.cell_size = 20
        self.padding = 20

        # Set a fixed screen size
        self.screen_size = (1000, 565)  # Adjust the size as needed
        self.screen = pygame.display.set_mode(self.screen_size)

        # Set the window title and icon (if available)
        pygame.display.set_caption("Digital WareHouse V.1.0")

        # Initialize main frame
        self.main_frame = pygame.Rect(0, 0, self.screen_size[0], self.screen_size[1])

        # Initialize display frame at the top of the main frame
        self.display_frame = pygame.Rect(self.padding, self.padding, self.screen_size[0] - 2 * self.padding, self.screen_size[1] - 2 * self.padding)
        self.display = Display(self.screen, self.warehouse_layout, self.cell_size, self.display_frame, inlets, outlets, sorting_areas, storage_areas, conveyors)

        # Padding between display frame and control panel frame
        padding_between_frames = 20

        # Initialize control panel frame at the bottom of the main frame with full width
        self.control_panel_height = 100
        self.control_panel_frame = pygame.Rect(0, self.display_frame.bottom + padding_between_frames, self.screen_size[0], self.control_panel_height)

        # Adjust the screen size to consider the height of the control panel
        self.screen_size = (self.screen_size[0], self.main_frame.height + self.control_panel_frame.height)
        self.screen = pygame.display.set_mode(self.screen_size)

        # Initialize control panel
        self.control_panel = ControlPanel(self.screen, self.control_panel_frame, simulation)

    def run(self):

        self.draw_dashboard_layout()

        pygame.display.flip()
            

    def draw_dashboard_layout(self):
        pygame.draw.rect(self.screen, (25, 25, 25), self.main_frame)  # Draw main frame
        pygame.draw.rect(self.screen, (0, 0, 0), self.display_frame)  # Clear display frame with a black background
        self.display.draw_warehouse_layout()

        # Draw control panel frame
        pygame.draw.rect(self.screen, (50, 50, 50), self.control_panel_frame)

        # Draw control panel
        self.control_panel.draw_control_panel()
