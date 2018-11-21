distance = [1, 1.5, 2.8, 1.9, 3, 4.6, 5.2]

# FOR LOOPS
# Summing up Distance
total = 0

# for each-item in list
for i in distance:
    total += i

print("First for loop total number: {}".format(total))

shopping_list = ["Epler", "Bananer", "Druer", "Egg"]
basket = ["Melk"]

basket.append("Sjokolade")
basket.append(shopping_list.pop(3))

print(shopping_list)
print(basket)

