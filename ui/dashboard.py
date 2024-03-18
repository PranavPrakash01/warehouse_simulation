# ui/dashboard.py

import pygame
from ui.display import Display
from ui.control_panel import ControlPanel
from ui.sidebar_panel import SidebarPanel

class Dashboard:
    def __init__(self, warehouse_layout, inlets, outlets, sorting_areas, storage_areas, conveyors, simulation):
        
        self.warehouse_layout = warehouse_layout
        self.cell_size = 20
        self.padding = 20
        self.sidebar_width = 220
        self.control_panel_height = 140
        self.display_width = 1000
        self.display_height = 565

        # Set a fixed screen size for the main display area
        
        self.screen_size = (self.display_width  + self.sidebar_width, self.display_height + self.control_panel_height)  # Adjust the size as needed
        self.screen = pygame.display.set_mode(self.screen_size)

        # Set the window title and icon (if available)
        pygame.display.set_caption("Digital WareHouse V.1.0")

        # Initialize main frame
        self.main_frame = pygame.Rect(0, 0, self.screen_size[0], self.screen_size[1])

        # Initialize display frame at the top of the main frame
        self.display_frame = pygame.Rect(self.padding, self.padding, self.display_width - 2 * self.padding, self.display_height - 2 * self.padding)
        self.display = Display(self.screen, self.warehouse_layout, self.cell_size, self.display_frame, inlets, outlets, sorting_areas, storage_areas, conveyors)

        # Padding between display frame and control panel frame
        padding_between_frames = 20

        # Initialize control panel frame at the bottom of the main frame with full width
        self.control_panel_frame = pygame.Rect(0, self.display_frame.bottom + padding_between_frames, self.display_width, self.control_panel_height)

        # Initialize control panel
        self.control_panel = ControlPanel(self.screen, self.control_panel_frame, simulation)

        # Initialize sidebar panel frame on the right side of the main frame
        self.sidebar_panel_frame = pygame.Rect(self.display_frame.right + self.padding, self.main_frame.top, self.sidebar_width, self.main_frame.height+self.control_panel_frame.height)

        # Initialize sidebar panel
        self.sidebar_panel = SidebarPanel(self.screen, self.sidebar_panel_frame)

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

        # Draw sidebar panel
        pygame.draw.rect(self.screen, (35, 35, 35), self.sidebar_panel_frame)
        self.sidebar_panel.draw_sidebar_panel()