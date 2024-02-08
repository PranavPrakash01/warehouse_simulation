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
    inlets = [inlet1, inlet2, inlet3]
    
    outlet1 = Outlet(name="Outlet1", row=23, column=16)
    outlet2 = Outlet(name="Outlet2", row=23, column=19)
    outlet3 = Outlet(name="Outlet3", row=23, column=22)
    outlets = [outlet1, outlet2, outlet3]

    conveyor1 = Conveyor(name="Conveyor1", start_location=(7, 2))
    conveyor2 = Conveyor(name="Conveyor2", start_location=(10, 2))
    conveyor3 = Conveyor(name="Conveyor3", start_location=(13, 2))
    conveyors = [conveyor1, conveyor2, conveyor3]

    # Create a big sorting area
    big_sorting_area = SortingArea(name="BigSortingArea", start_location=(10, 15), area_type="big")

    # Create a list of sorting areas
    sorting_areas = [big_sorting_area]

    #create big storage areas
    storage_area1 = StorageArea(name="StorageArea1", start_location=(4, 10), item_destination="A", area_type="big")
    storage_area2 = StorageArea(name="StorageArea2", start_location=(4, 12), item_destination="B", area_type="big")
    storage_area3 = StorageArea(name="StorageArea3", start_location=(4, 14), item_destination="C", area_type="big")
    storage_area4 = StorageArea(name="StorageArea4", start_location=(4, 16), item_destination="D", area_type="big")
    storage_area5 = StorageArea(name="StorageArea5", start_location=(6, 10), item_destination="E", area_type="big")
    storage_area6 = StorageArea(name="StorageArea6", start_location=(6, 12), item_destination="F", area_type="big")
    storage_area7 = StorageArea(name="StorageArea7", start_location=(6, 14), item_destination="G", area_type="big")
    storage_area8 = StorageArea(name="StorageArea8", start_location=(6, 16), item_destination="H", area_type="big")

    storage_area9 = StorageArea(name="StorageArea9", start_location=(15, 10), item_destination="I", area_type="big")
    storage_area10 = StorageArea(name="StorageArea10", start_location=(15, 12), item_destination="J", area_type="big")
    storage_area11 = StorageArea(name="StorageArea11", start_location=(15, 14), item_destination="K", area_type="big")
    storage_area12 = StorageArea(name="StorageArea12", start_location=(15, 16), item_destination="L", area_type="big")
    storage_area13 = StorageArea(name="StorageArea13", start_location=(17, 10), item_destination="M", area_type="big")
    storage_area14 = StorageArea(name="StorageArea14", start_location=(17, 12), item_destination="N", area_type="big")
    storage_area15 = StorageArea(name="StorageArea15", start_location=(17, 14), item_destination="O", area_type="big")
    storage_area16 = StorageArea(name="StorageArea16", start_location=(17, 16), item_destination="P", area_type="big")

    # Create a list of Sortign areas
    storage_areas = [
        storage_area1, storage_area2, storage_area3, storage_area4, storage_area5, storage_area6, storage_area7, storage_area8,
        storage_area9, storage_area10, storage_area11, storage_area12, storage_area13, storage_area14, storage_area15, storage_area16
        ]

    event_log = EventLog()
    warehouse_layout_data = warehouse_layout

    dashboard = Dashboard(warehouse_layout_data, inlets, outlets, sorting_areas, storage_areas, conveyors)  # Pass the inlets, outlets, sorting areas, and storage areas to the Dashboard

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
