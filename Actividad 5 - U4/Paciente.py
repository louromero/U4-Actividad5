import pathlib


class Paciente:
    __nombre=''
    __apellido=''
    __telefono=0
    __altura=0.00
    __peso=0.00

    def __init__(self,nombre,apellido,telefono,altura,peso):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__telefono=telefono
        self.__altura=altura
        self.__peso=peso

    #GETTERS
    def getNombre(self):
        return self.__nombre

    def getApellido(self):
        return self.__apellido

    def getTelefono(self):
        return self.__telefono

    def getAltura(self):
        return self.__altura

    def getPeso(self):
        return self.__peso

    #JSON
    def toJson(self):
        d = dict(__class__=self.__class__.__name__,
                 __atributos__=dict(
                     nombre   = self.getNombre(),
                     apellido = self.getApellido(),
                     telefono = self.getTelefono(),
                     altura   = self.getAltura(),
                     peso     = self.getPeso()
                 ))

        return d

    def __str__(self):
        return "{} {} {} {} {}".format(self.getNombre(),self.getApellido(),self.getTelefono(),self.getAltura(),self.getPeso())