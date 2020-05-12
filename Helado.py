from Sabor import Sabor
class Helado:
    __gramos = int
    __sabores = list

    def __init__(self, gramos):
        self.__gramos = gramos
        self.__sabores = []
    def getgramos(self):
        return int(self.__gramos)
    def getsabores(self):
        return self.__sabores
    def agregarsabor(self, sabor):
        if type(sabor) == Sabor:
            self.__sabores.append(sabor)