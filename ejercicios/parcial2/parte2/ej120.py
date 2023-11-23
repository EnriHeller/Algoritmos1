"""Se tiene un archivo llamado socios.csv, con muchas líneas (es decir, no entra en memoria), de formato dni,nombre,edad,estado_civil,tiene_empleo,terminó_secundario, donde tiene_empleo y terminó_secundario son 0 si es falso y 1 si es verdadero. Escribir un programa que imprima (como se quiera) todos los datos de los no graduados del secundario, con empleo y que sean menores de 35 años. El archivo debe cerrarse en todos los casos, tanto cuando finaliza la ejecución normalmente como si hay algún error."""

def filtrar_personas(ruta):
    datos_filtrados = []
    with open(ruta) as archivo:
        for linea in archivo:
            datos = linea.split(",")
            tiene_empleo = datos[-2]
            termino_secundario = datos[-1]
            edad = datos[3]
            
            if termino_secundario == 0 and tiene_empleo == 1 and edad < 35:
                datos_filtrados.append(linea)
    for dato in datos_filtrados:
        print(dato)