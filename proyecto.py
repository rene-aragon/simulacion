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

master = tk.Tk()
master.resizable(False, False)
master.wm_title("Campo de direcciones")
methods = {0:metodos.Euler,1:metodos.EulerMejorado,2:metodos.RK4}

fig = Figure()
ax1 = fig.add_subplot(111)
ax1.format_coord = lambda x, y: ""

canvas = FigureCanvasTkAgg(fig, master)
canvas.draw()
canvas.get_tk_widget().grid(row=4,column=0,columnspan=7,sticky="nsew")

toolbarFrame = tk.Frame(master)
toolbarFrame.grid(row=5,column=0,columnspan=7,sticky="ns")
toolbar = NavigationToolbar2Tk(canvas, toolbarFrame)

def graficar(i):
    x=0
    y=0
    
    if(len(f.get()) < 1):
        ax1.clear()
        ax1.plot(x,y)
        ax1.axhline(0, color="gray")
        ax1.axvline(0, color="gray")
        ani.event_source.stop()
        return
    
    x,y=evaluarMetodo()
    u,v = np.meshgrid(x,y)
    
    ax1.clear()
    
    ax1.quiver(x,y,u,v)
    ax1.plot(x,y)
    
    ax1.axhline(0, color="gray")
    ax1.axvline(0, color="gray")
    ani.event_source.stop() #DETIENE ANIMACIÓN
    
def represent():
    ani.event_source.start() #INICIA/REANUDA ANIMACIÓN

def validarDatos(): 
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
    if(len(M.get()) == 0):
        return "ingresa un numero de subintervalos"
    if(metodo.current() < 0):
        return "selecciona un metodo"  
    
    try:
        float(a.get())+float(b.get())+float(y0.get())+float(h.get())+float(h.get())
    except:
        return "revisa que los campos contengan numeros"
    
    return ""

def evaluarMetodo():
    error = validarDatos()
    
    if(len(error)>0):
        messagebox.showinfo("Revisar campos","Por favor "+error)
        return 0,0
    
    method = methods.get(metodo.current())
   
    m = int(round((float(b.get())-float(a.get()))/float(h.get())))
    x,y = method(float(a.get()),float(b.get()),float(y0.get()),float(h.get()),m,funcion)
    
    return x,y

def funcion(x,y):
    print("eval("+f.get()+")")
    return eval(f.get())
    

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

M = tk.Entry(master)
M.grid(padx=5,row=3,column=5)

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
tk.Label(master,text="Subintervalos").grid(row=2,column=5)
tk.Label(master,text="a").grid(row=3,column=1)
tk.Label(master,text="b").grid(row=3,column=3)

ani = animation.FuncAnimation(fig, graficar)

tk.mainloop()