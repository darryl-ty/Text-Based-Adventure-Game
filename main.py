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

    gender = input('Are you male or female? \n')
    name = input('Okay next, what is your name? \n')
    try:
        age = int(input('Note: This game is NOT for users 17 years or younger\nHow old are you? \n'))
        strength = int(input('On a scale of 1 - 10, how strong are you? \n'))
        agility = int(input('Similarly, on a scale of 1 - 10, how agile are you? \n'))
        toughness = int(input('Lastly, on a scale of 1 - 10, how tough are you? \n'))

    except ValueError:
        print("Please enter a valid number.\n")
        return character_create()

    if age < 18:
        print("You must be 18 years or older to play.")
        quit()

    elif strength < 0 and strength > 11 or agility < 0 and agility > 11 or toughness < 0 and toughness > 11:
        print("Invalid Input\n")
        return character_create()

    elif gender.lower().strip() != 'male' or gender.lower().strip() != 'female':
        print("Enter Male or Female please.\n")
        return character_create()

    return Character(name, age, gender, strength, agility, toughness, True)


if __name__ == '__main__':
    main()
