from Vista import NuevoPaciente


class Controlador(object):
    def __init__(self, repo, vista):
        self.repo = repo
        self.vista = vista
        self.seleccion = -1
        self.pacientes = list(repo.obtenerListaPacientes())
        # comandos de que se ejecutan a través de la vista

    def crearPaciente(self):
        nuevoPaciente = NuevoPaciente(self.vista).show()
        if nuevoPaciente:
            paciente  = self.repo.agregarPaciente(nuevoPaciente)
            self.pacientes.append(paciente)
            self.vista.agregarPaciente(paciente)

    def seleccionarPaciente(self, index):
        self.seleccion = index
        paciente = self.pacientes[index]
        self.vista.verPacienteEnForm(paciente)

    def modificarPaciente(self):
        if self.seleccion==-1:
            return
        detallesPaciente = self.vista.obtenerDetalles()

        if detallesPaciente != None:
            paciente = self.repo.modificarPaciente(detallesPaciente, self.seleccion)
            self.pacientes[self.seleccion] = paciente
            self.vista.modificarPaciente(paciente, self.seleccion)
            self.seleccion = -1
        
    def borrarPaciente(self):
        if self.seleccion==-1:
            return
        paciente= self.pacientes[self.seleccion]
        self.repo.borrarPaciente(paciente)
        self.pacientes.pop(self.seleccion)
        self.vista.borrarPaciente(self.seleccion)
        self.seleccion  = -1

    def viewIMC(self):
        paciente = self.pacientes[self.seleccion]
        kilos = float(paciente.getPeso())
        altura = float(paciente.getAltura())
        imc = kilos / ((altura / 100) *(altura/100))
        if imc < 18.5:
            info = "Peso inferior al normal"
        elif imc > 18.5 and imc < 24.9:
            info = "Peso normal"
        elif imc > 25 and imc < 29.9:
            info = "Peso superior al normal"
        else:
            info = "Obesidad"
        imc = "{:.2f}".format(imc)
        self.vista.verIMC(imc, info)

    def start(self):
        for c in self.pacientes:
            self.vista.agregarPaciente(c)
        self.vista.mainloop()

    def salirGrabarDatos(self):
        self.repo.grabarDatos()

