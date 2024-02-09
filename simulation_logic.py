# simulation_logic.py
from ui.event_log import EventLog
from items import Item  
import csv
import random

class Simulation:
    def __init__(self):
        self.event_log = EventLog()
        self.input_items = [] 
        self.running = False
        self.inlets_active = False
        self.conveyor_active = False

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

    def stop(self):
        self.input_items = [] 
        self.running = False
        self.inlets_active = False
        self.conveyor_active = False
        self.event_log.add_entry(f"Simulation Stopped/Completed: Click Run to restart")

    def pass_items_inlet(self, inlets):
        self.inlets_active = True
        # Check if there are items to distribute
        if self.input_items:
            # Choose a random inlet
            random_inlet = random.choice(inlets)

            # Receive one item from the input_items list
            item = self.input_items.pop(0)

            # Pass the item to the random inlet
            random_inlet.receive_item(item, self.event_log)

        else:
            log_entry = "All Items Received at Inlet"
            
            if self.inlets_active:
                self.inlets_active = False
                self.conveyor_active = True
            else:
                self.event_log.add_entry(log_entry)

    def send_items_to_sorting_area(self, conveyors, big_sorting_area):
        for conveyor in conveyors:
            items_on_conveyor = conveyor.items_on_conveyor.copy()

            if items_on_conveyor:
                # Pass items from conveyor to big_sorting_area
                big_sorting_area.receive_unsorted_items(items_on_conveyor, self.event_log, conveyor.name)
                
                # Clear items on the conveyor after passing to big_sorting_area
                conveyor.items_on_conveyor.clear()

                # Return after processing the first conveyor with items
                return

        # If no conveyors have items, log appropriate message
        log_entry = "All Items Transported to Big Sorting Area"
        if self.conveyor_active:
            self.conveyor_active = False
            self.stop()
        else:
            self.event_log.add_entry(log_entry)

        