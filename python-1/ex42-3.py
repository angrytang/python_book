from sys import exit
from random import randint

class Game(object):

    def __init__(self, start):
        self.quips = [
            "You died.",
            "Such a luser"
        ]
        self.start = start

    def play(self):
        next = self.start
        while True:
            print("\n--------")
            room = getattr(self, next)
            next = room()

    def death(self):
        print(self.quips[randint(0, len(self.quips)-1)])
        exit(1)

    def central_corridor(self):
        print("escape pod.")
        print("Please input 3 actions:")
        print("1.'shoot!'")
        print("2.'dodge!'")
        print("3.'tell a joke'")
        print("\n")
        action = input("> ")
        if action == "shoot!":
            return 'death'
        elif action == "dodge!":
            return 'death'
        elif action == "tell a joke":
            return 'laser_weapon_armory'
        else:
            return 'centeral_corridor'

    def laser_weapon_armory(self):
        print("get the bomb. The code is 1 digits.")
        code = "%d"%(randint(1,9))
        guess = input("[keypad]> ")
        guesses = 0
        while guess != code and guesses < 10:
            print("BZZZZEDDD!")
            guesses += 1
            guess = input("[keypad]> ")
        if guess == code:
            return 'the_bridge'
        else:
            return 'death'

    def the_bridge(self):
        print("Please input 2 actions:")
        print("1.'throw the bomb'")
        print("2.'slowly place the bomb'")
        action = input("> ")
        if action == "throw the bomb":
            return 'death'
        elif action == "slowly place the bomb":
            return 'escape_pod'
        else:
            return 'the_bridge'

    def escape_pod(self):
        print("There's 5 pods, which one do you take?")
        good_pod = randint(1,5)
        guess = input("[pod #]> ")
        if int(guess) != good_pod:
            return 'death'
        else:
            print("You won!")
            exit(0)

a_game = Game("central_corridor")
a_game.play()
