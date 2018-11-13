from random import randint

# HEADS AND TAILS
"""
heads = 0
tails = 0

for trial in range(0, 524845):
    while randint(0, 1) == 0:
        tails += 1
        # print("Heads =", heads, "and tails =", tails)
    heads += 1
    # print("Heads =", heads, "and tails =", tails)

print("heads / tais", heads/tails)
print("Heads =", heads, "and tails =", tails)
"""

# DICE
ener = 0
toer = 0
treer = 0
firer = 0
femmer = 0
sekser = 0


for trial in range(0, 10000):
    while randint(0, 5) == 0:
        ener += 1
    while randint(0, 5) == 1:
        toer += 1
    while randint(0, 5) == 2:
        treer += 1
    while randint(0, 5) == 3:
        firer += 1
    while randint(0, 5) == 4:
        femmer += 1
    while randint(0, 5) == 4:
        sekser += 1
    trial += 1

print("enere:")
print(ener)
print("toere:")
print(toer)
print("treere:")
print(treer)
print("firere:")
print(firer)
print("femmere:")
print(femmer)
print("seksere:", sekser)
print(sekser)
gjennomsnitt = (ener + (toer * 2) + (treer * 3) + (firer * 4) + (femmer * 5) + (sekser * 6)) / trial
print("Gjennomsnittstall: ", gjennomsnitt)

