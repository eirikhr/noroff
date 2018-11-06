def invest(amount, rate, time):
    print("Beløp som skal investeres:", str(amount))
    print("Vekstfaktoren er:", str(rate))
    for t in range(1, time + 1):
        amount = amount * (1 + rate)
        print("År", str(t), ":", str(amount))


invest(10, .25, 3)
