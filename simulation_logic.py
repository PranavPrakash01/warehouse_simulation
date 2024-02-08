# simulation_logic.py
from ui.event_log import EventLog

class Simulation:
    def __init__(self):
        self.event_log = EventLog()  # Create an instance of EventLog

    def run(self):
        log_entry = "Running simulation..."
        self.event_log.add_entry(log_entry)  # Add log entry to EventLog
