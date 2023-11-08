class Kutya:
    pass

    def __init__(self, nev, kor, fajta):
        self.nev = nev
        self.kor = kor
        self.fajta = fajta

    def emberi_evekben(self):

        if self.fajta == 'tacskó':
            emberi_ev = self.kor * 8
        else:
            emberi_ev = self.kor * 7

        return emberi_ev




