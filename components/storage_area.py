# storage_area.py

import pygame
from items import Item
from components.warehouse_layout import warehouse_layout

class StorageArea:
    def __init__(self, name, start_location, item_destination="warehouse", area_type="small"):
        self.name = name
        self.area_type = area_type
        self.item_destination = item_destination
        self.row, self.column = start_location
        self.max_capacity = 10
        self.empty_color = (169, 169, 169)  # Grey color for storage area
        self.non_empty_color = (50, 50, 50)
        self.storage = []

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
        # Draw the cells
        for cell in self.cells:
            row, col = cell
            if self.storage:
                color = self.non_empty_color
            else:
                color = self.empty_color
            pygame.draw.rect(screen, color, (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))

        # Draw the white border around the 2x2 square
        square_size = 2 * cell_size  # Size of the 2x2 square
        border_thickness = 1

        # Calculate starting positions for the borders
        border_start_x = start_x + self.cells[0][1] * cell_size
        border_start_y = start_y + self.cells[0][0] * cell_size

        # Top border
        pygame.draw.rect(screen, (255, 255, 255), (border_start_x, border_start_y, square_size, border_thickness))

        # Bottom border
        pygame.draw.rect(screen, (255, 255, 255), (border_start_x, border_start_y + square_size - border_thickness, square_size, border_thickness))

        # Left border
        pygame.draw.rect(screen, (255, 255, 255), (border_start_x, border_start_y, border_thickness, square_size))

        # Right border
        pygame.draw.rect(screen, (255, 255, 255), (border_start_x + square_size - border_thickness, border_start_y, border_thickness, square_size))
        
    def get_name(self):
        return self.name
    
    def store_item(self, item, event_log):
        # Check if the storage area has reached its maximum capacity
        if len(self.storage) < self.max_capacity:
            # Add the item to the storage list
            self.storage.append(item)

            # Log the item storage
            log_entry = f"[{self.name}]: Stored Item - {item.info()}"
            event_log.add_entry(log_entry)

            return True  # Item successfully stored
        else:
            # Log that the storage area is full
            log_entry = f"[{self.name}]: Storage Area Full - Unable to store Item - {item.info()}"
            event_log.add_entry(log_entry)

            return False  # Storage area full, unable to store item

