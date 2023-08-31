def hola(nombre):
    return "hola "+nombre

#print(hola("Enrique"))

def cuad(n):
    return n * n
"""
def suma_5_cuadrados():
    return cuad(1) + cuad(2) + cuad(3) + cuad(4) + cuad(5)
"""
"""
def suma_5_cuadrados():
    suma = 0 #variables no llevan def
    suma = suma + cuad(1)
    suma = suma + cuad(2)
    suma = suma + cuad(3)
    suma = suma + cuad(4)
    suma = suma + cuad(5)

    return suma
"""

def suma_5_cuadrados():
    suma = 0
    for i in range(1,6):
        suma = suma + cuad(i)
    return suma

print(suma_5_cuadrados())

"""
EXPRESIONES
Los identificadores son los nombres que les doy a las cosas
Las expresiones son un conjunto de variables y operaciones que producen un valor
Las expresiones pueden ser simples o compuestas. Puede haber expresiones dentro de otras.
Las expresiones literales producen como resultado literalmente como se llaman (numeros, cadena de caracteres)
Las variables son expresiones con nombres que alojan algún valor. Si hay nombres, hay variables.
Las operaciones son expresiones donde dos expresiones se ven relacionadas por un operador.
Las expresiones "llamada a función) son de tipo nombreDeLafunción(parametros)

division común -> /
división entera -> //
resto -> % (este operador se llama modulo) 
"""

"""
INSTRUCCIONES
Cada linea de código es una instrucción o sentencia. Una función es una instrucción formada de más instrucciones.

Las asignaciones solo se escriben con el nombre y pueden ser redefinidas
+= reescribe arriba de la asignación

Las definiciones de funciones, son instrucciones que parten de una firma def <nombre>(parametros) y son seguidas de un cuerpo(conjunto de instrucciones). 

El return es una instrucción que solo tiene sentido dentro de una función y permite que una función devuelva un valor. Si no hay return, la función por defecto devuelve none

EL cliclo definido (for) precisa una variable que se define for <variable> y un range(n) que cuenta desde 0 hasta n-1.

Con import <archivo> podes traer otras cosas 
Con from cuad import funcion/*, haces lo mismo.
Se puede importar bibliotecas nativas de python. por ejemplo math. con math.pi, traes el numero pi. 
"""

"""FUNCIONES

Se pueden pensar como las funciones matemáticas. La gracia de las funciones es que cada una cumpla una tarea específica, que permita que generar funciones más complejas, compuesta por las funciones más simples. Las funciones son como las moléculas de los programas.

La función print no se comporta como una función matemática porque no devuelve un resultado, si no que se escapa y realiza otra tarea. Se dice que tiene efectos secundarios (mostrar en pantalla) o que realiza un "procedimiento".

INPUT:
con la función input le permito al usuario ingresar algun dato. Cualquier cosa que mande el usuario va a ser de tipo string. La función int te convierte lo que le pases a un entero. Con la función str, podes convertir cualquier cosa a una cadena de texto. 
"""
nombre = input("Como te llamas? ")
print("hola "+ nombre)
"""
IMPORTANTE:
SI NO TE PIDEN QUE IMPRIMAS, NO LO IMPRIMAS. SI QUERES QUE UNA FUNCIÓN HAGA ALGO NO NECESARIAMENTE TIENE QUE IMPRIMIR DICHA FUNCIÓN. HAY QUE MANTENER LA FUNCIONES PURAS.
"""


"""
lo que se define dentro de una función, no funciona por fuera de la función. Las variables globales estan por fuera y las locales estan por dentro de las funciones. 

IMPORTANTE:
HAY QUE TRATAR DE NO USAR VARIABLES GLOBALES. UNA VARIABLE GLOBAL QUE CAMBIA DE VALOR ES UNA MALA PRACTICA. Las variables globales las reservamos para las constantes. Por convención, las constantes van en mayúscula.

"""
#Si quiero que una variable sea de un tipo en específico (no cambia en como funciona el programa, es solo documentación. Se llama type hints):
def cuad(x:float)-> int : "expect float, return int"

#Si tiene una sola linea la instrucción, no hace falta que haga un espacio, puedo hacerlo en una sola linea. 

#Instrucción pass: Si se cumple una condición, podes "pasar" de resolverla.

def funcion_que_no_hace_nada(): pass

# esta_es_la_forma_de_poner_nombres_a_las_funciones_por_convención
# las variables en minuscula.

"""
CONDICIONALES:

IF:
if expresion:instruccion

OPERADORES DE COMPARACIÓN

== -> igualdad
!= -> distinto
>= -> mayor o igual
<= -> menor o igual
> -> mayor
< -> menor
and -> y
or -> o
not -> no
"""

#else if = elif

#assert: assert <boolean>. Si es verdadero, no pasa nada. Si es falso, da error. 