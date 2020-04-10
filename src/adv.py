from room import Room
from player import Player
from item import Item

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


items = {
    'book': Item('book', 'pages filled with knowledge'),
    'pen': Item('pen', 'ink to write wise words')
}

room['outside'].add_item(items['book'])
room['outside'].add_item(items['pen'])


player1 = Player('Sally', room['outside'])
print('Hello ' + str(player1))

print("This Room's items: ")

for i in player1.current_room.items:
    print(i)


print(' Please make your first move.')

moves = input(
    "[n] North  [s] South  [e] East [w] West \n [take item_name] [drop item_name] \n [i] Inventory [q] Quit: ")


while not moves == "q":
    # If player chooses action move
    room_items = []


# print(room_items)
    if len(moves.split()) == 2:
        handle_action = moves.split()
        if handle_action[0] == 'take':
            if len(player1.current_room.items) > 0:
                for item in player1.current_room.items:
                    room_items.append(item.item_name)
            else:
                pass

            if handle_action[1] in room_items:
                player1.on_take(handle_action[1])
                # (player1.current_room).remove_item(handle_action[1])
                print('You have picked up ' + handle_action[1])
            else:
                print("Item not found.")

        elif handle_action[0] == 'drop':
            if handle_action[1] in player1.inventory:
                player1.current_room.add_item(handle_action[1])
                player1.on_drop(handle_action[1])
                print('Dropped ' + handle_action[1])
            else:
                print("Item could not be dropped.")

    # if player chooses INVENTORY
    elif moves == 'i':
        print("Your inventory:")
        for item in player1.inventory:
            print(player1.inventory)

    # if player is OUTSIDE
    elif player1.current_room == room['outside']:
        # if player chooses north
        if moves == "n":
            player1.current_room = room['outside'].n_to
            print(player1)
        else:
            print('Sorry, cannot move that direction. Try again.')

     # if player is in FOYER
    elif player1.current_room == room['foyer']:
        # if player chooses south
        if moves == "s":
            player1.current_room = room['foyer'].s_to
            print(player1)
        # if player chooses north
        elif moves == "n":
            player1.current_room = room['foyer'].n_to
            print(player1)
        # if player chooses east
        elif moves == "e":
            player1.current_room = room['foyer'].e_to
            print(player1)
        else:
            print('Sorry, cannot move that direction. Try again.')

     # if player is in OVERLOOK
    elif player1.current_room == room['overlook']:
        # if player chooses south
        if moves == "s":
            player1.current_room = room['overlook'].s_to
            print(player1)
        else:
            print('Sorry, cannot move that direction. Try again.')

    # if player is in NARROW
    elif player1.current_room == room['narrow']:
        # if player chooses north
        if moves == "n":
            player1.current_room = room['narrow'].n_to
            print(player1)
        # if player chooses west
        elif moves == "w":
            player1.current_room = room['narrow'].w_to
            print(player1)
        else:
            print('Sorry, cannot move that direction. Try again.')

    # if player is in TREASURE
    elif player1.current_room == room['treasure']:
        # if player chooses south
        if moves == "s":
            player1.current_room = room['treasure'].s_to
            print(player1)
        else:
            print('Sorry, cannot move that direction. Try again.')

    print("Please make your next move to continue...")
    moves = (input(
        "[n] North  [s] South  [e] East [w] West \n [take item_name] [drop item_name] \n [i] Inventory [q] Quit: "))
