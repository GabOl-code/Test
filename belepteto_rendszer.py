from photo_album import OnlineFotoalbum

class belepteto_rendszer:
    def __init__(self):

        self._user1_nev = "user1"
        self._user1_jelszo = "pw123"

        self._user2_nev = "user2"
        self._user2_jelszo = "pw456"

        self._admin_nev = "admin"
        self._admin_jelszo = "admin123"

        self._bejelentkezett_felhasznalo = None
        self._online_fotoalbum = None

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
                self._online_fotoalbum = OnlineFotoalbum(felhasznalo)
                print(f"Sikeres belépés {felhasznalo}!")
                if felhasznalo == "admin":
                    self._kiir_jelszavak()
                break
            else:
                print("Nem megfelelő jelszó vagy felhasználónév! Kérem, próbálja újra.")

    def _kiir_jelszavak(self):
        print(f"Jelszavak:\nuser1: {self._user1_jelszo}\nuser2: {self._user2_jelszo}")

    def fotoalbum_kezelese(self):
        if self._bejelentkezett_felhasznalo:
            while True:
                print("\nFotóalbum kezelése:")
                print("1. Feltöltés új képpel")
                print("2. Képek listázása")
                print("3. Kép adatainak módosítása")
                print("4. Kilépés a fotóalbumból")

                valasztas = input("Válasszon egy opciót (1-4): ")

                if valasztas == "1":
                    self._foto_feltoltese()
                elif valasztas == "2":
                    self._kepek_listazasa()
                elif valasztas == "3":
                    self._kep_modositasa()
                elif valasztas == "4":
                    break
                else:
                    print("Érvénytelen választás. Kérem, próbálja újra.")

    def _foto_feltoltese(self):
        cim = input("Kép címe: ")
        meret = input("Kép mérete: ")
        formatum = input("Kép formátuma: ")

        eredmeny = self._online_fotoalbum.foto_feltoltes(cim, meret, formatum)
        print(eredmeny)

    def _kepek_listazasa(self):
        kepek = self._online_fotoalbum.kepek_listazasa()
        print("\nKépek listája:")
        for i, kep in enumerate(kepek, 1):
            print(f"{i}. {kep['cim']} ({kep['meret']}, {kep['formatum']})")

    def _kep_modositasa(self):
        self._kepek_listazasa()
        if self._online_fotoalbum.kepek_listazasa():
            index = int(input("Válassza ki a módosítandó képet (1-től kezdve): ")) - 1
            uj_meret = input("Új méret (hagyja üresen, ha nem akarja módosítani): ")
            uj_formatum = input("Új formátum (hagyja üresen, ha nem akarja módosítani): ")

            eredmeny = self._online_fotoalbum.kepadat_modositasa(index, uj_meret, uj_formatum)
            print(eredmeny)

# Tesztelés
rendsz = belepteto_rendszer()
rendsz.belepes()
rendsz.fotoalbum_kezelese()
