# Testing functions

def addisjon(no1, no2):
    resultat = no1 + no2
    return resultat


def rot(no1):
    resultat = no1 * no1
    return resultat


def gange(no1, no2):
    resultat = no1 * no2
    return resultat


# Script

tall = addisjon(2, 3)
print("Tall er lik", tall)
rottall = rot(tall)
print("Roten av tall er lik", rottall)
supertall = gange(tall, rottall)
print ("Supertallet er lik", supertall)
