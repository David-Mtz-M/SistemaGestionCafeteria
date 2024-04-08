# Sistema de Gestión de Cafetería 
# Programador: David Martínez Molina  A01735425


def addBebida(bebida):
    if ',' not in bebida:
        return False
    
    nombre, tamanos = map(str.strip, bebida.split(",", 1))
    nombre = nombre.translate(str.maketrans("áéíóú", "aeiou"))

    # Validación del nombre
    if not (nombre.isalpha() and 2 <= len(nombre) <= 15):
        return False
    
    tamanos = tamanos.replace(" ", "").split(",")
    
    # Validación de la cantidad de tamaños
    if not (1 <= len(tamanos) <= 5):
        return False
    
    tamanos_enteros = []
    
    # Validación de los tamaños
    for tam in tamanos:
        if not tam.isdigit() or not (1 <= int(tam) <= 48):
            return False
        if tamanos_enteros and int(tam) <= tamanos_enteros[-1]:
            return False
        tamanos_enteros.append(int(tam))
        
    return True

