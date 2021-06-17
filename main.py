# coding=utf-8
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sqlite3

# -----------------------clases---------------------------------------
class UI(tk.Frame):
    def __init__(self, parent=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        self.parent.title("Gestion de dispositivos")
# ---------------------funciones---------------------------------------

# noinspection PyBroadException
def conexion_bbdd():
    mi_conexion = sqlite3.connect("Dispositivos")

    mi_cursor = mi_conexion.cursor()

    try:
        mi_cursor.execute('''
            CREATE TABLE DISPOSITIVOS(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_DISPOSITIVO VARCHAR(50),
            SERIAL_NUMBER VARCHAR(50),
            MODELO VARCHAR(10),
            COMENTARIOS VARCHAR(100))
            ''')
        messagebox.showinfo("BBDD", "BBDD creada con exito")
    except ValueError:
        messagebox.showwarning('Atencion,", "La BBDD ya existe')


def salir_aplicacion():
    valor = messagebox.askquestion("Salir", "Deseas salir de la aplicacion?")

    if valor == "yes":
        root.destroy()


def limpiar_campos():
    mi_nombre.set("")
    mi_id.set("")
    mi_model.set("")
    mi_serial_number.set("")
    texto_comentario.delete(1.0, END)


#
def crear():
    mi_conexion = sqlite3.connect("Dispositivos")

    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute("INSERT INTO DISPOSITIVOS VALUES(NULL, '" + mi_nombre.get() +
                      '\',\'' + mi_serial_number.get() +
                      '\',\'' + mi_model.get() +
                      '\',\'' + texto_comentario.get("1.0", END) + "')")

    mi_conexion.commit()

    messagebox.showinfo("BBDD", "Registro insertado con exito")


def leer():
    mi_conexion = sqlite3.connect("Dispositivos")

    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute("SELECT * FROM D WHERE ID=" + mi_id.get())

    el_dispositivo = mi_cursor.fetchall()

    for Dispositivo in el_dispositivo:
        mi_id.set(Dispositivo[0])
        mi_nombre.set(Dispositivo[1])
        mi_serial_number.set(Dispositivo[2])
        mi_model.set(Dispositivo[3])
        texto_comentario.insert(1.0, Dispositivo[5])

    mi_conexion.commit()


def actualizar():
    mi_conexion = sqlite3.connect("Dispositivos")

    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute("UPDATE DISPOSITIVOS SET NOMBRE_Dispositivo='" + mi_nombre.get() +
                      '\', SERIALNUMBER=\'' + mi_serial_number.get() +
                      '\', Modelo=\'' + mi_model.get() +
                      '\', COMENTARIOS=\'' + texto_comentario.get("1.0", END) +
                      '\' WHERE ID=' + mi_id.get())

    mi_conexion.commit()

    messagebox.showinfo("BBDD", "Registro actualizado con exito")


def eliminar():
    mi_conexion = sqlite3.connect("Dispositivos")

    mi_cursor = mi_conexion.cursor()

    mi_cursor.execute("DELETE FROM DISPOSITIVOS WHERE ID=" + mi_id.get())

    mi_conexion.commit()

    messagebox.showinfo("BBDD", "Registro eliminado con exito")


root = tk.Tk()
root.geometry("350x400")
app = UI(parent=root)
barra_menu = Menu(root)
root.config(menu=barra_menu, width=300, height=300)

bbdd_menu = Menu(barra_menu, tearoff=0)
bbdd_menu.add_command(label="Conectar", command=conexion_bbdd)
bbdd_menu.add_command(label="Salir", command=salir_aplicacion)

borrar_menu = Menu(barra_menu, tearoff=0)
borrar_menu.add_command(label="Borrar campo", command=limpiar_campos)

crud_menu = Menu(barra_menu, tearoff=0)
crud_menu.add_command(label="Crear", command=crear)
crud_menu.add_command(label="Leer", command=leer)
crud_menu.add_command(label="Actualizar", command=actualizar)
crud_menu.add_command(label="Borrar", command=eliminar)

#ayuda_menu = Menu(barra_menu, tearoff=0)
#ayuda_menu.add_command(label="Licencia")
#ayuda_menu.add_command(label="Acerca de")

barra_menu.add_cascade(label="BBDD", menu=bbdd_menu)
barra_menu.add_cascade(label="Borrar", menu=borrar_menu)
barra_menu.add_cascade(label="Opciones", menu=crud_menu)
#barra_menu.add_cascade(label="Ayuda", menu=ayuda_menu)

# ----------------------comienzo de campos-------------------------------

mi_frame = Frame(root)
mi_frame.pack()

mi_id = StringVar()
mi_nombre = StringVar()
mi_model = StringVar()
mi_serial_number = StringVar()

cuadro_id = Entry(mi_frame, textvariable=mi_id)
cuadro_id.grid(row=0, column=1, padx=10, pady=10)

cuadro_nombre = Entry(mi_frame, textvariable=mi_nombre)
cuadro_nombre.grid(row=1, column=1, padx=10, pady=10)
cuadro_nombre.config(fg="blue", justify="left")

cuadro_sn = Entry(mi_frame, textvariable=mi_serial_number)
cuadro_sn.grid(row=2, column=1, padx=10, pady=10)

cuadro_modelo = Entry(mi_frame, textvariable=mi_model)
cuadro_modelo.grid(row=3, column=1, padx=10, pady=10)

texto_comentario = Text(mi_frame, width=16, height=5)
texto_comentario.grid(row=5, column=1, padx=10, pady=10)
scroll_vert = Scrollbar(mi_frame, command=texto_comentario.yview)
scroll_vert.grid(row=5, column=2, sticky="nsew")

texto_comentario.config(yscrollcommand=scroll_vert.set)

# ------------------------aqui comienzan los label------------------------

id_label = Label(mi_frame, text="Id:")
id_label.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombre_label = Label(mi_frame, text="Nombre:")
nombre_label.grid(row=1, column=0, sticky="e", padx=10, pady=10)

sn_label = Label(mi_frame, text="Serial Number:")
sn_label.grid(row=2, column=0, sticky="e", padx=10, pady=10)

modelo_label = Label(mi_frame, text="Modelo:")
modelo_label.grid(row=3, column=0, sticky="e", padx=10, pady=10)

comentarios_label = Label(mi_frame, text="Comentarios:")
comentarios_label.grid(row=5, column=0, sticky="e", padx=10, pady=10)

# -----------------------aqui los botones----------------------------------

mi_frame2 = Frame(root)
mi_frame2.pack()

boton_crear = Button(mi_frame2, text="Crear", command=crear)
boton_crear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

boton_leer = Button(mi_frame2, text="Leer", command=leer)
boton_leer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

boton_actualizar = Button(mi_frame2, text="Actualizar", command=actualizar)
boton_actualizar.grid(row=1, column=2, sticky="e", padx=10, pady=10)

boton_borrar = Button(mi_frame2, text="Borrar", command=eliminar)
boton_borrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)

app.mainloop()
