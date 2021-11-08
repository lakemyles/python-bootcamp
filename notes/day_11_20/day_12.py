# Scope

# Functions, and only functions, create a local scope
# which behaves how you would expect it to in most languages
# You can access global scope variables inside functions,
# but you cannot modify them

# global scope
player_health = 10


def drink_health_potion():
    # local scope
    player_health = 2  # creates new local variable with same name as global variable # don't call local and global variables the same name #
    print(player_health)  # prints local scope value


drink_health_potion()
print(player_health)  # prints global scope value


# THERE IS NO SUCH THING AS BLOCK SCOPE IN PYTHON ##############
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

if game_level < 5:
    new_enemy = enemies[0]

# You have access to the new_enemy variable outside of the above if block!!!!!!
# As long as it's not in a function, then it's local scope only
# Blocks like if/while/for do not create a local scope
print(new_enemy)


# Modifying global scope variables inside functions
# Can only modify global variables by explicitly saying
# we're looking for a global variable, otherwise it's
# going to be looking for a local variable of that name
player_mana = 10


def drink_mana_potion():
    global player_mana  # Have to explicitly say we have a global variable
    player_mana += 2
    print(player_mana)


drink_mana_potion()
print(player_mana)

# Potentially avoid modifying global variables and return them from the function instead
# return player_mana + 2


# Constants
# Naming convention is to use all upper case for variable names, but
# it's not a true constant. It can be modifyed.
