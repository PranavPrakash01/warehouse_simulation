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
    
    outlet1 = Outlet(name="Outlet1", row=23, column=14)
    outlet2 = Outlet(name="Outlet2", row=23, column=17)
    outlet3 = Outlet(name="Outlet3", row=23, column=20)
    outlets = [outlet1, outlet2, outlet3]

    conveyor = Conveyor(name="Conveyor1")

    # Create a big sorting area
    big_sorting_area = SortingArea(name="BigSortingArea", start_location=(10, 10), area_type="big")

    # Create a list of sorting areas
    sorting_areas = [big_sorting_area]

    #create big storage areas
    storage_area1 = StorageArea(name="StorageArea1", start_location=(5, 10), item_destination="A", area_type="big")
    storage_area2 = StorageArea(name="StorageArea2", start_location=(5, 12), item_destination="B", area_type="big")
    storage_area3 = StorageArea(name="StorageArea3", start_location=(5, 14), item_destination="C", area_type="big")
    storage_area4 = StorageArea(name="StorageArea4", start_location=(5, 16), item_destination="D", area_type="big")
    storage_area5 = StorageArea(name="StorageArea5", start_location=(7, 10), item_destination="E", area_type="big")
    storage_area6 = StorageArea(name="StorageArea6", start_location=(7, 12), item_destination="F", area_type="big")
    storage_area7 = StorageArea(name="StorageArea7", start_location=(7, 14), item_destination="G", area_type="big")
    storage_area8 = StorageArea(name="StorageArea8", start_location=(7, 16), item_destination="H", area_type="big")

    # Create a list of Sortign areas
    storage_areas = [storage_area1, storage_area2, storage_area3, storage_area4, storage_area5, storage_area6, storage_area7, storage_area8]

    event_log = EventLog()
    warehouse_layout_data = warehouse_layout

    dashboard = Dashboard(warehouse_layout_data, inlets, outlets, sorting_areas, storage_areas)  # Pass the inlets, outlets, sorting areas, and storage areas to the Dashboard

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
