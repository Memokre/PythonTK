import math

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

class Kruh(Tvar):
    def __init__(self, polomer=0):
        super().__init__()
        self.polomer = polomer
        print("Vytváram kruh")

    def obvod(self):
        return 2 * math.pi * self.polomer

    def obsah(self):
        return math.pi * self.polomer ** 2

    def ziskaj_polomer(self):
        return self.polomer

    def info(self):
        print(f"Kruh s polomerom {self.polomer}")

class Valcek(Kruh):
    def __init__(self, polomer=0, vyska=0):
        super().__init__(polomer)
        self.vyska = vyska
        print("Vytváram valček")

    def objem(self):
        return math.pi * self.ziskaj_polomer() ** 2 * self.vyska

    def info(self):
        print(f"Valček s polomerom {self.ziskaj_polomer()} a výškou {self.vyska}")

class Gula(Kruh):
    def __init__(self, polomer=0):
        super().__init__(polomer)
        print("Vytváram guľu")

    def objem(self):
        return (4 / 3) * math.pi * self.ziskaj_polomer() ** 3

    def info(self):
        print(f"Guľa s polomerom {self.ziskaj_polomer()}")

if __name__ == "__main__":
    rec = Obdlznik()
    rec1 = Obdlznik(5, 6)
    kc = Kocka(5)
    print(kc.objem())
    kc.info()

    kr = Kruh(3)
    print(kr.obvod())
    print(kr.obsah())
    kr.info()

    val = Valcek(3, 4)
    print(val.objem())
    val.info()

    gul = Gula(2)
    print(gul.objem())
    gul.info()