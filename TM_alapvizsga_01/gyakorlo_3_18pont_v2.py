class csoki:
    def __init__(self, fajta, kiszereles, csomag) -> None:
        self.tipus = fajta
        self.tomeg = kiszereles
        self.csomagolas = csomag

    def ar(self):
        arr = self.tomeg*3
        if self.csomagolas == "papír":
            arr = arr + 100
        if self.csomagolas == "doboz":
            arr = arr + 500

        return arr

