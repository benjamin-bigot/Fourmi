class Salle:
    def __init__(self, nom, taille):
        self.nom = nom
        self.fourmi = 0
        self.taille = taille
        self.connexion = []

    def is_full(self):
        if self.fourmi < self.taille:
            return False
        return True

    def set_connexion(self, salle):
        self.connexion.append(salle.nom)

    def add_fourmi(self):
        self.fourmi += 1

    def remove_fourmi(self):
        self.fourmi -= 1


class Fourmi:
    def __init__(self, nom):
        self.nom = nom
        self.position = None

    def init_position(self, Sv):
        self.position = Sv.nom

    def move(self, start, end):
        if end.is_full() is False:
            start.remove_fourmi()
            end.add_fourmi()
            print(self.nom + " - " + start.nom + " - " + end.nom)
        else:
            print("Salle pleine")


class Fourmilliere:
    def __init__(self):
        self.graphe_salles = {}
        self.pos_fourmi = {}

    def add_fourmi(self, f):
        self.pos_fourmi[f.position].append(f.nom)

    def add_salle(self, salle):
        self.graphe_salles[salle.nom] = salle.connexion
        self.pos_fourmi[salle.nom] = list()

    def display(self):
        print(self.graphe_salles)

    #def solve(self):


Sv = Salle('Sv', 10)
S1 = Salle('S1', 1)
S2 = Salle('S2', 1)
S3 = Salle('S3', 2)
S4 = Salle('S4', 1)
S5 = Salle('S5', 3)
Sd = Salle('Sd', 10)

Sv.set_connexion(S1)
Sv.set_connexion(S2)
Sv.set_connexion(S3)
S1.set_connexion(S4)
S3.set_connexion(S5)
S5.set_connexion(Sd)
S2.set_connexion(Sd)
S4.set_connexion(Sd)

F = Fourmilliere()
F.add_salle(Sv)
F.add_salle(S1)
F.add_salle(S2)
F.add_salle(S3)
F.add_salle(S4)
F.add_salle(S5)
F.add_salle(Sd)
F.display()

f1 = Fourmi('f1')
f1.init_position(Sv)
F.add_fourmi(f1)
f2 = Fourmi('f2')
f2.init_position(Sv)
F.add_fourmi(f2)
f3 = Fourmi('f3')
f3.init_position(Sv)
F.add_fourmi(f3)
f4 = Fourmi('f4')
f4.init_position(Sv)
F.add_fourmi(f4)
f5 = Fourmi('f5')
f5.init_position(Sv)
F.add_fourmi(f5)
f6 = Fourmi('f6')
f6.init_position(Sv)
F.add_fourmi(f6)

print(F.pos_fourmi)

