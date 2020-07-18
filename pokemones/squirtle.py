from pokemon import Pokemon

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "Agua", 20, 125)
    
    def atacar(self, oponente):
        pass
    def curar(self):
        pass
    def __str__(self):
        return f"{self.get_nombre()}, Tipo: {self.get_tipo()}\nAtaque: {self.get_ataque()}, Vida: {self.get_HP()} HP"

#e = Squirtle()
#print(e)