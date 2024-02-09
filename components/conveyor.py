# conveyor.py

import pygame
from items import Item
from components.warehouse_layout import warehouse_layout

class Conveyor:
    def __init__(self, name, start_location):
        self.name = name
        self.row, self.column = start_location
        self.items_on_conveyor = []
        self.length = 3
        self.color_timer = 0
        self.color_duration = 500

        # Color variables
        self.color_original = (217, 217, 217)  # Light grey color
        self.color_transporting = (169, 169, 169)  # Grey color for transporting items

        # Calculate and add cells based on the starting location
        self.cells = [(start_location[0], start_location[1] + i) for i in range(self.length)]

        # Add the conveyor cells to the layout
        for cell in self.cells:
            row, col = cell
            warehouse_layout[row][col] = self.name

    def draw_conveyor(self, screen, cell_size, start_x, start_y):
        for cell in self.cells:
            row, col = cell
            color = self.color_transporting if self.color_timer != 0 else self.color_original
            pygame.draw.rect(screen, color, (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))

            # Check if the color change duration has passed
            if pygame.time.get_ticks() > self.color_timer:
                # Change color back to the original color
                self.color_timer = 0

    def transport_item(self, item, event_log):
        self.items_on_conveyor.append(item)
        
        # Change color to grey temporarily
        self.color_timer = pygame.time.get_ticks() + self.color_duration

        item_info = f"[{self.name}]: Transporting Item - {item.info()}"
        
        event_log.add_entry(item_info)

    def get_name(self):
        return self.name
