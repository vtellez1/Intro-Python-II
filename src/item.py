# Create a file called item.py and add an Item class in there.
# The item should have name and description attributes.
# Hint: the name should be one word for ease in parsing later.
# This will be the base class for specialized item types to be declared later.


class Item():
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description

    def __str__(self):
        return f"item_name: {self.item_name}, description: {self.item_description}"
