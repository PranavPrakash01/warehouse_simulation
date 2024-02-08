# sorting_area.py
import pygame
from items import Item
from components.warehouse_layout import warehouse_layout

class SortingArea:
    def __init__(self, name, start_location, area_type="small"):
        self.name = name
        self.area_type = area_type
        self.row, self.column = start_location
        self.sorted_items = []

        # Define attributes for big sorting area
        if self.area_type == "big":
            self.rows = 3
            self.columns = 3

            # Calculate and add cells based on the starting location
            self.cells = [(start_location[0] + i, start_location[1] + j) for i in range(self.rows) for j in range(self.columns)]

            # Add the big sorting area cells to the layout
            for cell in self.cells:
                row, col = cell
                warehouse_layout[row][col] = "BSA"
    
    def draw_sorting_area(self, screen, cell_size, start_x, start_y):
        for cell in self.cells:
            row, col = cell
            pygame.draw.rect(screen, (62, 73, 199) , (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))
        
    def sort_items(self, items):
        # Implement sorting logic here based on criteria
        # For example, sorting by location
        self.sorted_items = sorted(items, key=lambda x: x.location)
        print(f"Items sorted in Sorting Area {self.name}: {self.sorted_items}")

    def get_name(self):
        return self.name

