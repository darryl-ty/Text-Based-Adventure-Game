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
    gender = input('Are you male or female? ')
    if gender.lower().strip() != 'male' or gender.lower().strip() != 'female':
        gender = input(f'\nPlease enter a valid gender: Male or Female\n')

    name = input('\nOkay next, what is your name? ')
    try:
        age = int(input('\nHow old are you? \nNote: This game is NOT for users 17 years or younger: '))
        if age <= 17:
            age = int(input('Please enter an age of 18 years or older: '))
        strength = int(input('\nOn a scale of 1 - 10, how strong are you? '))
        agility = int(input('\nSimilarly, on a scale of 1 - 10, how agile are you? '))
        toughness = int(input('\nLastly, on a scale of 1 - 10, how tough are you? '))
    except ValueError:
        print("Please enter a valid number.\n")
        return game_start()

    return Character(name, age, gender, strength, agility, toughness, True)


if __name__ == '__main__':
    main()
