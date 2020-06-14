import numpy as np

labels = ["Euler","Euler Mejorado","RK4"]

def Euler(a,b,y0,h,M,f):
   # x= np.zeros(M+1)
    y= np.zeros(M+1)

    #Valores iniciales
    #x[0]=a
    y[0]=y0 
    
    x = np.linspace(a,b,M+1)
    for i in range(0,M):
    #    x[i+1] = x[i]+h
        y[i+1] = y[i]+ h*f(x[i], y[i])
        
    return (x,y)

def EulerMejorado(a,b,y0,h,M,f):
    #U= np.zeros(M+1)
    y= np.zeros(M+1)
    

    #Valores iniciales
    #x[0]=a
    y[0]=y0 
    
    x = np.linspace(a,b,M+1)
    for i in range(0,M):
    #    x[i+1] = x[i]+h
        k1 = f(x[i],y[i])   #pendiente del predictor
        U = y[i]+ h*k1 # predicción
        k2= f(x[i+1],U)
        y[i+1] = y[i]+ h*(0.5)*(k1+k2) #corrección
       
    return (x,y)

def RK4(a,b,y0,h,M,f):
    x = np.linspace(a,b,M+1)
    y= np.zeros(M+1)
    
    y[0]= y0
    
    for i in np.arange(0,M):
        k1=f(x[i],y[i])
        k2=f(x[i]+(h/2), y[i] + (h/2)*k1)
        k3=f(x[i]+(h/2), y[i] + (h/2)*k2)
        k4=f(x[i+1], y[i]+ h*k3)
        
        k = (1/6)*(k1+2*k2+2*k3+k4)
        
        y[i+1]= y[i] + h*k
        
    return x,y







