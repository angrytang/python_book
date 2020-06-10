class Robot:
    """表示有个带有名字的机器人"""
    #一个类变量，用来技术机器人的数量
    population = 0

    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))

        #当有人被创建时，机器人
        #将会增加人口数
        Robot.population += 1

    def die(self):
        """我挂了"""
        print("{} is being destroyed!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last one".format(self.name))
        else:
            print("There are still {:d} robots working.".format(self.population))

    def say_hi(self):
        """来自机器人的惩治问候"""
        print("Greetings, my masters call me {}".format(self.name))

    @classmethod
    def how_many(cls):
        """打印出当前人口数量"""
        print("We have {:d} robots.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print("\nRobots can do some wrok here.\n")

print("Robots have finished their work. So let's destroy them.")
droid1.die()
droid2.die()

Robot.how_many()