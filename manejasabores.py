from Sabor import Sabor
from Helado import Helado

class manejasabores:
    __sabores = list 

    def __init__(self):
        self.__sabores = []
    def agregarsabor(self, sabor):
        if type(sabor) == Sabor:
            self.__sabores.append(sabor)
    def buscarsabor(self, cod):
        i = 0
        while i<len(self.__sabores) and self.__sabores[i].getnum() != int(cod):
            i += 1 
            
        if i <= len(self.__sabores):
            return self.__sabores[i]
    def cantdesabores(self):
        return len(self.__sabores)
    