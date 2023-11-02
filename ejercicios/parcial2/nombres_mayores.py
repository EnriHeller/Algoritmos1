def buscar_nombres_de_mayores(nombre_archivo):
    '''
    DOC: Completar
    '''
    edades_nombres = {}
    with open(nombre_archivo, "r") as archivo:
        
        for linea in archivo:
            nombre, edad = linea.split(",")
            edades_nombres[int(edad)] = edades_nombres.get(int(edad),[])
            edades_nombres[int(edad)].append(nombre)

    mayor_edad = max(edades_nombres.keys())
    
    return mayor_edad, edades_nombres[mayor_edad]

resultado = buscar_nombres_de_mayores("nombres.txt")
print(resultado)