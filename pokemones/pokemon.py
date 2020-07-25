import random

class Pokemon:
    def __init__(self, nombre, tipo, ataque, vida):
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.vida = vida


class Pikachu(Pokemon):
    def __init__(self):
        super().__init__("Pikachu", "Electrico", 25, 118)
    
    def atacar(self, oponente):
        super = random.randint(1, 6)
        if super == 1:
            oponente.vida -= self.ataque * 2
            print("SUPER ATAQUE!!")
            print(f"-{self.ataque*2} de vida para {oponente.nombre}\n")
        elif oponente.tipo == "Agua":
            debilidad = random.randint(1, 4)
            if debilidad == 1:
                oponente.vida -= self.ataque * 1.5
                print(f"Golpe Critico!! -{self.ataque*1.5} de vida para {oponente.nombre}\n" )
            else:
                oponente.vida -= self.ataque
                print("-{self.ataque} de vida para {oponente.nombre}\n")
        else:
            oponente.vida -= self.ataque
            print(f"-{self.ataque} de vida para {oponente.nombre}\n")
    
    def curar(self):
        curacion = random.randint(25, 30)
        self.vida += curacion
        print(f"{self.nombre} ha recibido +{curacion} de vida\n")

class Squirtle(Pokemon):
    def __init__(self):
        super().__init__("Squirtle", "Agua", 20, 125)
    
    def atacar(self, oponente):
        super = random.randint(1, 6)
        if super == 1:
            oponente.vida -= self.ataque * 2
            print("SUPER ATAQUE!!")
            print(f"-{self.ataque*2} de vida para {oponente.nombre}\n")
        elif oponente.tipo == "Fuego":
            debilidad = random.randint(1, 4)
            if debilidad == 1:
                oponente.vida -= self.ataque * 1.5
                print(f"Golpe Critio!! -{self.ataque*1.5} de vida para {oponente.nombre}\n")
            else:
                oponente.vida -= self.ataque
                print(f"-{self.ataque} de vida para {oponente.nombre}\n")
        else:
            oponente.vida -= self.ataque
            print(f"-{self.ataque} de vida para {oponente.nombre}\n")

    def curar(self):
        curacion = random.randint(26, 30)
        self.vida += curacion
        print(f"{self.nombre} ha recibido +{curacion} de vida\n")

class Charizard(Pokemon):
    def __init__(self):
        super().__init__("Charizad", "Fuego", 32, 123)

    def atacar(self, oponente):
        super == random.randint(1, 6)
        if super == 1:
            oponente.vida -= self.ataque *2
            print("SUPER ATAQUE!!")
            print(f"-{self.ataque*2} de vida para {oponente.nombre}\n")
        elif oponente.tipo == "Tierra":
            debilidad = random.randint(1, 4)
            if debilidad == 1:
                oponente.vida -= self.ataque * 1.5
                print(f"Golpe Critico!! -{self.ataque*2} de vida para {oponente.nombre}\n")
            else:
                oponente.vida -= self.ataque
                print(f"-{self.ataque} de vida para {oponente.nombre}\n")
        else:
            oponente.vida -= self.ataque
            print(f"-{self.ataque} de vida para {oponente.nombre}\n")
    
    def curar(self):
        curacion = random.randint(22, 27)
        self.vida += curacion
        print(f"{self.nombre} ha recibido +{curacion} de vida\n")

class Golem(Pokemon):
    def __init__(self):
        super().__init__("Golem", "Tierra", 21, 134)
     
    def atacar(self, oponente):
        super = random.randint(1, 6)
        if super == 1:
            oponente.vida -= self.ataque * 2
            print("SUPER ATAQUE!!")
            print(f"-{self.ataque*2} de vida para {oponente.nombre}\n")
        elif oponente.tipo == "Electrico":
            debilidad = random.randint(1, 4)
            if debilidad == 1:
                oponente.vida -= self.ataque * 1.5
                print(f"Golpe Critico!! -{self.ataque*2} de vida para {oponente.nombre}\n")
            else:
                oponente.vida -= self.ataque
                print(f"-{self.ataque} de vida para {oponente.nombre}\n")
        else:
            oponente.vida -= self.ataque
            print(f"-{self.ataque} de vida para {oponente.nombre}\n")

    def curar(self):
        curacion = random.randint(27, 33)
        self.vida += curacion
        print(f"{self.nombre} ha recibido +{curacion} de vida\n")
