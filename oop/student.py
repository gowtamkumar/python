class Info:
    @staticmethod
    def result():
        print("result started")

    @staticmethod
    def result1():
        print("Result number 2")


class Student(Info):
    # default constructors
    def __init__(self):
        pass

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Called Constructor")

    @staticmethod
    def welcome():
        print("Welcome to This function")

    def get_avg_marks(self):
        avg = 0
        for value in self.marks:
            avg += value
        return avg / len(self.marks)

    # private fun
    def __hello(self):
        print("Hello person")

    def welcome2(self):
        self.__hello()


result = Student("Gowtam kumar", [80, 60, 60])
result.result()  # you can not access
