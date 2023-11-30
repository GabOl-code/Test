class Titkos:

    def __init__(self):
        self._titkos_attributum = "Titkos üzenet"

    def kiir(self):
        print(self._titkos_attributum)

obj = Titkos()
obj.kiir() #Output: Titkos üzenet

obj.__titkos_attributum = "Nem annyira titkos"

obj.kiir()
