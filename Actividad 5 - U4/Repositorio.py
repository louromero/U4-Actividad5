from Paciente import Paciente
from ObjectEncoder import ObjectEncoder
from Vista import Vista #Modelo


class Repositorio(object):
    __conn=None
    __manejador=None

    def __init__(self,conn):
        self.__conn=conn
        diccionario=self.__conn.leerJSONArchivo('pacientes.json')
        self.__manejador=self.__conn.decodificarDiccionario(diccionario)

    def to_value(self,paciente):
        return paciente.getApellido(), paciente.getNombre(), paciente.getTelefono(),paciente.getAltura(),paciente.getPeso()

    def obtenerListaPacientes(self):
        return self.__manejador.getListaPaciente()

    def agregarPaciente(self,paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente

    def modificarPaciente(self, paciente, ind):
        self.__manejador.updatePaciente(paciente, ind)
        return paciente

    def borrarPaciente(self,paciente):
        self.__manejador.borrarPaciente(paciente)

    def grabarDatos(self):
        diccionario=self.__manejador.toJson()
        self.__conn.guardarJSONArchivo(diccionario,'pacientes.json')