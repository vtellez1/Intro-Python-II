# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player():
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = [] if inventory is None else inventory

    def __str__(self):
        return 'Player: %s. %s' % (self.name, self.current_room)

    def on_take(self, item):
        self.inventory.append(item)

    def on_drop(self, item):
        self.inventory.remove(item)
