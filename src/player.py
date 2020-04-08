# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player(Room):
    def __init__(self, name, room, description):
        super().__init__(room, description)
        self.name = name

    def __str__(self):
        return 'Player: %s, your current room: %s. Room description: %s' % (self.name, self.room.room, self.description)
