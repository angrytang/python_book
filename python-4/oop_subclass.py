class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def tell(self):
        print("Name:{} Age:{}".format(self.name, self.age), end=' ')


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print("Initialized Teacher:{}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Salary:{}".format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print("Initialized Student:{}".format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print("Marks:{}".format(self.marks))

t1 = Teacher("Mrs.Li", 40, 18000)
s1 = Student("Tom", 16, 88)
print()

t1.tell()
s1.tell()
