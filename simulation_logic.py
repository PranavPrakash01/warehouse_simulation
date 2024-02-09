# simulation_logic.py
from ui.event_log import EventLog
import csv
import random
import pygame.time

class Simulation:
    def __init__(self, inlets):
        self.inlets = inlets
        self.event_log = EventLog()
        self.input_items = {}
        self.running = False

    def read_and_convert_csv(self, filename='items_data.csv'):
        try:
            with open(filename, 'r') as file:
                csv_reader = csv.DictReader(file)
                
                # Print field names for debugging
                print(f"CSV Field Names: {csv_reader.fieldnames}")
                
                for row in csv_reader:
                    serial_id = int(row['serial_id'])
                    item_data = {
                        'name': row[' name'].strip(),  
                        'weight': int(row[' weight']),
                        'location': row[' location'].strip() 
                    }
                    self.input_items[serial_id] = item_data

        except FileNotFoundError:
            log_entry = f"Error: File '{filename}' not found."
            self.event_log.add_entry(log_entry)
        print(self.input_items)

    def run(self):
        self.running = True
        log_entry = "Running simulation..."
        self.event_log.add_entry(log_entry)


        self.read_and_convert_csv()

    def pass_items_inlet(self):
        # Check if there are items to distribute
        if self.input_items:
            # Get the first item in the input_items dictionary
            serial_id, item_data = next(iter(self.input_items.items()))

            # Choose a random inlet
            random_inlet = random.choice(self.inlets)

            # Receive the first item in the random inlet
            random_inlet.receive_item(item_data, self.event_log)

            # Remove the processed item from the input_items dictionary
            del self.input_items[serial_id]
        else:
            log_entry = "No items to distribute."

            if self.event_log.log_entries and self.event_log.log_entries[0] == log_entry:
                pass
            else:
                self.event_log.add_entry(log_entry)
