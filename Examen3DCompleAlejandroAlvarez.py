"""
Instituto Tecnológico de Chetumal
NombreAlumno: Álvarez Carranza Alejandro Cruz 
No.Control:18390043
Docente: May Canché Isaias
Materia: Graficación
Grupo: I5U

EXAMEN COMPLEMENTARIO 3D
"""
#Importacion de librerias que utilizamos en anteriores programas
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, radians, sqrt

#Importacion de la cual se utiliza una función para determinar el valor de una sola tecla
import msvcrt

#Variable para guardar el valor de tecla presionada, se usa para determinar si continuar la ejecución o terminarla, dependiendo de si presiona determinada tecla o no
tecla=None

#Mientras la variable tecla sea diferente de ESC, Continuará la ejecución del programa
while tecla != chr(27):

    #Establecer tamaño de Ventana y activar la malla de la ventana
    plt.axis([0,200,80,0])
    plt.axis('on')
    plt.grid(True)

    #Establecer Titulo
    plt.title('Examen Complementario: Hitpoint Con Triangulo Mediante Formula de Heron')

    #Establecer los Ejes Y y X
    plt.ylabel('Eje Y') 
    plt.xlabel('Eje X') 

    #Pedir Valores al usuario
    hitx=float(input('Ingrese la coordenada del HitPoint en: X'))
    hity=float(input('Ingrese la coordenada del HitPoint en: Y'))

    #Asignar los valores en un Array para el dibujado de la figura y el calculo de distancias y areas
    x=[40,30,80,hitx]
    y=[60,10,60,hity]

    #Dibujar el Triangulo Base ---A
    plt.plot([x[0],x[1]],[y[0],y[1]],color='k') 
    plt.plot([x[1],x[2]],[y[1],y[2]],color='k')
    plt.plot([x[2],x[0]],[y[2],y[0]],color='k')

    #Dibujar el HitPoint
    plt.scatter(x[3],y[3],s=20,color='r')

    #Dibujar Triangulos Auxiliares
    plt.plot([x[0],x[3]],[y[0],y[3]],linestyle=':',color='peru')
    plt.plot([x[1],x[3]],[y[1],y[3]],linestyle=':',color='darksalmon')
    plt.plot([x[2],x[3]],[y[2],y[3]],linestyle=':',color='hotpink')

    #Escribir Identificadores de los puntos
    plt.text(35,60,'0')
    plt.text(32,10,'1')
    plt.text(82,60,'2')
    plt.text(x[3]+2,y[3],'3')

    #Distancias del triangulo Base
    #---Distancia del punto 0 al punto 1
    a=x[1]-x[0]
    b=y[1]-y[0]
    Distancia0a1=sqrt(a*a+b*b)

    #---Distancia del punto 2 al punto 1
    a=x[2]-x[1]
    b=y[2]-y[1]
    Distancia2a1=sqrt(a*a+b*b)

    #---Distancia del punto 2 al punto 0
    a=x[2]-x[0]
    b=y[2]-y[0]
    Distancia2a0=sqrt(a*a+b*b)

    #Distancias de Triangulos Auxiliares
    #---Distancia del punto 1 al punto 3
    a=x[1]-x[3]
    b=y[1]-y[3]
    Distancia1a3=sqrt(a*a+b*b)

    #---Distancia del punto 2 al punto 3
    a=x[2]-x[3]
    b=y[2]-y[3]
    Distancia2a3=sqrt(a*a+b*b)

    #---Distancia del punto 3 al punto 0
    a=x[0]-x[3]
    b=y[0]-y[3]
    Distancia0a3=sqrt(a*a+b*b)

    #Calcular Area del Triangulo Principal ---- A
    s=(Distancia0a1 + Distancia2a1 + Distancia2a0) / 2 
    #Formula de Herón ---- A
    A=sqrt(s * (s-Distancia0a1) * (s-Distancia2a1) * (s-Distancia2a0))

    #Calcular Area del Triangulo Auxiliar1 ---- A1
    s1=(Distancia0a1 + Distancia0a3 + Distancia1a3) / 2
    #Formula de Herón ---- A1
    A1=sqrt(s1*(s1-Distancia0a1) * (s1-Distancia0a3) * (s1-Distancia1a3))

    #Calcular Area del Triangulo Auxiliar2 ---- A2
    s2=(Distancia2a0 + Distancia2a3 + Distancia0a3) / 2
    #Formula de Herón ---- A2
    A2=sqrt(s2* (s2-Distancia2a0) * (s2-Distancia2a3) * (s2-Distancia0a3))

    #Mostrar Valor de A
    plt.text(165,60,'A= '+'%7.0f'%(A))

    #Mostrar Valor de A1
    plt.text(165,65,'A1='+'%7.0f'%(A1),color='r')

    #Mostrar Valor de A2
    plt.text(165,70,'A2='+'%7.0f'%(A2),color='r')
    
    #Mostrar Valor de la Suma de A1+A2
    plt.text(153,75,'A1+A2='+'%7.0f'%(A1+A2),color='b')

    #Determinar si la suma de las Areas de los Triangulos Auxiliares(A1+A2) es mayor o menor al Area del Triangulo Base(A)
    if A1+A2 > A:
        #En caso de que sea mayor, entonces se sabe que el HitPoint Esta fuera del Triangulo Base
        plt.text(5,70,'El HitPoint está fuera del límite del Triángulo Base')
    else:
        #En caso de que sea menor, entonces se sabe que el HitPoint Esta dentro del Triangulo Base
        plt.text(5,70,'El HitPoint está dentro del límite del Triángulo Base')

    #Mostrar Ventana con los resultados
    plt.show()

    #En este apartado se usa el msvcrt con getch, el cual espera a que el usuario presione una tecla y devuelve el valor de la tecla presionada
    print('Presione la tecla ESC para salir del programa ó Presione cualquier otra tecla para continuar')
    #utilice el siguiente link como referencia para determinar la tecla ESC y utilizarla en este programa, porque sinceramente, no sabia determinar la tecla ESC con un INPUT
    # https://stackoverflow.com/questions/5137238/how-to-detect-escape-keypress-in-python
    tecla = msvcrt.getch().decode()