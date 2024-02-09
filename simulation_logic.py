# simulation_logic.py
from ui.event_log import EventLog
from items import Item  
import csv
import random

class Simulation:
    def __init__(self, inlets):
        self.inlets = inlets
        self.event_log = EventLog()
        self.input_items = [] 
        self.running = False

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
            log_entry = "All Items Received"

            if self.event_log.log_entries and self.event_log.log_entries[0] == log_entry:
                pass
            else:
                self.event_log.add_entry(log_entry)
