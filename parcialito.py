
"""for x in range(2, 29, 7):
    print("Valor al inicio de la iteracion:", x)
    x = (x * 2) - 3
    print("Valor al final de la iteracion:", x)
"""
"""numero = 2 
while numero < 29:
    print("Valor al inicio de la iteracion:", numero)
    numero_2 = (numero * 2) - 3
    print("Valor al final de la iteracion:", numero_2)
    numero += 7"""


"""
def es_primo(numero):
        if numero <= 1:
            return False  # Los números menores o iguales a 1 no son primos
        
        if numero == 2:
            return True  # 2 es un número primo
        
        if numero % 2 == 0:
            return False  # Los números pares mayores que 2 no son primos
        
        for i in range(3, int(numero ** 0.5) + 1, 2):
            if numero % i == 0:
                return False  # Si es divisible por algún número en este rango, no es primo
        
        return True  # Si no es divisible por ningún número en el rango, es primo

def positivo_primo(c:int)->int:
    while True:
        n = int(input("Ingrese su numero: "))
        if(n <= 0 or not es_primo(n) ):
            continue
        elif n == c:
            return -1
        else:
            return n
 
positivo_primo(40)"""


"""import random

def generar_direccion_ipv6():
    direccion = []
    for i in range(8):
        secuencia = ""
        for c in range(4):
            secuencia += random.choice("0123456789abcdef")
        direccion.append(secuencia)
    return ":".join(direccion)

print(generar_direccion_ipv6())"""


"""def invertir_lista(lista):
    primer_elemento = lista[0]
    for i in range (len(lista)):
        lista[i] = lista[len(lista)-1-i]
    lista[len(lista)-1] = primer_elemento
    return lista

print(invertir_lista([0,1,2,3,4,5,6,7,8]))"""

"""def filtrar_n_termina_en_0(lista)->list:
    lista_filtrada = []
    for e in lista:
        if str(e)[-1] == "0":
            lista_filtrada.append(e)

    return lista_filtrada

print(filtrar_n_termina_en_0([1230,4234,5353,120,5,0,52345,100]))"""


"""def imprimir_matriz_4x4():
    entrada = input("ingrese sus 16 numeros separados con espacios: ")
    lista_numeros = entrada.split()
    matriz = [[],[],[],[]]
    fila_actual = 0
    for i in range(len(lista_numeros)):
        if(i%4 == 0 and i not in [0,16]):
            fila_actual += 1
        matriz[fila_actual].append(lista_numeros[i])

    for fila in matriz:
        print(fila)
        
imprimir_matriz_4x4()

        """

"""def obtener_elementos_comunes(lista1,lista2):
    e_comunes= []
    for e in lista1:
        if e in lista2:
            e_comunes.append(e)
    return e_comunes

print(obtener_elementos_comunes([0,1,3,5,7],[0,3,5,9,112,123,24]))"""

"""def elemA_estan_en_B(A,B):
    for e in A:
        if(e not in B):
            return False
    return True

print(elemA_estan_en_B([0,1,2,3,4],[0,1,2,3,5,6,7]))"""

"""def miki_moko():
    for n in range(1, 101):
        if n%3 == 0 and n%5 ==0:
            print("MikiMoko")
        elif n%3 == 0:
            print("Miki")
        elif n%5 == 0:
            print("Moko")
        else:
            print(n)

miki_moko()"""
"""def maximos_columnas(matriz):
    maximos = []
    for fila in matriz:
        maximo = sorted(fila).pop()
        maximos.append(maximo)
    return maximos

print(maximos_columnas([[0,1,34,5,7],[0,5,6,12,13,35,8],[0,5,8,1,34,6,23,36,2]]))"""

"""def obtener_bigramas(frase):
    palabras = frase.split()
    bigramas = []
    for i in range(len(palabras)):
        if i != len(palabras)-1 :
            bigramas.append((palabras[i],palabras[i+1]))
    return bigramas

print(obtener_bigramas("Uno se alegra de ser util"))
"hola".isdecimal()"""


"""def frase_con_guiones():
    frecuencia = input("Ingrese una frecuencia: ")
    frase = input("Ingrese una frase: ")
    frecuencia= int(frecuencia)
    porciones = []
    for caracter in range(0,len(frase),frecuencia):
        porcion= list(frase)[caracter:caracter+frecuencia]
        porciones.append("".join(porcion))
    print("-".join(porciones)) 

frase_con_guiones()"""

def a_multiplos_de_b():
  while True:
    a = input("Ingrese el numero 'a': ")
    if not a.isdecimal() or int(a)<=0:
      continue
    b = input("Ingrese el numero 'b': ")
    while not b.isdecimal() or int(b)==0:
        b = input("Ingrese el numero 'b': ")
    
    for n in range(1, int(a)+1):
      print(int(b)*n)
    break
  
a_multiplos_de_b()