class Test:
    def __init__(self, foo):
        self.__foo = foo

        def __bar(self):
            print(self.__foo)
            print('__bar')

def main():
    test = Test('hello')



if __name__ == "__main__":
    main()