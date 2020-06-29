from abc import ABCMeta, abstractmethod
from random import randint, randrange

class Fighter(object, metaclass=ABCMeta):
    __slots__ = ('name', 'hp')

    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    @property
    def name(self):
        return self.name

    @property
    def hp(self):
        return self.hp

    @hp.setter
    def hp(self, hp):
        self.hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self.hp > 0

    @abstractmethod
    def attack(self, other):
        pass


class Ultraman(Fighter):
    __slots__ = ('name', 'hp', 'mp')
    def __init__(self, name, hp, mp):
        super().__init__(name, hp)
        self.mp = mp

    def attack(self, other):
        other.hp -= randint(15, 25)

    def huge_attack(self, other):
        if self.mp >= 50:
            self.mp -= 50
            injury = other.hp * 3 // 4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False
    
    def magic_attack(self, others):
        if self.mp >= 20:
            self.mp -= 20
            for temp in others:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        incr_point = randint(1, 10)
        self.mp += incr_point
        return incr_point

    def __str__(self):
        return '~~~%sUltraman~~~\n'%self.name + 'HP:%d\n'%self.hp + 'MP:%d\n'%self.mp


class Monster(Fighter):
    __slots__ = ('name', 'hp')

    def attack(self, other):
        other.hp -= randint(10, 20)
    
    def __str__(self):
        return '~~~%sMonsters~~~\n'%self.name + 'HP:%d\n'%self.hp
        