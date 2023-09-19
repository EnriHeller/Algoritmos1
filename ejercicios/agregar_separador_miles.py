def agregar_separador_miles(numero_str):
    # Verificar si el número es negativo
    es_negativo = False
    if numero_str.startswith('-'):
        es_negativo = True
        numero_str = numero_str[1:]  # Eliminar el signo negativo

    # Separar la parte entera de la parte decimal (si existe)
    partes = numero_str.split('.')
    parte_entera = partes[0]
    parte_decimal = partes[1] if len(partes) > 1 else ''

    # Agregar separadores de miles a la parte entera
    separado_miles = []
    while parte_entera:
        separado_miles.append(parte_entera[-3:])
        parte_entera = parte_entera[:-3]

    # Revertir la lista y unir las partes separadas con puntos
    resultado = '.'.join(reversed(separado_miles))

    # Agregar el signo negativo (si es necesario) y la parte decimal (si existe)
    if es_negativo:
        resultado = '-' + resultado
    if parte_decimal:
        resultado += '.' + parte_decimal

    return resultado
numero = input()
# Ejemplos de uso:
print(agregar_separador_miles(numero))        # '12.345'

