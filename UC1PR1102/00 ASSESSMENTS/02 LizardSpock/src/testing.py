class Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

    def introduce_self(self):
        print("My name is:", self.name)

class Person:
    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False



r1 = Robot("Tom", "Red", 30)
r2 = Robot("Jerry", "Blue", 40)

p1 = Person("Alice", "Aggressive", False)
p2 = Person("Becky", "Talkative", True)

p1.robot_owned = r2
p2.robot_owned = r1

p1.robot_owned.introduce_self() # Ber p1's robot om og introdusere seg selv.
