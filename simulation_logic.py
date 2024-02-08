# simulation_logic.py
from ui.event_log import EventLog
import csv

class Simulation:
    def __init__(self):
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
        log_entry = "Running simulation..."
        self.event_log.add_entry(log_entry)

        # Trigger the function to read and convert the CSV file
        self.read_and_convert_csv()
