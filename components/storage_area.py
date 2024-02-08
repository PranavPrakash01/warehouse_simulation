# storage_area.py

from items import Item

class StorageArea:
    def __init__(self, name, max_capacity):

        self.name = name
        self.max_capacity = max_capacity
        self.stored_items = []

    def store_item(self, item):

        if len(self.stored_items) < self.max_capacity:
            self.stored_items.append(item)
            print(f"Item stored in Storage Area {self.name}: {item}")
        else:
            print(f"Storage Area {self.name} is full. Cannot store more items.")

    def retrieve_item(self):

        if self.stored_items:
            retrieved_item = self.stored_items.pop(0)
            print(f"Item retrieved from Storage Area {self.name}: {retrieved_item}")
            return retrieved_item
        else:
            print(f"Storage Area {self.name} is empty. No items to retrieve.")
            return None