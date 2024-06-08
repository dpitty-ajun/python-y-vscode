frutas = ["manzana", "naranja", "plátano", "uva", "pera"] # , "sandía", "melón", "kiwi", "mango", "fresa"]
verduras = ["zanahoria", "brócoli", "apio", "cebolla", "tomate"] # , "calabaza", "pepino", "coliflor", "pimiento", "apio"]

print("Tenemos {} Frutas".format(len(frutas)))
print("Tenemos {} Verduras".format(len(verduras)))

print("\nLos valores de la lista se accesan por índice, iniciando en cero.")
print("El primer valor de la lista de frutas es:""", frutas[0])

ultima_fruta = frutas.pop()
print("\nLa última fruta es", ultima_fruta)

verduras.sort() # orden ascendente por defecto
primer_verdura = verduras.pop(0)
print("\nLa primer verdura en orden alfabético es", primer_verdura)
print("\nLa lista de verduras ya no tiene apio por el pop:", verduras)

verduras.append("verdura nueva")
print("\nAppend agrega al final de la lista", verduras)

verduras.insert(2, "3ra verdura")
print("\nInsert permite escoger dónde se agrega el valor, índice empieza en cero", verduras)

todos_juntos = frutas.copy()
todos_juntos.extend(verduras)
print("\nEstas son todos los valores juntos", todos_juntos)



lista_con_duplicados = {2, 3, 5, 4, 0, 9, 4, 5, 0, 1, 2, 3}
set_numeros = set(lista_con_duplicados)
print("Los sets no permiten duplicados", set_numeros)

set_str = {"a", "a", "b", "c", "c"} # sintaxis: como la lista pero con corchetes
print("El orden arbitrario", set_str)

set_numeros.add(1)
set_numeros.add(16)
print("El método 'add' revisa que el elemento que se está agregando no exista en el set", set_numeros)
set_str.remove('b')
print("El método remove es para quitar elementos del set", set_str)



print("\nTratar de acceder un índice que no existe en la lista da el siguiente error:")
frutas[100]
