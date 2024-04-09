import pathlib
import numpy as np

from numpy import array
from matplotlib import pyplot as plt


def mostrarGraficaTrasformadda(trafo_fourier,nombre):
    plt.figure() # Crear una nueva figura
    plt.plot(np.abs(trafo_fourier)) # Graficar los valores absolutos de los coeficientes de Fourier
    plt.title("Transformada de Fourier para "+nombre)
    plt.xlabel("Frecuencia")
    plt.ylabel("Amplitud")
    plt.show() # Mostrar la figura
    return
    

def mostrarGrafica(x,y,nombre):
 plt.figure()
 plt.title(nombre)
 plt.grid()
 plt.plot(x,y)
 plt.show()
 return

def descomprimirTxt(archivo):
    retorno = []
    t = []
    Ft = []
    with open(archivo,'r') as archivo:
        for linea in archivo:
            numeros = linea.split()
            t.append(float(numeros[0]))
            Ft.append(float(numeros[1]))
        t_np = np.array(t)
        ft_np = np.array(Ft)
        retorno.append(t_np)
        retorno.append(ft_np)
        return retorno


ruta = pathlib.Path('.')

ruta = ruta / "QuakeProgram" / "Imputs"

print('Buscar el archivo que desea leer')

respuesta = input('Ingrese el nombre del archivo [exit para salir]: ')
nombre = respuesta

archivo = ruta / respuesta

while respuesta!="exit":
    if archivo.exists():
        
        datos_arreglo=descomprimirTxt(archivo) #Descomprimimos el txt en una lista donde el primer elemento es el t y el segundo elemento el Ft, guarados en arreglos .np

        mostrarGrafica(datos_arreglo[0],datos_arreglo[1],nombre) #muestra la grafica del terremoto donde x es el tiempo y el y amplitud

        trafo_fourier = np.fft.fft(datos_arreglo[1]) #Sacamos los coeficientes de la serie de fourier para cada pto

        print(trafo_fourier)

        mostrarGraficaTrasformadda(trafo_fourier,nombre) #mostramos la grafica de la trasformada

        respuesta = "exit" #salimos del while
    else:
        #Caso de ingresar mal el archivo
        print('No existe el archivo seleccionado')
        respuesta = input('Ingrese el nombre del archivo [exit para salir]: ')
        archivo = ruta / respuesta
        nombre = respuesta



