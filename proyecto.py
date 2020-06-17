#Librerias para entorno grafico
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

#Librerias para resolver los metodos
import metodos
import numpy as np
import matplotlib.pyplot as plt

master = tk.Tk() #Se asigna master como la ventana principal
master.resizable(False, False) #La ventana no se puede reescalar
master.wm_title("Campo de direcciones") #Se le pone un titulo a la ventana
methods = {0:metodos.Euler,1:metodos.EulerMejorado,2:metodos.RK4} #Este es un arreglo de los métodos disponibles
# 0 => euler
# 1 => euler mejorado
# 3 => RK4

fig = Figure() #se crea una figura
ax1 = fig.add_subplot(111) #se asigna fig a ax1 como subgrafica única en la columna 1, renglon 1
ax1.format_coord = lambda x, y: "" #Las coordenadas del puntero no se van a mostrar

canvas = FigureCanvasTkAgg(fig, master) #Se crea un canvas que contiene la grafica
canvas.draw() #Dibuja el canvas
canvas.get_tk_widget().grid(row=4,column=0,columnspan=7,sticky="nsew") #Posiciona el canvas en la ventana

toolbarFrame = tk.Frame(master) #Se crea la barra de herramientas de la grafica
toolbarFrame.grid(row=5,column=0,columnspan=7,sticky="ns") #Posiciona la barra de herramientas en la ventana
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame) #Enlaza la barra de herramientas con el canvas de la gráfica

def graficar(i): #Funcion que grafica en el canvas
    x=0 #Por default x y son cero
    y=0
    
    if(len(f.get()) < 1): #Si el campo de funcion esta vacio, ejecuta el código
        ax1.clear() #Limpia la grafica
        ax1.plot(x,y) #Grafica un punto en (0,0)
        ax1.axhline(0, color="gray") #Establece el eje de las x en color gris
        ax1.axvline(0, color="gray") #Establece el eje de las y en color gris
        ani.event_source.stop() #Detiene la animación de graficado
        return #Sale de la funcion
    
    # En caso de que el campo de función NO este vacío:
    x,y=evaluarMetodo() #Evalua x y
    X,Y=np.meshgrid(x,y)
    u,v = x,y 
    # Normalize the arrows:
    U = u / np.sqrt(u**2 + v**2);
    V = v / np.sqrt(u**2 + v**2);

    ax1.clear() #Limpia la grafica
    ax1.quiver(X,Y,U,V,units='width') #Grafica el campo de direcciones
    ax1.plot(x,y) #Grafica la funcion
    ax1.plot(float(a.get()),float(y0.get()),'ro')

    #ax1.axhline(0, color="gray") #Establece el eje de las x en color gris
    #ax1.axvline(0, color="gray") #Establece el eje de las y en color gris
    ani.event_source.stop() #Detiene la animación de graficado
    
def represent():
    ani.event_source.start() #Inicia i reanuda la animación de graficado

def validarDatos():  #Esta función verifica que no haya campos vacíos
    if(len(f.get()) == 0):
        return "ingresa una funcion"
    if(len(y0.get()) == 0):
        return "ingresa un valor inicial"
    if(len(a.get()) == 0):
        return "ingresa un intervalo de inicio"
    if(len(b.get()) == 0):
        return "ingresa un intervalo de fin"
    if(len(h.get()) == 0):
        return "ingresa un tamaño de paso"
   ## if(len(M.get()) == 0):
        ##return "ingresa un numero de subintervalos"
    if(metodo.current() < 0):
        return "selecciona un metodo"  
    
    #Se asegura que los valores de los campos se puedan convertir a numero
    try:
        float(a.get())+float(b.get())+float(y0.get())+float(h.get())+float(h.get())
    except:
        return "revisa que los campos contengan numeros"
    
    return "" #En caso de que no haya error, regresa una cadena vacía

def evaluarMetodo(): #Función que evalua según el método elegido
    error = validarDatos() #Revisa que no haya campos vacios
    
    if(len(error)>0): #Si hay un error muestra el mensaje de error
        messagebox.showinfo("Revisar campos","Por favor "+error) #Ventana emergente
        return 0,0 #Regresa valores de x=0, y=0
    
    #metodo.current() obtiene el indice del valor seleccionado de la lista desplegable
    method = methods.get(metodo.current()) #accede al arreglo de funciones la asigna a method
   
    m = int(round((float(b.get())-float(a.get()))/float(h.get()))) #Calcula m=b-a/h
    x,y = method(float(a.get()),float(b.get()),float(y0.get()),float(h.get()),m,funcion) #Evalua la función según el método seleccionado
    
    return x,y #Regresa los valores de x y

def funcion(x,y): #función evaluada según la entrada del campo función
    return eval(f.get())
    
###############################
#     ELEMENTOS GRÁFICOS      #
###############################
    
#Campos de texto
f = tk.Entry(master)
f.grid(padx=5,row=1,column=0)

y0 = tk.Entry(master)
y0.grid(padx=5,row=1,column=1,columnspan=4)

a = tk.Entry(master, width=5)
a.grid(padx=5,row=3,column=2)

b = tk.Entry(master, width=5)
b.grid(padx=5,row=3,column=4)

h = tk.Entry(master)
h.grid(padx=5,row=1,column=5)

##M = tk.Entry(master)
##M.grid(padx=5,row=3,column=5)

#Combobox (desplegable)
metodo = ttk.Combobox(master,values=metodos.labels,state="readonly")
metodo.grid(padx=5,row=1,column=6)

#Botones
tk.Button(master,text="Graficar",command=represent).grid(padx=5,row=3,column=6)

#Etiquetas
tk.Label(master,text="Ecuacion").grid(row=0,column=0)
tk.Label(master,text="Valor inicial:").grid(row=0,column=1,columnspan=4)
tk.Label(master,text="Tamano de paso").grid(row=0,column=5)
tk.Label(master,text="Metodo de evaluacion").grid(row=0,column=6)
tk.Label(master,text="Intervalo [a,b]").grid(row=2,column=1,columnspan=4)
##tk.Label(master,text="Subintervalos").grid(row=2,column=5)
tk.Label(master,text="a").grid(row=3,column=1)
tk.Label(master,text="b").grid(row=3,column=3)

ani = animation.FuncAnimation(fig, graficar) #Animación de graficado

tk.mainloop() #Cnp.exp()iclo principal de la ventana grafica