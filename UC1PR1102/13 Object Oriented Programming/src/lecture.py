class Computing:
    def __init__(self, first, last, registration):
        self.first = first
        self.last = last
        self.registration = registration
        self.email = first + "." + last + "@noroff.no"

    def fullname(self):
        return "{} {}" .format(self.first, self.last)


student_1 = Computing("Eirik", "Rynning", 90050985)
student_2 = Computing("James", "Cook", 123456789)
print(student_1)
print(student_2)

"""
student_1.first = "Eirik"
student_1.last = "Rynning"
student_1.email = "erynning@gmail.com"
student_1.registration = 90050985

student_2.first = "James"
student_2.last = "Cook"
student_2.email = "james.cook@gmail.com"
student_2.registration = 90060985

"""

print(student_1.email)
print(student_1.fullname())

