class Titkos:

    def __init__(self):
        self._titkos_attributum = "Titkos üzenet"

    def kiir(self):
        print(self._titkos_attributum)

obj = Titkos()
obj.kiir() #Output: Titkos üzenet

obj._Titkos_szuper_titkos_attributum = "Nem annyira titkos"

obj.kiir()
