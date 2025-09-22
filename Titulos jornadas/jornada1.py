# Abrir archivo y leer todas las líneas

archivo = open("texto_tarea.txt", "r")
lineas = archivo.readlines()
archivo.close()

digitos = "0123456789"
MAYUS   = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
minus   = "abcdefghijklmnñopqrstuvwxyz"

# Quitar espacios y saltos de linea al inicio

for linea in lineas:
    while len(linea) > 0 and (linea[0] == " " or linea[0] == "\n"):
        linea = linea[1:]

# Quitar espacios y saltos de linea al final
    while len(linea) > 0 and (linea[-1] == " " or linea[-1] == "\n"):
        linea = linea[:-1]

    if len(linea) == 0:
        continue

# Buscar los dígitos iniciales
    i = 0
    while i < len(linea) and linea[i] in digitos:
        i = i+1

# Revisar si hay ".-" después de los dígitos
    if i > 0 and i+1 < len(linea) and linea[i] == "." and linea[i+1] == "-":

# Verificar que la línea no tenga minúsculas
        tiene_minus = False
        j = 0
        while j < len(linea):
            if linea[j] in minus:
                tiene_minus = True
                break
            j = j+1
        if not tiene_minus:


# Imprimir títulos
           print(linea)

