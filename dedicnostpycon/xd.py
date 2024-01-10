class Tvar:
    def __init__(self):
        print("Vykresľujem tvar")

class Stvorec(Tvar):
    def __init__(self, a=0):
        super().__init__()
        self.a = a
        print("Vytváram štvorec")

    def obvod(self):
        return self.a * 4

    def obsah(self):
        return self.a * self.a

    def ziskaj_a(self):
        return self.a

    def info(self):
        print(f"Štvorec so stranou dĺžky {self.a}")

class Obdlznik(Stvorec):
    def __init__(self, a=0, b=0):
        super().__init__(a)
        self.b = b
        print("Vytváram obdĺžnik")

    def obvod(self):
        return 2 * self.b + 2 * self.ziskaj_a()

    def obsah(self):
        return self.b * self.ziskaj_a()

    def info(self):
        print(f"Obdĺžnik so stranou dĺžky {self.ziskaj_a()} a druhou stranou dĺžky {self.b}")

class Kocka(Stvorec):
    def __init__(self, a=0):
        super().__init__(a)
        print("Vytváram kocku")

    def objem(self):
        return self.obsah() * self.ziskaj_a()

    def info(self):
        print(f"Kocka so stranami dĺžky {self.ziskaj_a()}")

if __name__ == "__main__":
    rec = Obdlznik()
    rec1 = Obdlznik(5, 6)
    kc = Kocka(5)
    print(kc.objem())
    kc.info()
