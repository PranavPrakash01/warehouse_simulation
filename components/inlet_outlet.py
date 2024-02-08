# inlet_outlet.py

import pygame
from items import Item

class Inlet:
    def __init__(self, name, row, column):
        self.name = name
        self.row = row
        self.column = column
        self.conveyor = None 
        self.received_items = []

    def receive_item(self, item_data, event_log):
        self.received_items.append(item_data)
        item_info = f"[{self.name}] : New Item Received - name: '{item_data['name']}', weight: {item_data['weight']}, location: '{item_data['location']}'"
        event_log.add_entry(item_info)

    def draw_inlet(self, screen, cell_size, start_x, start_y):
        # Draw a green square for the inlet
        pygame.draw.rect(screen, (139, 204, 137), (start_x + self.column * cell_size, start_y + self.row * cell_size, cell_size, cell_size))

    def get_name(self):
        return self.name

class Outlet:
    def __init__(self, name, row, column):
        self.name = name
        self.row = row
        self.column = column

    def dispatch_item(self, item):
        print(f"Item dispatched from Outlet {self.name}: {item}")

    def draw_outlet(self, screen, cell_size, start_x, start_y):
        # Draw a red square for the inlet
        pygame.draw.rect(screen, (217, 122, 115), (start_x + self.column * cell_size, start_y + self.row * cell_size, cell_size, cell_size))

    def get_name(self):
        return self.name