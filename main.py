class Character:
    def __init__(self, ad, saglamliq, hujum):
        self.ad = ad
        self.saglamliq = saglamliq
        self.hujum = hujum

    def attack(self, other):
        other.take_damage(self.hujum)

    def take_damage(self, damage):
        self.saglamliq -= damage
        if self.saglamliq < 0:
            self.saglamliq = 0

    def __str__(self):
        return f"{self.ad} - Sağlamlıq: {self.saglamliq}, Hücum: {self.hujum}"

    def __add__(self, other):
        return f"{self.ad} + {other.ad} komandası"

    def __lt__(self, other):
        return self.saglamliq < other.saglamliq

    def __eq__(self, other):
        return self.ad == other.ad and self.saglamliq == other.saglamliq

    def __len__(self):
        return self.saglamliq

    def __bool__(self):
        return self.saglamliq > 0


# Döyüşçü
class Warrior(Character):
    def __init__(self, ad, saglamliq, hujum, zireh):
        super().__init__(ad, saglamliq, hujum)
        self.zireh = zireh

    def attack(self, other):
        print(self.ad, "qılıncla hücum edir!")
        other.take_damage(self.hujum)


# Sehrbaz
class Mage(Character):
    def __init__(self, ad, saglamliq, hujum, mana):
        super().__init__(ad, saglamliq, hujum)
        self.mana = mana

    def attack(self, other):
        print(self.ad, "sehr ilə hücum edir!")
        other.take_damage(self.hujum + 10)
        self.mana -= 10


# Oxçu
class Archer(Character):
    def __init__(self, ad, saglamliq, hujum, ox_sayi):
        super().__init__(ad, saglamliq, hujum)
        self.ox_sayi = ox_sayi

    def attack(self, other):
        print(self.ad, "ox atır!")
        if self.ox_sayi > 0:
            other.take_damage(self.hujum)
            self.ox_sayi -= 1


# Personajların yaradılması
warrior = Warrior("Ali", 100, 20, 10)
mage = Mage("Murad", 80, 25, 50)
archer = Archer("Kamran", 90, 15, 10)


# Məlumatları ekrana çıxarmaq
print(warrior)
print(mage)
print(archer)

print()


# Polimorfizm
personajlar = [warrior, mage, archer]

for personaj in personajlar:
    personaj.attack(warrior)

print()

# Müqayisə
print(warrior < mage)
print(warrior == mage)

# __len__
print("Warrior sağlamlığı:", len(warrior))

# __bool__
if warrior:
    print("Warrior sağdır.")
else:
    print("Warrior ölüdür.")

# __add__
print(warrior + mage)

# Hücum
mage.attack(archer)

print(archer)
