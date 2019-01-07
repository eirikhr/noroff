# When starting, no tries have been made
tries = 0

while tries < 3:                                            # Så lenge vi ikke har prøvd tre ganger eller mer
    password = input("Password: ")                          # Spør etter passord.
    if password == "I<3BIEBER":                             # Hvis riktig passord
        break                                               # Bryt ut, directe til linje 15 (Logget inn)
    else:                                                   # Ved feil passord
        tries += 1                                          # Legg til et forsøk ved bruk av +=
        print("Nope.")                                      # Og si nei.
else:                                                       # Siden vi nå har fått 3 (eller flere forsøk)
    print("Suspicious activity. Sending email to boss.")    # Har vi fått nok, og sender mail til eieren av løsning.
    quit()                                                  # Lukk programmet

print("Successfully logged in.")                            # Har vi unngått siste else statement, er du da logget inn.


# When starting, no tries have been made
tries = 0

while tries < 3:
    password = input("Password: ")
    if password == "I<3BIEBER":
        break
    else:
        tries += 1
        print("Nope.")
else:
    print("Suspicious activity. Sending email to boss.")
    quit()

print("Successfully logged in.")
print("Run your code here!")
