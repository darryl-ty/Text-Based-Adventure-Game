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

    def get_health_overall(self):
        return self._health

    def set_name(self, name):
        self._name = name

    def set_age(self, age):
        self._age = age

    def set_gender(self, gender):
        self._gender = gender

    def get_health(self, body_part):
        if body_part.lower() == 'left arm' or body_part.lower() == 'l arm':
            return f'{self.get_name()} - Left Arm: {self._health.get_l_arm_health()}'
        elif body_part.lower() == 'right arm' or body_part.lower() == 'r arm':
            return f'{self.get_name()} - Right Arm: {self._health.get_r_arm_health()}'
        elif body_part.lower() == 'arms' or body_part.lower() == 'arm':
            return f'{self.get_name()} ' \
                   f'- Left Arm: {self._health.get_l_arm_health()} | Right Arm: {self._health.get_r_arm_health()}'
        elif body_part.lower() == 'left leg' or body_part.lower() == 'l leg':
            return f'{self.get_name()} - Left Leg: {self._health.get_l_leg_health()}'
        elif body_part.lower() == 'right leg' or body_part.lower() == 'r leg':
            return f'{self.get_name()} - Right Leg: {self._health.get_r_leg_health()}'
        elif body_part.lower() == 'legs' or body_part.lower() == 'leg':
            return f'{self.get_name()} ' \
                   f'- Left Leg: {self._health.get_l_leg_health()} | Right Leg: {self._health.get_r_leg_health()}'
        elif body_part.lower() == 'body':
            return f'{self.get_name()} ' \
                   f'- Torso: {self._health.get_torso_health()} | Stomach: {self._health.get_stomach_health()}'
        elif body_part.lower() == 'torso':
            return f'{self.get_name()} - Torso: {self._health.get_torso_health()}'
        elif body_part.lower() == 'stomach':
            return f'{self.get_name()} - Stomach: {self._health.get_stomach_health()}'
        elif body_part.lower() == 'head':
            return f'{self.get_name()} - Head: {self._health.get_head_health()}'
        else:
            return f'{self._health.__str__()}'

    def __str__(self):
        if self._player is True:
            return f'This is you. You are {self._name} and are {self._age} years old. ' \
                   f'You have {self._strength} strength, {self._agility} agility, and {self._toughness} toughness.'
        elif self._gender.lower() == 'male':
            return f'This is {self._name}. He is {self._age} years old.'
        else:
            return f'This is {self._name}. She is {self._age} years old.'

    def __repr__(self):
        return f'Player:{self._player},Name:{self._name},Age:{self._age},Sex:{self._gender},' \
               f'Strength:{self._strength},Agility:{self._agility},Toughness:{self._toughness}'
