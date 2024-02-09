# sorting_area.py
import pygame
from items import Item
from components.warehouse_layout import warehouse_layout

class SortingArea:
    def __init__(self, name, start_location, area_type="small"):
        self.name = name
        self.area_type = area_type
        self.row, self.column = start_location
        self.unsorted_items = []
        self.color_timer = 0
        self.color_duration = 500

        # Color variables
        self.color_original = (126, 155, 222) 
        self.color_transporting = (0, 136, 255)

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
            color = self.color_transporting if self.color_timer != 0 else self.color_original
            pygame.draw.rect(screen, color , (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))

            # Check if the color change duration has passed
            if pygame.time.get_ticks() > self.color_timer:
                # Change color back to the original color
                self.color_timer = 0
        
    def receive_unsorted_items(self, items, event_log, conveyor_name):
        for item in items:
            self.unsorted_items.append(item)
        
        # Change color to grey temporarily
        self.color_timer = pygame.time.get_ticks() + self.color_duration

        item_info = f"[{self.name}]: Recieved {len(items)} Items from {conveyor_name}"
        
        event_log.add_entry(item_info)

    def get_name(self):
        return self.name

