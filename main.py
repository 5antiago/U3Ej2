import csv
from Sabor import Sabor
from Helado import Helado
from manejasabores import manejasabores
from manejahelados import manejahelados
from menu import Menu



if __name__ == "__main__":
    Helados = manejahelados()
    Sabores = manejasabores()
    menu = Menu()
    with open("Sabores.csv") as f:
        reader = csv.reader(f, delimiter=",")
        for row in reader:
            Sabores.agregarsabor(Sabor(row[0], row[1], row[2]))
        
    print(" 1. Vender Helado\n 2. Sabores mas vendidos\n 3. Gramos de Sabor Vendido\n 4. Sabores vendidos por tipo de helado")
    op = int(input("Ingrese opcion: "))
    while op > 0:
        menu.opcion(op, Helados, Sabores)
        print(" 1. Vender Helado\n 2. Sabores mas vendidos\n 3. Gramos de Sabor Vendido\n 4. Sabores vendidos por tipo de helado")
        op = int(input("Ingrese opcion: "))