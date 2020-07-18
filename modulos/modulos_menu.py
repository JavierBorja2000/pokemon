from pokemones.pikachu import Pikachu

#Instrucciones
def instrucciones():
    print(f"""
    INSTRUCCIONES:
    1. El juego termina cuando la vida de un Pokemon llegue a "0"
    2. Los Tipos de elemento de tu Pokemon pueden sufrir mas dependiendo del elemento de tu oponente
       asi que: ELIGUE BIEN!!!
    3. Si un jugador eligue la opcion: "Huir", el otro ganara automaticamente""")

def menu1():
    print("SELECCIONE SU PERSONAJE:")
    print("1. Pikachu (Tipo: Electrico)")
    print("2. Squirtle (Tipo: Agua)")
    print("3. Golem (Tipo: Tierra)")
    print("4. Charizad (Tipo: Fuego)")
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
    elif opcion == "2":
        charizard = Charizard()
        return charizard