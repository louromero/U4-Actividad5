import json
from pathlib import Path
from Modelo import Modelo
from Paciente import Paciente

class ObjectEncoder:
    
    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
        destino.close()

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
        class_ = eval(class_name)
        if class_name == 'Modelo':
            lista = d['Pacientes']
        manejador = class_()

        for i in range(len(lista)):
            dPaciente  = lista[i]
            class_name = dPaciente.pop('__class__')
            class_     = eval(class_name)
            atributos  = dPaciente['__atributos__']

            unPaciente = class_(**atributos)
            manejador.agregarPaciente(unPaciente)
        return manejador

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
        fuente.close()
        return diccionario