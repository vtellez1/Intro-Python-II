from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player1 = Player('Sally', room['outside'],
                 room['outside'].description)
print('Hello ' + str(player1) + ' Please make your first move.')

moves = (input("[n] North  [s] South  [e] East [w] West [q] Quit: "))


while not moves == "q":

    # if player is OUTSIDE
    if player1.room == room['outside']:
        # if player chooses north
        if moves == "n":
            player1.room = room['outside'].n_to
            print(player1)
        else:
            print('Sorry, cannot move that direction. Try again.')

     # if player is in FOYER
    elif player1.room == room['foyer']:
        # if player chooses south
        if moves == "s":
            player1.room = room['foyer'].s_to
            print(player1)
        # if player chooses north
        elif moves == "n":
            player1.room = room['foyer'].n_to
            print(player1)
        # if player chooses east
        elif moves == "e":
            player1.room = room['foyer'].e_to
            print(player1)
        else:
            print('Sorry, cannot move that direction. Try again.')

     # if player is in OVERLOOK
    elif player1.room == room['overlook']:
        # if player chooses south
        if moves == "s":
            player1.room = room['overlook'].s_to
            print(player1)
        else:
            print('Sorry, cannot move that direction. Try again.')

    # if player is in NARROW
    elif player1.room == room['narrow']:
        # if player chooses north
        if moves == "n":
            player1.room = room['narrow'].n_to
            print(player1)
        # if player chooses west
        elif moves == "w":
            player1.room = room['narrow'].w_to
            print(player1)
        else:
            print('Sorry, cannot move that direction. Try again.')

    # if player is in TREASURE
    elif player1.room == room['treasure']:
        # if player chooses south
        if moves == "s":
            player1.room = room['treasure'].s_to
            print(player1)
        else:
            print('Sorry, cannot move that direction. Try again.')

    print("Please make your next move to continue...")
    moves = (input("[n] North  [s] South  [e] East [w] West [q] Quit: "))
