

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
        return self._head

    def get_torso_health(self):
        return self._torso

    def get_stomach_health(self):
        return self._stomach

    def get_l_arm_health(self):
        return self._l_arm

    def get_r_arm_health(self):
        return self._r_arm

    def get_l_leg_health(self):
        return self._l_leg

    def get_r_leg_health(self):
        return self._r_leg

    def __str__(self):
        return f'Head Health - {self._head} | Torso Health - {self._torso} | Stomach Health - {self._stomach} | ' \
               f'Left Arm Health - {self._l_arm} | Right Arm Health - {self._r_arm} | Left Leg Health - {self._l_leg} | ' \
               f'Right Leg Health - {self._r_leg}'

    def __repr__(self):
        return f'Head:{self._head}, Torso:{self._torso}, Stomach:{self._stomach}, ' \
               f'Left Arm:{self._l_arm}, Right Arm:{self._r_arm}, Left Leg:{self._l_leg}, Right Leg:{self._r_leg}'
