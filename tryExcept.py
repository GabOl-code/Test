while True:
    try:
        inputszam = int(input("Adj meg egy számot: "))
        print(inputszam)
        print(type(inputszam))
        break

    except ValueError:
        print("Nem egész szám!! Próbáld újra!")