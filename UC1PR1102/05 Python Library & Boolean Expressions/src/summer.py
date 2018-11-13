sum = 0  # To avoid declaring int()

while True:
    num = int(input("Add a number: "))
    if num != 0:
        sum = sum + num
        print(sum)
    else:
        print("Sluttsum er", sum)
        break
