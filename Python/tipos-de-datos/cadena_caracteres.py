cadena_caracteres = "Hola Mundo!"

numero_caracteres = len(cadena_caracteres)
print("cadena_caracteres tiene {} caracteres", numero_caracteres)

en_minuscula = cadena_caracteres.lower()
en_mayuscula = cadena_caracteres.upper()
print("\nEn minúscula:", en_minuscula)
print("En mayúscula:", en_mayuscula)

nombre = "David"
cadena_con_reemplazo = cadena_caracteres.replace("Mundo", nombre)
print("\nReemplaza 'Mundo' por 'David':", cadena_con_reemplazo)


partes = cadena_caracteres.split(" ")
print("\nSplit convirte la cadena en una lista")
print(partes)

partes_unidas = "-".join(partes)
print("\nJoin une valores de una lista con un delimitador:", partes_unidas)

print("\n\nFunciones para validar cadena de caracteres:")

print("\ncadena_caracteres termina en 'Mundo'?:", cadena_caracteres.endswith("Mundo"))
print("cadena_caracteres termina en '!'?:", cadena_caracteres.endswith("!"))

print("\ncadena_caracteres empieza con 'Mundo'?:", cadena_caracteres.endswith("Mundo"))
print("cadena_caracteres empieza con 'Hola'?:", cadena_caracteres.startswith("Hola"))

mundo_en_cadena = "Mundo" in cadena_caracteres
print("\nLa palabra 'Mundo' está en cadena_caracteres:", mundo_en_cadena)


print("\n\nisdecimal revisa si sólo hay números en la cadena de caracteres")
print("'{}' tiene son sólo números?: {}".format(cadena_caracteres, cadena_caracteres.isdecimal()))

valor = "1234"
print("'{}' tiene son sólo números?: {}".format(valor, valor.isdecimal()))

valor_entero = int(valor)
print("valor_entero es de tipo:", type(valor_entero))
