def leer_dialogo(nombre_archivo):
    '''
    DOC: Completar
    '''
    palabras_x_persona = {}

    with open(nombre_archivo) as dialogos:

        for linea in dialogos:
            persona, frase = linea.split(": ")

            palabras = frase.split(" ")
            if(persona not in palabras_x_persona):
                palabras_x_persona[persona]= {}

            for palabra in palabras:
                palabra = palabra.rstrip('\n')
                palabras_x_persona[persona][palabra] = palabras_x_persona[persona].get(palabra,0)+1
        
    return palabras_x_persona
