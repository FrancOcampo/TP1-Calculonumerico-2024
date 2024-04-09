import pathlib
import numpy as np

from numpy import array
from matplotlib import pyplot as plt

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
                
        # Leer los datos de los archivos
        datos= descomprimirTxt(archivo)
        # datos = np.loadtxt(archivo)
        # tiempo, datos= np.loadtxt(archivo, unpack=True)

        # Aplicar la Transformada de Fourier Discreta a los datos
        # coeficientes1 = np.fft.fft(datos[1])
        trafo_fourier = np.fft.fft(datos[1]) # Transformada de Fourier

        # Imprimir los coeficientes de Fourier
        # print("Coeficientes de Fourier para terremoto1.txt:", coeficientes1)
        plt.figure() # Crear una nueva figura
        plt.plot(np.abs(trafo_fourier)) # Graficar los valores absolutos de los coeficientes de Fourier
        plt.title("Transformada de Fourier para "+nombre)
        plt.xlabel("Frecuencia")
        plt.ylabel("Amplitud")
        plt.show() # Mostrar la figura

        # grafica=descomprimirTxt(archivo)

        mostrarGrafica(datos[0],datos[1],nombre)

        respuesta = "exit"
    else:
        print('No existe el archivo seleccionado')
        respuesta = input('Ingrese el nombre del archivo [exit para salir]: ')
        archivo = ruta / respuesta
        nombre = respuesta


