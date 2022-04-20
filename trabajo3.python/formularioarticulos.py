import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos, cliente

class FormArticulos:
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.cliente1=cliente.Cliente()

        self.ventana1=tk.Tk()
        self.ventana1.title("Articulos")
        self.cuaderno1 = ttk.Notebook(self.ventana1)        
        
        self.consulta_por_codigo()
        self.listado_completo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()
        
        
    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código/Sku")

        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Artículo")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)

        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)

        self.label2=ttk.Label(self.labelframe2, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe2, textvariable=self.nombre, state="readonly")
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe2, text="Descripción:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=2, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos = (self.codigo.get(), )
        respuesta= self.articulo1.consulta(datos)
        if len(respuesta)>0:
            self.nombre.set(respuesta[0][0])
            self.descripcion.set(respuesta[0][1])
        else:
            self.nombre.set("")
            self.descripcion.set("")
            mb.showinfo("Información", "No existe un articulo con el código suministrado")
    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Ventas de cliente")
 
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Datos del cliente")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
 
        self.label4=ttk.Label(self.labelframe3, text="RUT:")
        self.label4.grid(column=0, row=0, padx=4, pady=4)
 
        self.rutcliente=tk.StringVar()
        self.entryrut=ttk.Entry(self.labelframe3, textvariable=self.rutcliente)
        self.entryrut.grid(column=1, row=0, padx=4, pady=4)
        self.idcliente = 0
 
        self.label5=ttk.Label(self.labelframe3, text="Nombre:")        
        self.label5.grid(column=0, row=1, padx=4, pady=4)
        self.nombrecliente=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe3, textvariable=self.nombrecliente, state="readonly")
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
 
        self.label6=ttk.Label(self.labelframe3, text="Apellido:")        
        self.label6.grid(column=0, row=2, padx=4, pady=4)
        self.apellidocliente=tk.StringVar()
        self.entryapellido=ttk.Entry(self.labelframe3, textvariable=self.apellidocliente, state="readonly")
        self.entryapellido.grid(column=1, row=2, padx=4, pady=4)

        self.label7=ttk.Label(self.labelframe3, text="Apellido M:")        
        self.label7.grid(column=0, row=3, padx=4, pady=4)
        self.apellidocliente2=tk.StringVar()
        self.entryapellido2=ttk.Entry(self.labelframe3, textvariable=self.apellidocliente2, state="readonly")
        self.entryapellido2.grid(column=1, row=3, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe3, text="Recuperar ventas", command=self.consultarcliente)
        self.boton1.grid(column=0, row=5, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=4, padx=10, pady=10)
 
    def consultarcliente(self):
        datosrut = (self.rutcliente.get(),)
        datosrut2 = datosrut[0]
        mantisa = datosrut2[:-1]
        respuesta1= self.cliente1.consulta(mantisa)
        if len(respuesta1)>0:
            self.idcliente = (respuesta1[0][0])
            self.nombrecliente.set(respuesta1[0][1])
            self.apellidocliente.set(respuesta1[0][2])
            self.apellidocliente2.set(respuesta1[0][3])
            self.listarventas(self.idcliente)
        else:
            self.nombre.set("")
            self.descripcion.set("")
            mb.showinfo("Información", "No existe el cliente con RUT suministrado")
 
    def listarventas(self, idcliente):
        respuesta=self.cliente1.recuperar_datos(idcliente)
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "Fecha: "+str(fila[1])+"\nCantidad:"+str(fila[2])+"\nProducto:"+str(fila[3])+"\nTotal:"+str(fila[4])+"\n\n")
    
aplicacion1=FormArticulos()