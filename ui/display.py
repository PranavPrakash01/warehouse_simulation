# ui/display.py

import pygame

class Display:
    def __init__(self, screen, warehouse_layout, cell_size, display_frame, inlets, outlets, sorting_areas):
        self.screen = screen
        self.warehouse_layout = warehouse_layout
        self.cell_size = cell_size
        self.display_frame = display_frame  # Pass the display frame to the Display class
        self.inlets = inlets  # Pass the inlets to the Display class
        self.outlets = outlets  # Pass the outlets to the Display class
        self.sorting_areas = sorting_areas  # Pass the sorting areas to the Display class

    def draw_warehouse_layout(self):
        # Calculate the starting position to center the layout
        start_x = self.display_frame.left + (self.display_frame.width - len(self.warehouse_layout[0]) * self.cell_size) // 2
        start_y = self.display_frame.top + (self.display_frame.height - len(self.warehouse_layout) * self.cell_size) // 2

        for row_idx, row in enumerate(self.warehouse_layout):
            for col_idx, cell in enumerate(row):
                color = (255, 255, 255)  # Default color for empty cells (light blue)

                if cell == "#":
                    color = (173, 216, 230)  # Wall color (light blue)

                # Adjust the position by adding the starting position
                pygame.draw.rect(self.screen, color, (start_x + col_idx * self.cell_size, start_y + row_idx * self.cell_size, self.cell_size, self.cell_size))

        # Draw inlets
        for inlet in self.inlets:
            inlet.draw_inlet(self.screen, self.cell_size, start_x, start_y)

        # Draw outlets
        for outlet in self.outlets:
            outlet.draw_outlet(self.screen, self.cell_size, start_x, start_y)

        # Draw Sorting areas
        for sorting_area in self.sorting_areas:
            sorting_area.draw_sorting_area(self.screen, self.cell_size, start_x, start_y)
