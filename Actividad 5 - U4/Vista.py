from tkinter import *
from tkinter import ttk, messagebox
from Paciente import Paciente

class Vista(Tk):
    def __init__(self):
        super().__init__()
        self.title("Lista de Pacientes")
        self.resizable(False,False)
        self.list = ListaPacientes(self, height=15)
        self.form = UpdateFormularioPaciente(self)
        self.btn_new = ttk.Button(self, text ="Agregar Paciente")
        self.list.pack(side=LEFT, padx =10, pady = 10)
        self.form.pack(padx = 10, pady = 10 )
        self.btn_new.pack(side=BOTTOM, pady = 3 )#tipo de posicionamiento que ajusta todo los elementos acomodándolos entre sí, para luego hacer la ventana raíz tan grande para contener todos estos elementos.

        self.config(background = "#E4E8D1")

    def setControlador(self, ctrl):
        # vincula la vista con el controlador
        self.btn_new.config(command=ctrl.crearPaciente)
        self.list.bind_doble_click(ctrl.seleccionarPaciente)
        self.form.bind_save(ctrl.modificarPaciente)
        self.form.bind_delete(ctrl.borrarPaciente)
        self.form.bind_view(ctrl.viewIMC)

    def agregarPaciente(self, paciente):
        self.list.insertar(paciente)

    def verIMC(self, imc, info):
        self.imc = verIMC(self, imc, info)

    def modificarPaciente(self, paciente, index):
        self.list.modificar(paciente, index)

    def borrarPaciente(self, index):
        self.form.limpiar()
        self.list.borrar(index)
        # obtiene los valores del formulario y crea un nuevo paciente

    def obtenerDetalles(self):
        return self.form.crearPacienteDesdeFormulario()
        # Ver estado de Paciente en formulario de pacientes

    def verPacienteEnForm(self, paciente):
        self.form.mostrarEstadoPacienteEnFormulario(paciente)




class ListaPacientes(Frame):
     def __init__(self, master, **kwargs):
         super().__init__(master)
         self.lb = Listbox(self, **kwargs)
         scroll = Scrollbar(self, command=self.lb.yview)
         self.lb.config(yscrollcommand=scroll.set)
         scroll.pack(side=RIGHT, fill=Y)
         self.lb.pack(side=LEFT, fill=BOTH, expand=1)
         
     def insertar(self, paciente, index=END):
         text = "{}, {}".format(paciente.getApellido(), paciente.getNombre())
         self.lb.insert(index, text)
         
     def borrar(self, index):
         self.lb.delete(index, index)
         
     def modificar(self, pacient, index):
         self.borrar(index)
         self.insertar(pacient, index)
         
     def bind_doble_click(self, callback):
         handler = lambda _: callback(self.lb.curselection()[0])
         self.lb.bind("<Double-Button-1>", handler)

class FormularioPaciente(ttk.Frame):
    fields = ("Apellido", "Nombre", "Teléfono","Altura","Peso")
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.frame   = ttk.Frame(self)
        self.titulo  = ttk.Label(self.frame,text="PACIENTE",style="BW.TLabel",anchor=E,background="#E4E8D1")
        self.titulo.grid(columnspan=2,pady=3,padx=3,ipadx=10)
        self.entries = list(map(self.crearCampo, enumerate(self.fields)))
        self.frame.pack()



        style = ttk.Style()
        style.configure("TLabelframe", background="#fff")
        style.configure("BW.TLabel",  background="#fff", font=("Times New Roman",23), foreground="black")
        style.configure("TLabel" ,  background="#fff", font=("Corbel",15),foreground="#086972" )
        style.configure("TFrame" , background="#fff")
        style.configure("TEntry", padding = 6)

    def crearCampo(self, field):
        position, text = field
        label = ttk.Label(self.frame, text=text)
        entry = ttk.Entry(self.frame, width=25)

        label.grid(row=position+1, column=0, pady=10, padx = 5)
        entry.grid(row=position+1, column=1, pady=5, padx = 5)
        return entry

    def mostrarEstadoPacienteEnFormulario(self, paciente):
        # a partir de un paciente, obtiene el estado
        # y establece en los valores en el formulario de entrada
        values = (paciente.getApellido(), paciente.getNombre(),
                  paciente.getTelefono(), paciente.getAltura(), paciente.getPeso())
        for entry, value in zip(self.entries, values):
            entry.delete(0, END)
            entry.insert(0, value)

    def crearPacienteDesdeFormulario(self):
        values   = [e.get() for e in self.entries]
        paciente = None
        try:
            float(values[3])
            float(values[4])
            if '' not in values :
                try:
                    paciente = Paciente(*values)
                except ValueError as e:
                    messagebox.showerror("Error de Validación", str(e), parent=self)
                return paciente
        except:
            pass

    def limpiar(self):
        for entry in self.entries:
            entry.delete(0, END)

class NuevoPaciente(Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.resizable(False, False)
        self.paciente = None
        self.form = FormularioPaciente(self)
        style = ttk.Style()
        style.configure("TFrame", background="#fff")
        self.btn_add  = ttk.Button(self, text="Confirmar",command=self.confirmar)
        self.form.pack(padx=10, pady=10)
        self.btn_add.pack(pady=10)

    def confirmar(self):
        self.paciente = self.form.crearPacienteDesdeFormulario()
        if self.paciente:
            self.destroy()

    def show(self):
        self.grab_set()
        self.wait_window()
        return self.paciente

class verIMC(Toplevel):
    def __init__(self, parent, imc, info):
        super().__init__(parent)
        self.resizable(False,False)
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack()
        self.label1 = ttk.Label(self.mainFrame, text = "IMC: ")
        self.label2 = ttk.Label(self.mainFrame, text = imc)
        self.label3 = ttk.Label(self.mainFrame, text="Composicion Corporal: ")
        self.label4 = ttk.Label(self.mainFrame, text=info)
        style = ttk.Style()
        opcs = {"ipadx" : 8, "ipady" : 8, "pady" : 4, "padx" : 4}

        self.label1.grid(column=0, row=0, **opcs)
        self.label2.grid(column=1, row=0, **opcs)
        self.label3.grid(column=0, row=1, **opcs)
        self.label4.grid(column=1, row=1, **opcs)
        self.grab_set()
        self.wait_window()
        


class UpdateFormularioPaciente(FormularioPaciente):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        opcs = {"ipadx": 5, "padx": 5, "pady": 15}
        style = ttk.Style()

        style.configure("TLabel", **opcs)
        style.configure("TButton", background="green", width=20, padding=10 )

        self.btn_save   = ttk.Button(self, text = "Guardar")
        self.btn_delete = ttk.Button(self, text = "Borrar" )
        self.btn_view   = ttk.Button(self, text = "Ver IMC")

        self.btn_save   .pack(side=RIGHT,**opcs)
        self.btn_delete .pack(side=RIGHT,**opcs)
        self.btn_view   .pack(side=RIGHT, **opcs)

    def bind_save(self, callback):
        self.btn_save.config(command=callback)
    def bind_delete(self, callback):
        self.btn_delete.config(command=callback)
    def bind_view(self, callback):
        self.btn_view.config(command=callback)
        
