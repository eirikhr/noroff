while True:
    data = input("$>")
    if data.lower() == "q":
        break

# tast q for og komme til denne delen

for i in range(1, 51):
    if i % 3 == 0:
        continue
    print(i)
