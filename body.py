_HEALTH_STATE = ['Dead', 'Broken', 'Badly Injured', 'Injured', 'Slightly Injured', 'Fine']

class Body:

    def __init__(self, head=5, torso=10, stomach=10, l_arm=10, r_arm=10, l_leg=10, r_leg=10):
        self._head: int = head
        self._torso: int = torso
        self._stomach: int = stomach
        self._l_arm: int = l_arm
        self._r_arm: int = r_arm
        self._l_leg: int = l_leg
        self._r_leg: int = r_leg

    def get_head_health(self):
        if self._head == 5:
            return _HEALTH_STATE[5]
        elif self._head == 4:
            return _HEALTH_STATE[4]
        elif self._head == 3:
            return _HEALTH_STATE[3]
        elif self._head >= 1:
            return _HEALTH_STATE[2]
        elif self._head == 0:
            return _HEALTH_STATE[0]

    def get_torso_health(self):
        if self._torso >= 8:
            return _HEALTH_STATE[5]
        elif self._torso >= 6:
            return _HEALTH_STATE[4]
        elif self._torso >= 4:
            return _HEALTH_STATE[3]
        elif self._torso >= 1:
            return _HEALTH_STATE[2]
        elif self._torso == 0:
            return _HEALTH_STATE[0]

    def get_stomach_health(self):
        if self._stomach >= 8:
            return _HEALTH_STATE[5]
        elif self._stomach >= 6:
            return _HEALTH_STATE[4]
        elif self._stomach >= 4:
            return _HEALTH_STATE[3]
        elif self._stomach >= 1:
            return _HEALTH_STATE[2]
        elif self._stomach == 0:
            return _HEALTH_STATE[0]

    def get_l_arm_health(self):
        if self._l_arm >= 8:
            return _HEALTH_STATE[5]
        elif self._l_arm >= 6:
            return _HEALTH_STATE[4]
        elif self._l_arm >= 4:
            return _HEALTH_STATE[3]
        elif self._l_arm >= 1:
            return _HEALTH_STATE[2]
        elif self._l_arm == 0:
            return _HEALTH_STATE[1]

    def get_r_arm_health(self):
        if self._r_arm >= 8:
            return _HEALTH_STATE[5]
        elif self._r_arm >= 6:
            return _HEALTH_STATE[4]
        elif self._r_arm >= 4:
            return _HEALTH_STATE[3]
        elif self._r_arm >= 1:
            return _HEALTH_STATE[2]
        elif self._r_arm == 0:
            return _HEALTH_STATE[1]

    def get_l_leg_health(self):
        if self._l_leg >= 8:
            return _HEALTH_STATE[5]
        elif self._l_leg >= 6:
            return _HEALTH_STATE[4]
        elif self._l_leg >= 4:
            return _HEALTH_STATE[3]
        elif self._l_leg >= 1:
            return _HEALTH_STATE[2]
        elif self._l_leg == 0:
            return _HEALTH_STATE[1]

    def get_r_leg_health(self):
        if self._r_leg >= 8:
            return _HEALTH_STATE[5]
        elif self._r_leg >= 6:
            return _HEALTH_STATE[4]
        elif self._r_leg >= 4:
            return _HEALTH_STATE[3]
        elif self._r_leg >= 1:
            return _HEALTH_STATE[2]
        elif self._r_leg == 0:
            return _HEALTH_STATE[1]

    def set_head_health(self, health: int):
        self._head = health

    def set_torso_health(self, health: int):
        self._torso = health

    def set_stomach_health(self, health: int):
        self._stomach = health

    def set_l_arm_health(self, health: int):
        self._l_arm = health

    def set_r_arm_health(self, health: int):
        self._r_arm = health

    def set_l_leg_health(self, health: int):
        self._l_leg = health

    def set_r_leg_health(self, health: int):
        self._r_leg = health

    def __str__(self):
        return f'\nHead Health - {self.get_head_health()}\nTorso Health - {self.get_torso_health()} ' \
               f'\nStomach Health - {self.get_stomach_health()}\nLeft Arm Health - {self.get_l_arm_health()} ' \
               f'\nRight Arm Health - {self.get_r_arm_health()}\nLeft Leg Health - {self.get_l_leg_health()} ' \
               f'\nRight Leg Health - {self.get_r_leg_health()}'

    def __repr__(self):
        return f'Head:{self._head}, Torso:{self._torso}, Stomach:{self._stomach}, ' \
               f'Left Arm:{self._l_arm}, Right Arm:{self._r_arm}, Left Leg:{self._l_leg}, Right Leg:{self._r_leg}'
