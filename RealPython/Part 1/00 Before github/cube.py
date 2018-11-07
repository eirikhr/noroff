def cube(n1):
    out = n1 * n1 * n1
    return out


def multiply(n1, n2):
    out = n1 * n2
    return out


def fahrToCelc(n1):
    out = (int(n1) - 32) * 5/9
    return out


def celcToFahr(n1):
    out = int(n1) * 9/5 + 32
    return out


# print(cube(3))
# print(multiply(4, 2))
fahrInput = input("Input Fahrenheit: ")
celcInput = input("Input Celcius: ")

print(fahrToCelc(fahrInput))
print(celcToFahr(celcInput))
