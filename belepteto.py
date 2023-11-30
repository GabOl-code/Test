class belepteto_rendszer:
    def __init__(self):
        self._user1_nev = "user1"
        self._user1_jelszo = "pw123"

        self._user2_nev = "user2"
        self._user2_jelszo = "pw456"

        self._admin_nev = "admin"
        self._admin_jelszo = "admin123"

        self._bejelentkezett_felhasznalo = None

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
        while True: # Addig kérje be a felhasználó nevet és jelszót, amíg nem OK!
            nev = input("Felhasználónév: ")
            jelszo = input("Jelszó: ")
            felhasznalo = self._ellenoriz(nev, jelszo)
            if felhasznalo:
                self._bejelentkezett_felhasznalo = felhasznalo
                print(f"Sikeres belépés {felhasznalo}!")
                if felhasznalo == "admin":
                    self._kiir_jelszavak()
                break  # Kilép a ciklusból, ha sikeres belépés történt
            else:
                print("Nem megfelelő jelszó vagy felhasználónév! Kérem, próbálja újra.")

    def _kiir_jelszavak(self):
        print(f"A felhasználók jelszavai:\nuser1: {self._user1_jelszo}\nuser2: {self._user2_jelszo}")

    @property
    def bejelentkezett_felhasznalo(self):
        return self._bejelentkezett_felhasznalo

    @bejelentkezett_felhasznalo.setter
    def bejelentkezett_felhasznalo(self, value):
        self._bejelentkezett_felhasznalo = value


# Tesztelés
rendsz = belepteto_rendszer()
rendsz.belepes()
