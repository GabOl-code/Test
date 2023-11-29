class Etel:

    def __init__(self, nev, ar):
        self.nev = nev
        self.ar = ar


class Etterem:
    def __init__(self, etteremNev, menuitems):
        self.etteremNev = etteremNev
        self.menuitems = menuitems

    def __str__(self):
        return f"Az étterem neve: {self.etteremNev}"

    def __add__(self, other):
        if isinstance(other, Etel):
            self.menuitems.append(other)
        else:
            print("Nem étel!")

    def getmenuItems(self):
        for menuitem in self.menuitems:
            print(f"{menuitem.nev}...........{menuitem.ar}")


etel1 = Etel("Húsleves", 800)
etel2 = Etel("Pörkölt nokedlivel", 2500)
my_menu = [etel1, etel2]
my_etterem = Etterem("Kockás abrosz", my_menu)

for i in range(1):
    etelNev = input("Add meg az étel nevét: ")
    etelAr = int(input("Add meg az étel árát: "))
    if etelAr <= 0 or etelAr > 100000:
        print("Az ár nem megfelelő!")
        break
    else:
        my_etterem + Etel(etelNev, etelAr)
my_etterem.getmenuItems()
print(my_etterem)
