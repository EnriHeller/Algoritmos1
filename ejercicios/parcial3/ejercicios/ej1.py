from pila import Pila

pila_prueba = Pila()
for i in range (10):
    pila_prueba.apilar(i)

print(pila_prueba)

def remplazar(pila, valor_nuevo, valor_viejo):
    pila_respaldo = Pila()

    while not pila.esta_vacia():
        valor_actual = pila.desapilar()
        if valor_actual == valor_viejo:
            valor_actual = valor_nuevo
        
        pila_respaldo.apilar(valor_actual)

    while not pila_respaldo.esta_vacia():
        valor_actualizado = pila_respaldo.desapilar()
        pila.apilar(valor_actualizado)

    print(pila)

remplazar(pila_prueba,"funciona",5)
