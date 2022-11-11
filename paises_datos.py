#Se importa libreria tkinter con todas sus funciones

from tkinter import *
from tkinter import messagebox

# funciones de la app

def datos():
    messagebox.showinfo("Suma 1.0", "procesando...")
    
    opcion = int(x.get())
    
    #processing
    if (opcion==1):
        pais = "\nPais: Colombia\nCapital: Bogota\ncontinente: America del sur\nIdioma: español\nreligion: Catolicismo\n Moneda:Peso colombiano"
    elif(opcion==2):
        pais =  "\nPais:Japon\ncapital:Tokyo\ncontinente: Asiatico\nidioma:Japones\nreligion:Budista\nmoneda:yen"
    elif (opcion==3):
        pais= "\npais:Francia\ncontinente:Europeo\nidioma:Frances\nreligion:catolicismo\nmoneda:euro"
    elif (opcion==4):
        pais = "\npais:Canada\ncontinente:America del norte\nidioma:ingles\nreligion:catolica\nmoneda:dolar canadience"
    elif (opcion==5):
        pais = "\npais:Egipto\ncotinente:Africa\nidioma:arabe\nreligion:Islam\nmoneda:libra egipcia"
        
    # otra condicion
    if (opcion>5):
     pais = ("pais no registrado")
    t_resultados.insert(INSERT, "Opcion:" + x.get()+ "."+str(pais)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados...")
    x.set("")
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrara...")
    ventana_principal.destroy()

# variables globales 


#ventana principal

#se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Sistemas UIS")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("600x600")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="black")

x = StringVar()
y  = StringVar()

#--------------------
#frame entrada datos
#--------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 580 , height = 240)
frame_entrada.place(x = 10, y = 10)

# Etiquetas par el titulo de app
titulo = Label(frame_entrada, text = "Datos del pais")
titulo.config(bg = "white", fg = "blue", font = ("Arial",16))
titulo.place(x = 150, y = 10)

# Etiquetas par el titulo de app
titulo = Label(frame_entrada, text ="1. Colombia\n""2. Japon\n""3. Francia\n""4. Canada\n""5. Egipto\n")
titulo.config(bg = "white", fg = "black", font = ("Arial",16))
titulo.place(x = 10, y = 60)

# Etiqueta para x
lb_x = Label(frame_entrada, text = "- Numero del pais = ")
lb_x.config(bg="white", fg="blue", font=("Arial",16))
lb_x.place(x=150, y=50, width=180, height=30)

# Entry para x
entry_x = Entry(frame_entrada, textvariable=x)
entry_x.config(font=("Arial",20), justify=LEFT,fg="blue")
entry_x.focus_set()
entry_x.place(x=335, y=50, width=115, height=30)

#--------------------
#frame operaciones
#--------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "white", width = 580 , height = 120)
frame_operaciones.place(x = 10, y = 260)

# Boton para sumar
bt_sumar = Button(frame_operaciones, text="Aceptar", command=datos)
bt_sumar.place(x=45, y=45, width=100, height=30)

#Boton borrar
bt_sumar = Button(frame_operaciones, text="Borrar")
bt_sumar.place(x=190, y=45, width=100, height=30)



#Boton borrar
bt_sumar = Button(frame_operaciones, text="Borrar",command=borrar)
bt_sumar.place(x=190, y=45, width=100, height=30)

# Boton salir
bt_salir = Button(frame_operaciones, text="Salir",command=salir)
bt_salir.place(x=335, y=45, width=100, height=30)

# fram resultados

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=580, height=200)
frame_resultados.place(x=10, y = 390)

#area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="green", fg="black", font=("Arial",20))
t_resultados.place(x=10,y=10, width=560, height= 180)

ventana_principal.mainloop()