# Running in circles...
'''

n = 1
while (n <= 5):
    print("n =", n)
    n = n + 1
    print("Added one successfully")
print("While loop is now finished. N is now ", n)


for x in range(1, 6):
    print("x =", x)
print("For loop is now finished. X is now", x)


for x in range(1, 7):
    for j in ["a", "b", "c", "d", "f"]:
        print("x =", x, "and j =", j)

'''

for x in range(2, 11):
    print ("x =", x)


n = 2
print("While loop")

while (n < 11):
    print("N =", n)
    n = n + 1

print("Finished.")

def doubles(input):
    for x in range(1, 4):
        input = input * 2
        print(input)

doubles(4)
doubles(7)