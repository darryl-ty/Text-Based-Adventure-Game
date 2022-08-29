from adventurelib import *
# from art import *
from character import Character

welcome_room = Room("""
\nWelcome to the world of Syrelia.

This short demo will take you through a couple of quests and a boss encounter.
I hope you enjoy and please leave feedback if you have any!

Please type 'start' to begin the game.
""")
character_creation = Room("""
Before we begin, let us get a better idea of what your character looks like.
""")
current_room = welcome_room


def main():
    welcome_message()
    start()


@when('start')
def game_start():
    global current_room
    current_room = character_creation

    say(current_room)
    player = character_create()
    print(player)


def welcome_message():
    global current_room
    print(current_room)


def character_create():
    player = Character()
    player.set_player(True)

    gender = input('Are you male or female?. \n')
    if gender.strip().lower() == "male":
        player.set_gender("Male")
    elif gender.strip().lower() == "female":
        player.set_gender("Female")
    else:
        print("Please enter either 'Male' or 'Female' to progress.")
        return character_create()

    name = input('Okay next, what is your name? \n')
    player.set_name(name)
    try:
        age = int(input('Note: This game is NOT for users 17 years or younger\nHow old are you? \n'))
        player.set_age(age)
        strength = int(input('On a scale of 1 - 10, how strong are you? \n'))
        player.set_strength(strength)
        agility = int(input('Similarly, on a scale of 1 - 10, how agile are you? \n'))
        player.set_agility(agility)
        toughness = int(input('Lastly, on a scale of 1 - 10, how tough are you? \n'))
        player.set_toughness(toughness)

    except ValueError:
        print("Please enter a valid number.\n")
        return character_create()

    if age < 18:
        print("You must be 18 years or older to play.")
        quit()

    if strength > 11 or strength < 0:
        print("Invalid Input for Strength\n")
        return character_create()
    elif agility > 11 or agility < 0:
        print("Invalid Input for Agility\n")
        return character_create()
    elif toughness > 11 or toughness < 0:
        print("Invalid Input for Toughness\n")
        return character_create()

    return player


if __name__ == '__main__':
    main()
