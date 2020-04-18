# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item


class Room:
    def __init__(self, room, description, items=None, n_to=None, s_to=None, e_to=None, w_to=None):
        self.room = room
        self.description = description
        self.items = [] if items is None else items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    def __str__(self):
        return 'Your current room: %s. Room description: %s.' % (self.room, self.description)

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)
