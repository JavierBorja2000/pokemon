from pokemones.pokemon import Pikachu, Charizard, Golem, Squirtle

#Instrucciones
def instrucciones():
    print(f"""
    INSTRUCCIONES:
    1. El juego termina cuando la vida de un Pokemon llegue a "0"
    2. La oportunidad de tu Pokemon de dar un "Golpe Critico" dependera del tipo de elemento de tu oponente
       (El tipo de elemento de tu Pokemon importa!) "ELIGUE BIEEEN"
    3. Puedes sorprender a tu oponente con un "SUPER ATAQUE" de vez en cuando
    4. Si un jugador eligue la opcion: "Huir", el otro ganara automaticamente""")

def menu1():
    print("  :SELECCIONE SU PERSONAJE:")
    print("1. Pikachu (Tipo: Electrico)")
    print("2. Squirtle (Tipo: Agua)")
    print("3. Golem (Tipo: Tierra)")
    print("4. Charizard (Tipo: Fuego)\n")
    while True:
        opcion = input("Eliga su personaje (1-4): ")
        if opcion == "1" or opcion == "2" or opcion == "3" or opcion == "4":
            break
        print("Error, escoja un numero en el rango de 1 a 4")
        continue
    return opcion

def seleccionar_personaje(opcion):
    if opcion == "1":
        pikachu = Pikachu()
        return pikachu 
    elif opcion == "2":
        squirtle = Squirtle()
        return squirtle
    elif opcion == "3":
        golem = Golem()
        return golem
    elif opcion == "4":
        charizard = Charizard()
        return charizard

def menu2():
    print("Que Accion quiere ejecutar....")
    print("1. Atacar")
    print("2. Curar")
    print("3. Huir")
    while True:
        accion = input("INGRESE SU OPCION (1-3): ")
        if accion == "1" or accion == "2" or accion == "3":
            break
        else:
            print("No se haga el chistoso es solo del (1-3) :)")
    return accion

def verificar_vida(jugador, pokemon):
    if pokemon.vida <= 0:
        print(f"GANADOR: {jugador}")
        return False
    else:
        return True

def estado_actual(p1, j1, p2, j2):
    print(f"""
              :Resultados:
      {j1} con:    {j2} con:
        {p1.nombre}       {p2.nombre}
        Ataque: {p1.ataque}     Ataque: {p2.ataque}
        Vida: {p1.vida}      Vida: {p2.vida}
        
        """)
