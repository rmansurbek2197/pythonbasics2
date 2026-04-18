class Kitob:
    def __init__(self, nomi, muallifi, narxi):
        self.nomi = nomi
        self.muallifi = muallifi
        self.narxi = narxi
        self.holati = "Erkin"

class Foydalanuvchi:
    def __init__(self, ismi, familiyasi):
        self.ismi = ismi
        self.familiyasi = familiyasi
        self.kitoblar = []

class Kitobxona:
    def __init__(self):
        self.kitoblar = []
        self.foydalanuvchilar = []

    def kitob_qo_sh(self, kitob):
        self.kitoblar.append(kitob)

    def foydalanuvchi_qo_sh(self, foydalanuvchi):
        self.foydalanuvchilar.append(foydalanuvchi)

    def kitob_ol(self, foydalanuvchi, kitob):
        if kitob.holati == "Erkin":
            kitob.holati = "Borilmoqda"
            foydalanuvchi.kitoblar.append(kitob)
        else:
            print("Kitob borilmoqda")

    def kitob_qaytar(self, foydalanuvchi, kitob):
        if kitob in foydalanuvchi.kitoblar:
            foydalanuvchi.kitoblar.remove(kitob)
            kitob.holati = "Erkin"
        else:
            print("Sizda bunday kitob yo'q")

kitobxona = Kitobxona()
kitob1 = Kitob("Olma", "Jaloliddin", 10000)
kitob2 = Kitob("Anor", "Farrux", 15000)
foydalanuvchi1 = Foydalanuvchi("Ali", "Valiyev")
foydalanuvchi2 = Foydalanuvchi("Vali", "Aliyev")

kitobxona.kitob_qo_sh(kitob1)
kitobxona.kitob_qo_sh(kitob2)
kitobxona.foydalanuvchi_qo_sh(foydalanuvchi1)
kitobxona.foydalanuvchi_qo_sh(foydalanuvchi2)

kitobxona.kitob_ol(foydalanuvchi1, kitob1)
kitobxona.kitob_ol(foydalanuvchi2, kitob2)
kitobxona.kitob_qaytar(foydalanuvchi1, kitob1)

class BorLog:
    def __init__(self):
        self.log = []

    def qo_sh(self, foydalanuvchi, kitob, sana):
        self.log.append((foydalanuvchi, kitob, sana))

borlog = BorLog()
borlog.qo_sh(foydalanuvchi1, kitob1, "2024-02-20")
borlog.qo_sh(foydalanuvchi2, kitob2, "2024-02-21")

class QaytarLog:
    def __init__(self):
        self.log = []

    def qo_sh(self, foydalanuvchi, kitob, sana):
        self.log.append((foydalanuvchi, kitob, sana))

qaytarlog = QaytarLog()
qaytarlog.qo_sh(foydalanuvchi1, kitob1, "2024-02-25")
qaytarlog.qo_sh(foydalanuvchi2, kitob2, "2024-02-26")