# simulation_logic.py
from ui.event_log import EventLog
from items import Item  
import csv
import random

class Simulation:
    def __init__(self, inlets, outlets, sorting_areas, storage_areas, conveyors):

        self.inlets = inlets
        self.outlets = outlets
        self.sorting_areas = sorting_areas
        self.storage_areas = storage_areas
        self.conveyors = conveyors

        self.event_log = EventLog()
        self.input_items = [] 
        self.running = False
        self.inlets_active = False
        self.conveyor_active = False
        self.big_sorting_active = False
        self.big_storage_active = False
        self.outlets_active = False
        self.dispatch_items = []

    def read_and_convert_csv(self, filename='items_data.csv'):
        try:
            with open(filename, 'r') as file:
                csv_reader = csv.DictReader(file)

                length = 0
                for row in csv_reader:
                    serial_id = int(row['serial_id'])
                    item = Item(
                        serial_id=serial_id,
                        name=row[' name'].strip(),
                        weight=int(row[' weight']),
                        location=row[' location'].strip()
                    )
                    self.input_items.append(item)
                    length += 1

                self.event_log.add_entry(f"{length} Items Received")

        except FileNotFoundError:
            log_entry = f"Error: File '{filename}' not found."
            self.event_log.add_entry(log_entry)

    def run(self):
        self.running = True
        log_entry = "Running simulation..."
        self.event_log.add_entry(log_entry)

        self.read_and_convert_csv()

        self.inlets_active = True

    def pause(self):
        self.input_items = [] 
        self.running = False
        self.inlets_active = False
        self.conveyor_active = False
        self.event_log.add_entry(f"Simulation Paused: Click Again to Continue")

    def reset(self):
        self.input_items = [] 
        self.running = False
        self.inlets_active = False
        self.conveyor_active = False
        self.event_log.clear_log_box()
        self.event_log.all_logs.clear()
        for storage_area in self.storage_areas:
            storage_area.storage.clear()
        self.event_log.add_entry(f"Simulation Reset: Click Run to restart")

    def stop(self):
        self.input_items = [] 
        self.running = False
        self.inlets_active = False
        self.conveyor_active = False
        self.event_log.add_entry(f"Simulation Completed: Click Run Restart")


    def pass_items_inlet(self):
        
        # Check if there are items to distribute
        if self.input_items:
            # Choose a random inlet
            random_inlet = random.choice(self.inlets)

            # Receive one item from the input_items list
            item = self.input_items.pop(0)

            # Pass the item to the random inlet
            random_inlet.receive_item(item, self.event_log)

        else:
            log_entry = "All Items Received at Inlet"
            
            if self.inlets_active:
                self.inlets_active = False
                self.conveyor_active = True
                self.event_log.add_entry(log_entry)

    def send_items_to_sorting_area(self):
        for conveyor in self.conveyors:
            items_on_conveyor = conveyor.items_on_conveyor.copy()

            if items_on_conveyor:
                # Pass items from conveyor to big_sorting_area
                self.sorting_areas[0].receive_unsorted_items(items_on_conveyor, self.event_log, conveyor.name)
                
                # Clear items on the conveyor after passing to big_sorting_area
                conveyor.items_on_conveyor.clear()

                # Return after processing the first conveyor with items
                return

        # If no conveyors have items, log appropriate message
        log_entry = "All Items Transported to Big Sorting Area"
        if self.conveyor_active:
            self.event_log.add_entry(log_entry)
            self.conveyor_active = False
            self.big_sorting_active = True
            #self.stop()

    def big_sorting_area_sort(self):
        is_done = self.sorting_areas[0].sort_items()
        
        if is_done:
            self.big_sorting_active = False
            self.big_storage_active = True
        else:
            self.sorting_areas[0].log_status(self.event_log)

    def send_items_to_storage_area(self):
        sorted_items = self.sorting_areas[0].sorted_items.copy()

        for location, items in sorted_items.items():
            # Find the corresponding storage area for the location
            storage_area = next((area for area in self.storage_areas if area.item_destination == location), None)

            if storage_area:
                # Store items in the storage area
                for item in items:
                    storage_area.store_item(item, self.event_log)

                # Clear the sorted items from the sorting area
                self.sorting_areas[0].sorted_items.pop(location)

                log_entry = f"{len(items)} items sent to {storage_area.get_name()} from Sorting Area"
                self.event_log.add_entry(log_entry)

                return 

        # Check if all items are sorted and stored
        if not self.sorting_areas[0].sorted_items:
            self.big_storage_active = False
            self.stop()

    def get_items_in_storage(self, location):
        # Find the corresponding storage area for the location
        storage_area = next((area for area in self.storage_areas if area.item_destination == location), None)

        if storage_area:
            log_entry = f"Found Storage Area: {storage_area.name} With Location: {location}"
            self.event_log.add_entry(log_entry)
            if storage_area.storage:

                log_entry = f"[{storage_area.name}] Total Items: {len(storage_area.storage)}"
                self.event_log.add_entry(log_entry)

                storage_area.storage.clear()

            else:
                log_entry = f"[{storage_area.name}] No Items To Dispatch"
                self.event_log.add_entry(log_entry)

        else:
            log_entry = "No matching storage area found."
            self.event_log.add_entry(log_entry)