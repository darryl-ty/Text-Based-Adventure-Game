from adventurelib import *
from art import *
from character import Character
from body import Body

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


@when('start')
def game_start():
    global current_room
    current_room = character_creation

    say(current_room)
    gender = input('Are you male or female?')
    name = input('\nOkay next, what is your name?')
    age = input('\nHow old are you?')
    strength = input('\nOn a scale of 1 - 10, how strong are you?')
    agility = input('\nSimilarly, on a scale of 1 - 10, how agile are you?')
    toughness = input('\nLastly, on a scale of 1 - 10, how tough are you?')
    player = Character(name, age, gender, strength, agility, toughness, True)
    player_health = Body()
    print(player.name)
    print(player_health)


def welcome_message():
    global current_room
    print(current_room)


def main():
    welcome_message()
    start()


if __name__ == '__main__':
    main()
