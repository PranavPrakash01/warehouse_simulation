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

        # Calculate and add cells based on the starting location
        self.cells = [(start_location[0], start_location[1] + i) for i in range(self.length)]

        # Add the conveyor cells to the layout
        for cell in self.cells:
            row, col = cell
            warehouse_layout[row][col] = self.name

    def draw_conveyor(self, screen, cell_size, start_x, start_y):
        for cell in self.cells:
            row, col = cell
            pygame.draw.rect(screen, (217, 217, 217), (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))

    def transport_item(self, item):
        self.items_on_conveyor.append(item)
        print(f"Item transported on Conveyor {self.name}: {item}")

    def get_name(self):
        return self.name
