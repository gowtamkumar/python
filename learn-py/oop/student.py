class Info:
    @staticmethod
    def result():
        print("result started")

    @staticmethod
    def result1():
        print("Result number 2")


class StudentRols:
    def __init__(self, role):
        self.role = role
        print("This is a Student Rols", role)

    def role_run(self):
        print("this is role function")


class Student(Info, StudentRols):
    age = 33

    # default constructors
    def __init__(self):
        pass

    def __init__(self, name, marks, role):
        super().__init__(role)
        self.name = name
        self.marks = marks

    @classmethod
    def change_name(cls, age):
        cls.age = age

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

    @property
    def get_marks(self):
        return [mark * 2 for mark in self.marks]


result = Student("Gowtam kumar", [80, 60, 60], 40)
# del result.name
# del result
print(result.age)

result.change_name(66)

print(result.age)

print(result.get_marks)

# class StudentDetails(Student):
#     def __init__(self):
#         print("this is student details")

#     def get_student_details(self):
#         print("this is a Students")


# det_result = StudentDetails()
# print("this is multile lavel class", det_result.get_avg_marks())
