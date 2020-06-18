from time import sleep

class Clock(object):
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def show(self):
        return '%02d:%02d:%02d'%(self.hour, self.minute, self.second)

    def run(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
            if self.minute == 60:
                self.hour += 1
                self.minute = 0
                if self.hour == 24:
                    self.hour = 0

def main():
    clock = Clock(10,12,12)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()

if __name__ == '__main__':
    main()