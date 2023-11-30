class OnlineFotoalbum:
    def __init__(self, felhasznalo_nev):
        self._felhasznalo_nev = felhasznalo_nev
        self._kepek = []

    def foto_feltoltes(self, cim, meret, formatum):
        kepadat = {"cim": cim, "meret": meret, "formatum": formatum}
        self._kepek.append(kepadat)
        return f"Sikeres a kép feltöltése: {cim} ({meret}, {formatum})"

    def kepek_listazasa(self):
        return self._kepek

    def kepadat_modositasa(self, index, uj_meret=None, uj_formatum=None):
        if uj_meret:
            self._kepek[index]["meret"] = uj_meret
        if uj_formatum:
            self._kepek[index]["formatum"] = uj_formatum
        return f"A kép adatok sikeresen módosítva: {self._kepek[index]['cim']} ({self._kepek[index]['meret']}, {self._kepek[index]['formatum']})"
