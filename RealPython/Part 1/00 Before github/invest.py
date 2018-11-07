def invest(beløp, vekst, tid):
    print()
    print("\nOpprinnelig beløp:", int(beløp))
    print("Årlig vekst:", minVekst * 100, "prosent")
    for t in range(1, tid + 1):
        beløp = beløp * (1 + vekst)
        print("År {}: {} kr".format(t, beløp))
    print()


mittBeløp = int(input("Investeringsbeløp:\n"))
minVekst = int(input("Stigningsprosent:\n")) / 100
minTid = int(input("År:\n"))

invest(mittBeløp, minVekst, minTid)
