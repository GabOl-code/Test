inputresult1 = input ("Írj be egy szöveget: ")

print(inputresult1)
print(type(inputresult1))

inputresult2 = input ("Írj be egy számot: ")

if not isinstance(inputresult2, int):
    raise TypeError("Nem szám")
else:
    if inputresult2 < 10:
        raise ValueError("10-nél nagyobb számot adj meg!!")
