from photo_album2 import OnlineFotoalbum


class BeleptetoRendszer:
    def __init__(self):
        self._user1_nev = "user1"
        self._user1_jelszo = "pw123"
        self._user2_nev = "user2"
        self._user2_jelszo = "pw456"
        self._admin_nev = "admin"
        self._admin_jelszo = "admin123"
        self._bejelentkezett_felhasznalo = None
        self._online_fotoalbum = OnlineFotoalbum()

    def _ellenoriz(self, nev, jelszo):
        if nev == self._user1_nev and jelszo == self._user1_jelszo:
            return "user1"
        elif nev == self._user2_nev and jelszo == self._user2_jelszo:
            return "user2"
        elif nev == self._admin_nev and jelszo == self._admin_jelszo:
            return "admin"
        else:
            return None

    def belepes(self):
        while True:
            nev = input("Felhasználónév: ")
            jelszo = input("Jelszó: ")
            felhasznalo = self._ellenoriz(nev, jelszo)
            if felhasznalo:
                self._bejelentkezett_felhasznalo = felhasznalo
                print(f"Sikeres belépés {felhasznalo} Online Fotóalbumodba!")
                if felhasznalo == "admin":
                    self._kiir_jelszavak()
                elif felhasznalo.startswith("user"):
                    self._kezel_fotoalbum()
                break
            else:
                print("Nem megfelelő jelszó vagy felhasználónév! Kérem, próbálja újra.")

    def _kiir_jelszavak(self):
        print(f"A felhasználók jelszavai:\nuser1: {self._user1_jelszo}\nuser2: {self._user2_jelszo}")

    def _kezel_fotoalbum(self):
        album_nev = f"{self._bejelentkezett_felhasznalo.capitalize()} Online Fotóalbum"
        self._online_fotoalbum.set_album_nev(album_nev)

        cim = input("Kép címe: ")
        meret = input("Kép mérete: ")
        formatum = input("Kép formátuma: ")

        self._online_fotoalbum.set_foto_adatok(cim, meret, formatum)
        print("Kép feltöltése sikeres.")
        print("Kép adatok:", self._online_fotoalbum.get_foto_adatok())

        valtoztatni = input("Szeretné megváltoztatni a kép méretét vagy formátumát? \n i=igen, egyéb gombra kilép: ")
        if valtoztatni.lower() == "i":
            uj_meret = input("Új méret: ")
            uj_formatum = input("Új formátum: ")
            self._online_fotoalbum.set_foto_adatok(cim, uj_meret, uj_formatum)
            print("Kép adatok frissítve.")
            print("Új kép adatok:", self._online_fotoalbum.get_foto_adatok())
        else:
            print("Sikeres kilépés!")

    @property
    def bejelentkezett_felhasznalo(self):
        return self._bejelentkezett_felhasznalo

    @bejelentkezett_felhasznalo.setter
    def bejelentkezett_felhasznalo(self, value):
        self._bejelentkezett_felhasznalo = value


# Tesztelés
rendsz = BeleptetoRendszer()
rendsz.belepes()
