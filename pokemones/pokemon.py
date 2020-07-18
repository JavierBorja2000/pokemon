from abc import ABC, abstractclassmethod

class Pokemon(ABC):
    def __init__(self, nombre, tipo, ataque, vida):
        self.__nombre = nombre
        self.__tipo = tipo
        self.__ataque = ataque
        self.__HP = vida
    
    @abstractclassmethod
    def atacar(self, oponente):
        pass
    
    @abstractclassmethod
    def curar(self):
        pass
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self, tipo):
        self.__tipo = tipo
    def get_ataque(self):
        return self.__ataque
    def set_ataque(self, ataque):
        self.__ataque = ataque
    def get_HP(self):
        return self.__HP
    def set_HP(self, vida):
        self.__HP = vida