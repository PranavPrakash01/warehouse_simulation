# event_log.py

class EventLog:
    def __init__(self):
        """
        Initialize an EventLog object.
        """
        self.events = []

    def log_item_arrival(self, item):
        """
        Log an item arrival event.

        Parameters:
        - item (Item): The item that arrived.
        """
        self.events.append(f"Item Arrival: {item}")

    def log_sorting_action(self, area, sorted_items):
        """
        Log a sorting action event.

        Parameters:
        - area (str): The area where sorting occurred.
        - sorted_items (list): The items that were sorted.
        """
        self.events.append(f"Sorting Action in {area}: {sorted_items}")

    def log_storage_change(self, area, action, item):
        """
        Log a storage change event.

        Parameters:
        - area (str): The storage area where the change occurred.
        - action (str): The type of storage action (store or retrieve).
        - item (Item): The item involved in the storage change.
        """
        self.events.append(f"Storage Change in {area} - {action}: {item}")

    def display_events(self):
        """
        Display the logged events.
        """
        print("\nEvent Log:")
        for event in self.events:
            print(event)

