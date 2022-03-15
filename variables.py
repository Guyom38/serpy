class homme():
    def __init__(self, _nom, _age):
        self.nom = _nom
        self.age = _age

    def parler(self):
        print("Salut, je m'appelle " + self.nom)

    def age(self):
        return self.age


soldat1 = homme("Guillaume", 37)
soldat2 = homme("Robert", 99)

soldat1.parler()
soldat2.parler()

print("L'age du soldat 1 est ", soldat1.age, " ans.")
print("L'age du soldat 2 est ", soldat2.age, " ans.")
