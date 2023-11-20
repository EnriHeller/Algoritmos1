"""

Implementar un método de la clase ListaEnlazada que elimine sobre la misma lista los elementos consecutivos repetidos. La misma está implementada con únicamente una referencia al primer nodo self.prim y cada nodo tiene los atributos para su dato dato y su próximo nodo prox.

Ejemplo:

L: [3 4 4 4 1 4] -> L.eliminar_consecutivos() -> L: [3 4 1 4]

"""

def eliminar_consecutivos(self):

    if not self.prim:
        return 

    nodo_actual = self.prim

    while nodo_actual.prox:
    
        if nodo_actual.dato == nodo_actual.prox.dato:
            if nodo_actual.prox.prox:
                nodo_actual.prox = nodo_actual.prox.prox
            else:
                nodo_actual.prox = None
    
        else:
            nodo_actual = nodo_actual.prox