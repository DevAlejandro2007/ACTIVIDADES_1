import tkinter as tk
from tkinter import PhotoImage, messagebox, Menu

#crear ventana 
window= tk.Tk()
window.title("MAYUSCULAS-MINUSCULAS")
window.geometry("1800x1920")
window.configure(background= "lightblue", ) 

logo = PhotoImage(file = "/home/alejo/Escritorio/entornos/lab/apple.png")

window.iconphoto(True,logo)


#TITULO
tk.Label(master = window, text= "INSERTAR TEXTO",bg= "lightblue", font="ARIAL 30").pack(padx= 1, pady=1)

#ENTRADAS
entrada_texto = tk.Entry(master= window, font="ARIAL 20", width= 100)
entrada_texto.pack(padx=1,pady=2)

#BOTON DE MAYUSCULAS Y MINUSCULAS
boton = tk.Button(master= window, text= "TRANSFORMAR A MAYUSCULA",font = "ARIAL 20", width=30, command= lambda: mayus())
boton.place(x= 60, y = 100)

boton2 = tk.Button(master=window, text= "TRANSFORMAR A MINUSCULA", font= "ARIAL 20", width= 30, command=lambda:mins())
boton2.place(x = 850, y = 100)

#TITULO DE SALIDA DE TEXTO 
entrada_texto2 = tk.Label(master=window, text="TEXTO FINAL", bg= "lightblue", font= "ARIAL 30")
entrada_texto2.pack(padx =1, pady=2)
tk.Label(master = window, text="----------------------------------------------", bg = "LightBlue", font= "ARIAM 20").pack(padx = 20, pady = 20)

#SALIDA DE TEXTO
salida = tk.Label(master = window, text= "",bg= "lightblue", font="ARIAL 30")
salida.pack(padx= 3, pady= 4)

#LIMPIAR TEXTO

limpiar = tk.Button(master= window, text= "LIMPIAR", font= "ARIAL 20", width= 30, command= lambda:(entrada_texto.delete(0, tk.END), salida.configure(text= "")))
limpiar.pack(padx= 3, pady= 4)

#MENU DEL SISTEMA
menu = Menu()
menu_transformar = Menu(menu, tearoff=0)

menu_transformar.add_command(label="INTERCALADO", command= lambda: intercalado())  
menu_transformar.add_command(label="NUMEROS", command= lambda: numeros())
menu.add_cascade(label="MENU DE CONVERSION", menu=menu_transformar)

menu_ayuda= Menu(menu, tearoff=0)
menu_ayuda.add_command(label="AYUDA", command= lambda : ayuda())

menu.add_cascade(label="AYUDA", menu=menu_ayuda)
window.config(menu=menu)

#MENU DE CONVERSION 

def ayuda():
    window2 = tk.Tk()
    window2.title("AYUDA")
    window2.geometry("1000x1000")
    window2.configure(background= "lightblue")
    tk.Label(master= window2, text= "AYUDA", bg= "lightblue", font="ARIAL 30").pack(padx= 1, pady=1)
    tk.Label(master= window2, text= "Este programa permite transformar el texto" +
    "en mayusculas o minusculas", bg= "lightblue", font="ARIAL 20").pack(padx= 1, pady=1)
    boton = tk.Button(master= window2, text= "CERRAR", font= "ARIAL 20", width= 30, command= window2.destroy)
    boton.pack(padx= 1, pady=1)

def intercalado():
    palabras = entrada_texto.get()
    if eSTex(palabras):
        salida.configure(text= palabras.swapcase())
    else:
        error()

def numeros():
    palabras = entrada_texto.get()
    palabras = palabras.upper()
    if eSTex(palabras):
        diccionario = {"A":4, "E":3, "I":1, "O":0, "U":"U"}
        for i in palabras:
            if i in diccionario:
                palabras = palabras.replace(i, str(diccionario[i]))
        salida.configure(text=palabras)
    else:
        error()


#FUNCIONES BASICAS 

#FUNCION DE TRANSFORMACION DE TEXTO A MAYUSCULAS
def mayus():
    palabras =entrada_texto.get()
    if eSTex(palabras):
        salida.configure(text= palabras.upper())
    else:
        error()
    

#FUNCION DE TRANSFORMACION DE TEXTO A MINUSCULAS
def mins():
    palabras = entrada_texto.get()
    if eSTex(palabras):
        salida.configure(text=palabras.lower())
    else:
        error()

#FUNCION QUE VERIFICA SI EL TEXTO ES VALIDO
def eSTex(texto):
    return all(caracter.isalpha() or caracter.isspace() for caracter in texto)

#FUNCION PARA MENSAJE DE ERROR
def error():
    messagebox.showerror("ERROR", "INGRESASTE UN NUMERO O UN CARACTER INVALIDO ")

    

    


window.mainloop()
