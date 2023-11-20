from cola import Cola

def intercarlar_en_cola_final(colas, cola_final):

    cambios = 0

    for cola_i in colas:
        if not cola_i.esta_vacia():
            cola_final.encolar(cola_i.desencolar())
            cambios +=1

    if cambios == 0:
        return cola_final
    else:
        intercarlar_en_cola_final(colas, cola_final)


def intercalar(colas):
    
    cola_final = Cola()

    intercarlar_en_cola_final(colas, cola_final)


    