import random 

def definir_palabras()->[str]:
    """
    Transforma palabras separadas por espacio desde un input a una lista de las mismas en minúscula.
    """

    entrada = input("Ingrese las palabras para contar entre contactos: ")
    lista_palabras = entrada.lower().split()

    return lista_palabras

def es_mensaje_valido(linea: str)->bool:
    """
    Recibe una linea del archivo de chat y retorna si es un mensaje valido. Se considera mensaje valido a aquel que es enviado por un contacto. No considera envíos de multimedia ni avisos/advertencias propias del chat.
    
    Para considerar a un mensaje como valido, en el mismo se debe encontrar una secuencia similar a la siguiente: 

    'Contacto: Mensaje'

    Por ende, todo mensaje valído tendrá un ": " incluido. 
    Existe la excepción para los "Multimedias Emitidos", donde aparece un ": <". Por eso se contempla dentro de lo que retornará esta función.
    """

    return ": <" not in linea and ": " in linea

def obtener_informacion_de_linea(mensaje:str)->(str,str):
    """
    Recibe un mensaje enviado por un contacto y devuelve el contacto y el mensaje por separado, dentro de una tupla.
    """
    
    contacto_y_mensaje = mensaje.split(" - ", 1)[1]
    contacto, mensaje = contacto_y_mensaje.split(":",1)

    return contacto,mensaje

def palabras_por_mensaje(palabras_a_filtrar:[str], mensaje:str) -> dict:
    """
    Dada una lista de palabras a encontrar dentro de un mensaje, obtengo un diccionario donde cada clave es la palabra. Cada valor, es la cantidad de veces que dicha palabra aparece.
    """

    resultado = {}

    for palabra in palabras_a_filtrar:
        lista_palabras = mensaje.split(" ")
        palabras_filtradas = list(filter(lambda p: p==palabra, lista_palabras))
        resultado[palabra] = resultado.get(palabra,0) + len(palabras_filtradas)

    return resultado

def definir_archivo_reporte():
    """
    Permite ingresar una ruta hacía un archivo con función de reporte, a partir de un input. En caso de que la ruta sea invalida, se deberá ingresar una valida para finalizar la función.
    """

    while True:
        try:
            archivo = input("Ingrese el archivo destino para guardar el reporte: ")
            return archivo
        except FileNotFoundError:
            print("Error al ingresar nombre del archivo. Intente nuevamente")


def obtener_contactos(ruta):
    """
    Dado un archivo de chat, obtengo una lista de los contactos allí presentes.
    """

    contactos = []

    with open(ruta) as chat:
        for linea in chat:
            if not es_mensaje_valido(linea):
                continue
            contacto = obtener_informacion_de_linea(linea)[0]
            if contacto not in contactos:
                contactos.append(contacto)

        return contactos

def seleccionar_contacto(contactos:list)->str:
    """
    Se imprimen los contactos de un chat y se permite mediante un input escoger al contacto por indice del mismo. Devuelve el nombre del contacto seleccionado.
    """

    print("\n\033[1mContactos:\033[0m\n")
    for i, contacto in enumerate(contactos):
        print(f"\t{i}. {contacto}")

    while True:
        i_contacto_seleccionado = input("\nIngrese el índice del contacto para generar el mensaje: ")

        if not i_contacto_seleccionado.isdecimal() or int(i_contacto_seleccionado) not in range(len(contactos)):
            print("El índice ingresado es ínvalido. Intente nuevamente")
            continue

        return contactos[int(i_contacto_seleccionado)]


def filtrar_mensajes_de_contacto(ruta:str, contacto:str)->[str]:
    mensajes = []

    with open(ruta) as chat:

        for linea in chat:
            if not es_mensaje_valido(linea):
                continue

            contacto_actual, mensaje = obtener_informacion_de_linea(linea)
            
            if contacto_actual != contacto:
                continue

            mensajes.append(mensaje)

    return mensajes

def obtener_cantidad_de_inicios(mensajes:list)->dict:
    """
    A partir de una lista de mensajes, obtengo un diccionario cuyas claves indican todos los inicios de mensajes detectados y cuyos valores, indican la cantidad de veces que aparecen.

    Se descartan palabras que terminen con "." con la intención de generar mensajes más largos.
    """

    cantidad_de_inicios = {}

    for mensaje in mensajes:
        try:
            inicio = mensaje.split()[0]
        except IndexError:
            pass

        if inicio[-1] == ".": continue
        
        cantidad_de_inicios[inicio] = cantidad_de_inicios.get(inicio, 0) + 1

    return cantidad_de_inicios

def obtener_palabra_probable(cantidad_palabras:dict)->dict:
    """
    Convierte diccionario que describe la cantidad de veces que aparece cada palabra por mensaje, a un diccionario que indica la probabilidad de que esa palabra aparezca en una Cadena de Markov.
    """

    palabras = list(cantidad_palabras.keys())
    cantidad_ponderada = map(lambda c : c/len(cantidad_palabras), cantidad_palabras.values())

    palabra_probable = random.choices(palabras, weights=cantidad_ponderada, k=1)[0]
    return palabra_probable

def obtener_palabras_siguientes(palabra_filtro:str, mensajes:[str])->dict:
    """
    Dada una palabra y una lista de mensajes, obtengo un diccionario cuyas claves indican las palabras siguientes a mi palabra inicial y cuyos valores indican la cantidad de veces que dicha palabra siguiente apareció en la totalidad de mensajes. 
    """

    palabras_siguientes = {}

    for msj in mensajes:
        palabras_msj = msj.split()
        for i, palabra in enumerate(palabras_msj):
            if palabra == palabra_filtro and i + 1 < len(palabras_msj):
                p_siguente = palabras_msj[i + 1]
                palabras_siguientes[p_siguente] = palabras_siguientes.get(p_siguente, 0) +1

    return palabras_siguientes