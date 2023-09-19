
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



