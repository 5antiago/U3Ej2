from manejahelados import manejahelados
from Helado import Helado
from manejasabores import manejasabores
from Sabor import Sabor
class Menu:
    __switcher = dict
    def __init__(self):
        self.__switcher = {1: self.vender, 2: self.masvendidos, 3: self.gramosvendidos, 4:self.saboresvendidos}
    def opcion(self, op, helados, sabores):
        self.__switcher.get(op)(helados, sabores)
    def vender(self, helados, sabores ):
        helado = Helado(int(input("Ingrese la cantidad de Gramos: ")))
        op = int(input("Ingrese Codigo de sabor (0.Salir): "))
        while op > 0:
            helado.agregarsabor(sabores.buscarsabor(op))
            op = int(input("Ingrese Codigo de sabor (0. Terminar): "))
        helados.agregarhelado(helado)
        del helado
    def masvendidos(self, helados, sabores):
        print(helados.saboresmaspedidos(sabores))
    def gramosvendidos(self,helados, sabores):
        print("Se vendieron: {}".format(helados.estimarsabores(int(input("Ingrese el codigo de sabor: ")))))
    def saboresvendidos(self, helados, sabores):
        for sabor in helados.saboresporgramos(int(input("Ingrese cantidad de Gramos: "))):
            print("- {}".format(sabor.getnom()))


