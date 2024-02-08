# storage_area.py

import pygame
from items import Item
from components.warehouse_layout import warehouse_layout

class StorageArea:
    def __init__(self, name, start_location, item_destination="warehouse", area_type="small"):
        self.name = name
        self.area_type = area_type
        self.item_location = item_destination
        self.row, self.column = start_location
        self.max_capacity = 10
        self.color = (169, 169, 169)  # Grey color for storage area
        self.storage_list = []

        # Define attributes for big storage area
        if self.area_type == "big":
            self.rows = 2
            self.columns = 2

            # Calculate and add cells based on the starting location
            self.cells = [(start_location[0] + i, start_location[1] + j) for i in range(self.rows) for j in range(self.columns)]

            # Add the big storage area cells to the layout
            for cell in self.cells:
                row, col = cell
                warehouse_layout[row][col] = self.name

    def draw_storage_area(self, screen, cell_size, start_x, start_y):
        for cell in self.cells:
            row, col = cell
            pygame.draw.rect(screen, self.color, (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))

    def store_item(self, item):
        if len(self.storage_list) < self.max_capacity:
            self.storage_list.append(item)
            return True
        else:
            return False
        
    def get_name(self):
        return self.name
