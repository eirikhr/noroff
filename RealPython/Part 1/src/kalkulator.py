# Priser Hverdag

agderHverdagStartS = 69
agderHverdagStartM = 104
agderHverdagStartL = 137
agderHverdagKmS = 13.65
agderHverdagKmM = 24.1
agderHverdagKmOverM = 19.5
agderHverdagKmOverL = 27.7
agderHverdagKmL = 34.6
agderHverdagMin = 7.85

agderHelligStartS = 69
agderHelligStartM = 104
agderHelligStartL = 137
agderHelligKmS = 13.65
agderHelligKmM = 24.1
agderHelligKmOverM = 19.5
agderHelligKmOverL = 27.7
agderHelligKmL = 34.6
agderHelligMin = 7.85

agderHelgStartS = 69
agderHelgStartM = 104
agderHelgStartL = 137
agderHelgKmS = 13.65
agderHelgKmM = 24.1
agderHelgKmOverM = 19.5
agderHelgKmOverL = 27.7
agderHelgKmL = 34.6
agderHelgMin = 7.85

def agderPris(inputkm, inputtid, inputkmover, inputtillegg):
    print()
    print("Beregner pris for {} km (+ {} km over 3 mil ved buss), {} minutter og {},- kroner i tilegg."
          .format(inputkm, inputkmover, inputtid, inputtillegg))
    print()
    print("HVERDAGER 06:00 - 20:00")
    print("1-4 Passasjerer")
    print((inputkm * agderHverdagKmS) + (inputtid * agderHverdagMin) + inputtillegg, ",- kroner")
    print("5-8 Passasjerer")
    print((inputkm * agderHverdagKmM) + (inputtid * agderHverdagMin) + (inputkmover * agderHverdagKmOverM) + inputtillegg, ",- kroner")
    print("9-16 Passasjerer")
    print((inputkm * agderHverdagKmM) + (inputtid * agderHverdagMin) + (inputkmover * agderHverdagKmOverL) + inputtillegg, ",- kroner")
    print()
    print("KVELD 20:00 - 06:00, OG HELGER")
    print("1-4 Passasjerer")
    print((inputkm * agderHelgKmS) + (inputtid * agderHelgMin) + inputtillegg, ",- kroner")
    print("5-8 Passasjerer")
    print((inputkm * agderHelgKmM) + (inputtid * agderHelgMin) + (inputkmover * agderHelgKmOverM) + inputtillegg, ",- kroner")
    print("9-16 Passasjerer")
    print((inputkm * agderHelgKmL) + (inputtid * agderHelgMin) + (inputkmover * agderHelgKmOverL) + inputtillegg, ",- kroner")
    print()
    print("HELLIGDAGER")
    print("1-4 Passasjerer")
    print((inputkm * agderHelligKmS) + (inputtid * agderHelligMin) + inputtillegg, ",- kroner")
    print("5-8 Passasjerer")
    print((inputkm * agderHelligKmM) + (inputtid * agderHelligMin) + (inputkmover * agderHelligKmOverM) + inputtillegg, ",- kroner")
    print("9-16 Passasjerer")
    print((inputkm * agderHelligKmL) + (inputtid * agderHelligMin) + (inputkmover * agderHelligKmOverL) + inputtillegg, ",- kroner")
    print()
    print("Alle priser er inklusive moms")
    print()


while True:
    try:
        kminput = input("Antall kilometer: ")
        if kminput.lower() == "q" or kminput.lower() == "quit":
            break
        if len(kminput) == 0:
            kminput = 0

        mininput = input("Antall minutter: ")
        if mininput.lower() == "q" or mininput.lower() == "quit":
            break
        if len(mininput) == 0:
            mininput = 0

        over30input = input("Antall kilometer over 30 km (kun ved bussbestilling: ")
        if over30input.lower() == "q" or over30input.lower() == "quit":
            break
        if len(over30input) == 0:
            over30input = 0

        tilinput = input("Antall kroner i tillegg: ")
        if tilinput.lower() == "q" or tilinput.lower() == "quit":
            break
        if len(tilinput) == 0:
            tilinput = 0

        agderPris(int(kminput), int(mininput), int(over30input), int(tilinput))
    except ValueError:
        print("That was not an integrer\n")
    except ZeroDivisionError:
        print("You cannot divide anything by 0!")
