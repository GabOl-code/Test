inputresult1 = input ("Írj be egy szöveget: ")

print(inputresult1)
print(type(inputresult1))

szam = int(input ("Írj be egy számot: "))
if isinstance(szam, int):
    print(szam)
    print(type(szam))

szam1 = int(input ("Írj be egy számot: "))

if not (isinstance(szam1, int)):
    raise TypeError("Nem szám")
else:
    if szam1 < 10:
        raise ValueError("10-nél nagyobb számot adj meg!!")
print(szam1)
print(type(szam1))