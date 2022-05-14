from random import random
from body import  Body


class Character:

    def __init__(self, name, age, gender, strength, agility, toughness, player=False):
        self._name: str = name
        self._age: int = age
        self._gender: str = gender
        self._strength: int = strength
        self._agility: int = agility
        self._toughness: int = toughness
        self._player: bool = player

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
