from random import random

total_A = 0
total_B = 0
trials = 1000000

for trial in range(0, trials):
    A_win = 0
    B_win = 0
    if random() < .87:
        A_win += 1
    else:
        B_win +=1
    if random() < .65:
        A_win += 1
    else:
        B_win +=1
    if random() < .17:
        A_win += 1
    else:
        B_win +=1
    if A_win > B_win:
        total_A += 1
        print("A won trial {}.".format(trial))
    else:
        total_B += 1
        print("B won trial {}".format(trial))

print("Total A wins: {} - and total B wins: {}".format(total_A, total_B))
print("Probability A wins:", total_A / trials * 100, "percent")
print("Probability B wins:", total_B / trials * 100, "percent")