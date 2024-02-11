# inlet_outlet.py

import pygame
from items import Item
import time

class Inlet:
    def __init__(self, name, row, column):
        self.name = name
        self.row = row
        self.column = column
        self.conveyor = None 
        self.received_items = []
        self.color = (139, 204, 137)  # Original color
        self.color_timer = 0
        self.color_duration = 250  # Time duration in milliseconds for the color change

    def receive_item(self, item, event_log):
        
        self.received_items.append(item)

        # Change color to green temporarily
        self.color = (0, 255, 0)
        self.color_timer = pygame.time.get_ticks() + self.color_duration

        item_info = f"[{self.name}]: New Item Received - {item.info()}"
        event_log.add_entry(item_info)

        # Check if the Inlet has a connected Conveyor
        if self.conveyor:
            self.conveyor.transport_item(item, event_log)


    def draw_inlet(self, screen, cell_size, start_x, start_y):
        # Draw the inlet with the current color
        pygame.draw.rect(screen, self.color, (start_x + self.column * cell_size, start_y + self.row * cell_size, cell_size, cell_size))

        # Check if the color change duration has passed
        if pygame.time.get_ticks() > self.color_timer:
            # Change color back to the original color
            self.color = (139, 204, 137)

    def get_name(self):
        return self.name

class Outlet:
    def __init__(self, name, row, column):
        self.name = name
        self.row = row
        self.column = column
        self.received_items = []
        self.color = (217, 122, 115)
        self.color_timer = 0
        self.color_duration = 250 

    def dispatch_item(self, item, event_log):

        self.received_items.append(item)

        # Change color to green temporarily
        self.color = (255, 0, 0)
        self.color_timer = pygame.time.get_ticks() + self.color_duration

        item_info = f"[{self.name}]: Item Dispatched - {item.info()}"
        event_log.add_entry(item_info)

    def draw_outlet(self, screen, cell_size, start_x, start_y):
        # Draw a red square for the inlet
        pygame.draw.rect(screen, (217, 122, 115), (start_x + self.column * cell_size, start_y + self.row * cell_size, cell_size, cell_size))

        # Check if the color change duration has passed
        if pygame.time.get_ticks() > self.color_timer:
            # Change color back to the original color
            self.color = (217, 122, 115)

    def get_name(self):
        return self.name