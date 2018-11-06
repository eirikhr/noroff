for i in range(0, 53):
    if i >= 3:
        continue
    print(i)

print("Finished with i = ", str(i))

phrase = "Hei hei hallo"

for letter in phrase:
    if letter == "X":
        break
    else:
        print('There was no "X" in the phrase')

