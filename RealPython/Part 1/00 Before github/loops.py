"""

n = 7


while (n > -1):
    print("n =", n)
    n = n - 1


print("Loop finished")


for n in range(1, 5):
    print("n = ", n)
print("Loop finished")


for n in range(1, 3):
    for j in ["a", "b", "c", "d", "EIRIK"]:
        print("n =", n, "and j =", j)


for n in range(2, 11):
    print("n =", n)

print("Loop finished")

n = 2

while (n < 11):
    print("n = ", n)
    n = n + 1

print("Loop finished")


def double(n1):
    return n1 * 2


myNum = int(input("My number: "))

for n in range(0, 3):
    myNum = double(myNum)
    print(myNum)

"""


