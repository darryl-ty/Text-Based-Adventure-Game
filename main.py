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
    if str(gender.lower().strip()) != 'male' or str(gender.lower().strip()) != 'female':
        gender = input(f'Please enter a valid gender: Male or Female\n')

    name = input('Okay next, what is your name? \n')
    try:
        age = int(input('Note: This game is NOT for users 17 years or younger\nHow old are you? \n'))
        if age <= 17:
            age = int(input('Please enter an age of 18 years or older: \n'))
        strength = int(input('On a scale of 1 - 10, how strong are you? \n'))
        if strength > 10 or strength < 1:
            strength = int(input('Please enter a value between 1 - 10 \n'))
        agility = int(input('Similarly, on a scale of 1 - 10, how agile are you? \n'))
        if agility > 10 or agility < 1:
            agility = int(input('Please enter a value between 1 - 10 \n'))
        toughness = int(input('Lastly, on a scale of 1 - 10, how tough are you? \n'))
        if toughness > 10 or toughness < 1:
            toughness = int(input('Please enter a value between 1 - 10 \n'))

    except ValueError:
        print("Please enter a valid number.\n")
        return character_create()

    return Character(name, age, gender, strength, agility, toughness, True)


if __name__ == '__main__':
    main()
