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
        self.sorted_items = {}
        #self.color_timer = 0
        self.receiving_color_timer = 0
        self.sorting_color_timer = 0
        self.color_duration = 500
        self.sort_color_duration = 300
        
        # Color variables
        self.color_original = (126, 155, 222) 
        self.color_transporting = (0, 136, 255)
        self.color_sorting = (255, 0, 0)

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

    def get_name(self):
        return self.name
    
    def draw_sorting_area(self, screen, cell_size, start_x, start_y):
        for cell in self.cells:
            row, col = cell

            # Determine the color based on the current state
            if self.receiving_color_timer != 0:
                color = self.color_transporting  # Blue for receiving
            elif self.sorting_color_timer != 0:
                color = self.color_sorting  # Red during sorting
            else:
                color = self.color_original  # Original color

            pygame.draw.rect(screen, color, (start_x + col * cell_size, start_y + row * cell_size, cell_size, cell_size))

            # Check if the color change duration for receiving has passed
            if pygame.time.get_ticks() >  self.receiving_color_timer:
                self.receiving_color_timer = 0

            # Check if the color change duration for sorting has passed
            if pygame.time.get_ticks() > self.sorting_color_timer:
                self.sorting_color_timer = 0

    def receive_unsorted_items(self, items, event_log, conveyor_name):
        for item in items:
            self.unsorted_items.append(item)
        
        # Change color to blue temporarily
        self.receiving_color_timer = pygame.time.get_ticks() + self.color_duration

        item_info = f"[{self.name}]: Recieved {len(items)} Items from {conveyor_name}"
        
        event_log.add_entry(item_info)

    def sort_items(self):

        if self.unsorted_items:
            item = self.unsorted_items.pop()
            location = item.location

            if location not in self.sorted_items:
                self.sorted_items[location] = []
            self.sorted_items[location].append(item)

            # Change color to red temporarily
            self.sorting_color_timer = pygame.time.get_ticks() + self.sort_color_duration
            return False
        else:
            # Clear the unsorted items after sorting
            self.unsorted_items.clear()
            #self.print_sorted_items()
            return True

    def print_sorted_items(self):
        for location, items in self.sorted_items.items():
            print(f"Location: {location}")
            for item in items:
                print(f"  {item.serial_id} {item.name} {item.location} {item.weight}")

    def log_status(self, event_log):
        if not self.unsorted_items:
            log_entry = f"[{self.name}]: Sorting Completed"
            event_log.add_entry(log_entry)
            return

        log_entry = f"[{self.name}]: Sorting Items..."
        if event_log.log_entries[0] != log_entry:
            event_log.add_entry(log_entry)