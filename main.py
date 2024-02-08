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
    inlet1 = Inlet(name="Inlet1", row=7, column=1)
    inlet2 = Inlet(name="Inlet2", row=10, column=1)
    inlet3 = Inlet(name="Inlet3", row=13, column=1)
    
    outlet1 = Outlet(name="Outlet1", row=23, column=14)
    outlet2 = Outlet(name="Outlet2", row=23, column=17)
    outlet3 = Outlet(name="Outlet3", row=23, column=20)

    conveyor = Conveyor(name="Conveyor1")
    sorting_area = SortingArea(name="SortingArea1")
    storage_area = StorageArea(name="StorageArea1", max_capacity=5)
    event_log = EventLog()
    warehouse_layout_data = warehouse_layout
    inlets = [inlet1, inlet2, inlet3]
    outlets = [outlet1, outlet2, outlet3]
    dashboard = Dashboard(warehouse_layout_data, inlets, outlets)  # Pass the inlets and outlets to the Dashboard

    # Place Inlets in the layout
    warehouse_layout_data[inlet1.row][inlet1.column] = "I"
    warehouse_layout_data[inlet2.row][inlet2.column] = "I"
    warehouse_layout_data[inlet3.row][inlet3.column] = "I"

    # Place Outlets in the layout
    warehouse_layout_data[outlet1.row][outlet1.column] = "O"
    warehouse_layout_data[outlet2.row][outlet2.column] = "O"
    warehouse_layout_data[outlet3.row][outlet3.column] = "O"

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
