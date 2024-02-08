# main.py

from components.inlet_outlet import Inlet, Outlet
from components.conveyor import Conveyor
from components.sorting_area import SortingArea
from components.storage_area import StorageArea
from ui.dashboard import Dashboard
from ui.event_log import EventLog
from items import Item
from components.warehouse_layout import warehouse_layout
import pygame

def main():
    # Initialize components

    # Inlets
    inlet1 = Inlet(name="Inlet1", row=7, column=1)
    inlet2 = Inlet(name="Inlet2", row=10, column=1)
    inlet3 = Inlet(name="Inlet3", row=13, column=1)
    inlets = [inlet1, inlet2, inlet3]

    outlet1 = Outlet(name="Outlet1")
    conveyor = Conveyor(name="Conveyor1")
    sorting_area = SortingArea(name="SortingArea1")
    storage_area = StorageArea(name="StorageArea1", max_capacity=5)
    event_log = EventLog()
    warehouse_layout_data = warehouse_layout
    
    dashboard = Dashboard(warehouse_layout_data, inlets)  # Pass the inlets to the Dashboard

    # Place Inlets in the layout
    warehouse_layout_data[inlet1.row][inlet1.column] = "I"  # Inlet 1
    warehouse_layout_data[inlet2.row][inlet2.column] = "I"  # Inlet 2
    warehouse_layout_data[inlet3.row][inlet3.column] = "I"  # Inlet 3

    # Main simulation loop
    running = True
    while running:
        # Display warehouse layout and simulation controls
        dashboard.run()

        # Handle user events (button clicks, etc.) directly in the GUI
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        # You can add any additional logic here based on GUI events

        # Display event log
        dashboard.display_event_log(event_log)

    pygame.quit()

if __name__ == "__main__":
    main()
