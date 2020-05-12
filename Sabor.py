class Sabor:
    __num = int
    __nom = str
    __des = str
    def __init__(self, num, nom, des):
        self.__num = num
        self.__nom = nom
        self.__des = des
    def getnum(self):
        return int(self.__num)
    def getnom(self):
        return str(self.__nom)
    def getdes(self):
        return str(self.__des)