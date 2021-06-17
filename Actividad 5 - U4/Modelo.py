class Modelo:

    __modelo = []

    def __init__(self,model = []):
        self.__modelo = model

    def agregarPaciente(self, paciente):
        self.__modelo.append(paciente)
    
    def borrarPaciente(self, paciente):
        self.getListaPaciente().remove(paciente)

    def updatePaciente(self, paciente, ind):
        self.getListaPaciente()[ind] = paciente




    def toJson(self):
        d = dict(
            __class__=self.__class__.__name__,
            Pacientes=[Pacientes.toJson() for Pacientes in self.__modelo]
        )
        return d

    def getListaPaciente(self):
        return self.__modelo

    def __str__(self):
        lista = []
        for x in self.getLista():
            lista.append(str(x))
        return str(lista)

    def getPaciente(self, ind):
        return self.getListaPaciente()[ind]