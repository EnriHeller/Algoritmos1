from pila import Pila

elementos = [7,1,3,3,3,2,3,3,8,8,8,2]

pila_prueba = Pila()
for e in elementos:
    pila_prueba.apilar(e)

def remover_duplicados_consecutivos(pila):
    pila_aux = Pila()

    while not pila.esta_vacia():
        valor_actual = pila.desapilar()
        if (pila.esta_vacia()) or (valor_actual != pila.ver_tope()):
            pila_aux.apilar(valor_actual)
    
    while not pila_aux.esta_vacia():
        nuevo_valor = pila_aux.desapilar()
        pila.apilar(nuevo_valor)


remover_duplicados_consecutivos(pila_prueba)

print(pila_prueba)