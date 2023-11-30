class OnlineFotoalbum:
    def __init__(self):
        self._album_nev = ""
        self._foto_cim = ""
        self._foto_meret = ""
        self._foto_formatum = ""

    def set_album_nev(self, album_nev):
        self._album_nev = album_nev

    def get_album_nev(self):
        return self._album_nev

    def set_foto_adatok(self, cim, meret, formatum):
        self._foto_cim = cim
        self._foto_meret = meret
        self._foto_formatum = formatum

    def get_foto_adatok(self):
        return f"Cím: {self._foto_cim}, Méret: {self._foto_meret}, Formátum: {self._foto_formatum}"
