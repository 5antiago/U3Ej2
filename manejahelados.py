from manejasabores import Sabor
from Helado import Helado
from Sabor import Sabor

class manejahelados(object):
    __Helados = list

    def __init__(self):
        self.__Helados = []
    def agregarhelado(self, helado):
        if type(helado) == Helado:
            self.__Helados.append(helado)
    def saboresporgramos(self, gramos):
        cont = []
        for helado in self.__Helados:
            if helado.getgramos() == int(gramos):
                for sabor in helado.getsabores():
                    if sabor not in cont:
                        cont.append(sabor)
        return cont
    def saboresmaspedidos(self, sabores):
        listavendidos = [0 for x in range(sabores.cantdesabores())]
        for helado in self.__Helados:
            for sabor in helado.getsabores():
                listavendidos[sabor.getnum()-1] += 1
        aux = ""
        for __ in range(5):
            h=int(listavendidos.index(max(listavendidos)))
            aux += "Sabor {} cantidad: {}  \n".format(sabores.buscarsabor(h+1).getnom(), listavendidos[h])
            listavendidos[h]=-1
        return aux
    def estimarsabores(self, cod):
        acum = 0
        for helado in self.__Helados:
            for sabor in helado.getsabores():
                if cod == sabor.getnum():
                    acum += helado.getgramos() / len(helado.getsabores())
        return acum