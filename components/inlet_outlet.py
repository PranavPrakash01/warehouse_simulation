# inlet_outlet.py

import pygame
from items import Item

class Inlet:
    def __init__(self, name, row, column):
        self.name = name
        self.row = row
        self.column = column
        self.received_items = []

    def receive_item(self, item):
        self.received_items.append(item)
        print(f"Item received at Inlet {self.name}: {item}")

    def draw_inlet(self, screen, cell_size, start_x, start_y):
        # Draw a green square for the inlet
        pygame.draw.rect(screen, (0, 255, 0), (start_x + self.column * cell_size, start_y + self.row * cell_size, cell_size, cell_size))


class Outlet:
    def __init__(self, name, row, column):
        self.name = name
        self.row = row
        self.column = column

    def dispatch_item(self, item):
        print(f"Item dispatched from Outlet {self.name}: {item}")

    def draw_outlet(self, screen, cell_size, start_x, start_y):
        # Draw a red square for the inlet
        pygame.draw.rect(screen, (255, 0, 0), (start_x + self.column * cell_size, start_y + self.row * cell_size, cell_size, cell_size))
