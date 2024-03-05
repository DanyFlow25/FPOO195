from tkinter import Tk, Frame, Button, messagebox

#Métodos
def mostrarMensajes():
    print(messagebox.showinfo('showinfo', 'Information'))
    print(messagebox.showerror('showerror', 'Error'))
    print(messagebox.showwarning('showwarning', 'Warning'))
    print(messagebox.askokcancel(message="¿Desea continuar?", title="Soy el título"))
    
def addbtn():
    botonVerde.config(text="+")
    botonrosa = Button(seccion3,text="Nuevo", bg="#f7089c")
    botonrosa.configure(height=3, width=5)
    botonrosa.pack()
    
# Creamos una instancia
ventana=Tk() #Uso de poo creando objetos ventana 
ventana.title("Ejemplo con 3 frames")
ventana.geometry("600x400")
 
#colocamos frames de la ventana
seccion1=Frame(ventana, bg="red")
seccion1.pack(expand=True, fill='both')

seccion2=Frame(ventana, bg="aqua")
seccion2.pack(expand=True, fill='both')

seccion3=Frame(ventana, bg="black")
seccion3.pack(expand=True, fill='both')

#Place
botonAzul = Button(seccion1,text="Azul", fg="#0733f7")
botonAzul.place(x=60,y=60, width=500, height=30)

#grid
botonNegro = Button(seccion2,text="Negro", fg="Black")
botonNegro.configure(height=2, width=10)
botonNegro.grid(row=0, column=1)

botonAmarillo = Button(seccion2,text="Amarillo", fg="#fbff00", command=mostrarMensajes)
botonAmarillo.configure(height=2, width=10)
botonAmarillo.grid(row=2, column=1)

#Pack
botonVerde = Button(seccion3,text="Verde", fg="#06e813", command=addbtn)
botonVerde.configure(height=2, width=10)
botonVerde.pack()

#Ejecutamos la ventana
ventana.mainloop()