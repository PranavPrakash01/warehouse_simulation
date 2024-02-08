# sorting_area.py

from items import Item

class SortingArea:
    def __init__(self, name):

        self.name = name

    def sort_items(self, items):

        sorted_items = []

        # Implement sorting logic here based on criteria
        # For example, sorting by location
        sorted_items = sorted(items, key=lambda x: x.location)

        print(f"Items sorted in Sorting Area {self.name}: {sorted_items}")
