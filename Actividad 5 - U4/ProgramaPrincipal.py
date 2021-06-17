from Controlador import Controlador
from Repositorio import Repositorio
from Vista import Vista
from ObjectEncoder import ObjectEncoder

if __name__=="__main__":
    objectEncoder=ObjectEncoder()
    repositorio= Repositorio(objectEncoder)
    app=Vista()
    controlador=Controlador(repositorio,app)
    app.setControlador(controlador)
    controlador.start()
    controlador.salirGrabarDatos()
