import random
from body import Body


class Character:

    def __init__(self, name, age, gender, strength=random.randint(1, 5),
                 agility=random.randint(1, 5), toughness=random.randint(1, 5), player=False):
        self._name: str = name
        self._age: int = age
        self._gender: str = gender
        self._health = Body()
        self._strength: int = strength
        self._agility: int = agility
        self._toughness: int = toughness
        self._player: bool = player

    def get_name(self):
        return self._name

    def get_age(self):
        return self._age

    def get_gender(self):
        return self._gender

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_gender(self, gender):
        self._gender = gender

    #TODO - Implement the rest of the get_health checks for other body parts.
    #TODO - If not looking at player, give rough idea of health instead of specific integer value.
    def get_health(self, body_part):
        if body_part.lower() == 'left arm' or body_part.lower() == 'l arm':
            return f'{self._name} - Left Arm: {self._health.get_l_arm_health()}'

    def __str__(self):
        if self._player is True:
            return f'This is you. You are {self._name} and are {self._age} years old. You have {self._strength} strength, ' \
                   f'{self._agility} agility, and {self._toughness} toughness.'
        elif self._gender.lower() == 'male':
            return f'This is {self._name}. He is {self._age} years old.'
        else:
            return f'This is {self._name}. She is {self._age} years old.'

    def __repr__(self):
        return f'Player:{self._player},Name:{self._name},Age:{self._age},Sex:{self._gender},' \
               f'Strength:{self._strength},Agility:{self._agility},Toughness:{self._toughness}'
