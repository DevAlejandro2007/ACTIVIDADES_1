import tkinter as tk
from tkinter import PhotoImage, messagebox

#from tkinter import menu

#crear ventana 
window= tk.Tk()
window.title("MAYUSCULAS-MINUSCULAS")
window.geometry("1800x1920")
window.configure(background= "lightblue", ) 

logo = PhotoImage(file = "apple.png")

window.iconphoto(True,logo)


#TITULO
tk.Label(master = window, text= "INSERTAR TEXTO",bg= "lightblue", font="ARIAL 30").pack(padx= 1, pady=1)

#ENTRADAS
entrada_texto = tk.Entry(master= window, font="ARIAL 20", width= 100)
entrada_texto.pack(padx=1,pady=2)

boton = tk.Button(master= window, text= "TRANSFORMAR A MAYUSCULA",font = "ARIAL 20", width=25, command= lambda: mayus())
boton.place(x= 90, y = 100)

boton2 = tk.Button(master=window, text= "TRANSFORMAR A MINUSCULA", font= "ARIAL 20", width= 25, command=lambda:mins())
boton2.place(x = 1185, y = 100)


entrada_texto2 = tk.Label(master=window, text="TEXTO FINAL", bg= "lightblue", font= "ARIAL 30")
entrada_texto2.pack(padx =1, pady=2)


salida = tk.Label(master = window, text= "",bg= "lightblue", font="ARIAL 30")
salida.pack(padx= 3, pady= 4)



def mayus():
    palabras =entrada_texto.get()
    if eSTex(palabras):
        salida.configure(text= palabras.upper())
    else:
        error()
    
def mins():
    palabras = entrada_texto.get()
    if eSTex(palabras):
        salida.configure(text=palabras.lower())
    else:
        error()

def eSTex(texto):
    return all(caracter.isalpha() or caracter.isspace() for caracter in texto)

def error():
    messagebox.showerror("ERROR", "INGRESASTE UN NUMERO O UN CARACTER INVALIDO ")

    

    


window.mainloop()
