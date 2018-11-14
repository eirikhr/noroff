import math

def arealkvadrat(grunnlinje, høyde):
    if not grunnlinje.isdigit() or not høyde.isdigit():
        print("Invalid input")
        return
    else:
        return int(grunnlinje) * int(høyde)


def arealcircle(radius):
    if not radius.isdigit():
        return "Invalid input"
    return math.pi * int(radius)**2


def arealtrekant(grunnlinje, høyde):
    if not grunnlinje.isdigit() or not høyde.isdigit():
        print("Invalid input")
        return
    else:
        return (int(grunnlinje) * int(høyde)) / 2


grunnlinje = input("Grunnlinje: ")
høyde = input("Høyde: ")
radius = input("Radius: ")

print("Areal for kvadrat = ", arealkvadrat(grunnlinje, høyde))
print("Areal for trekant = ", arealtrekant(grunnlinje, høyde))
print("Areal for sirkel = ", arealcircle(radius))
