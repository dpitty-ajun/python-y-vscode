diccionario_pelicula = {
    "titulo": "Iron Man 2",
    "fecha": 2010,
    "rating": 7.0
}

print("Hay dos formas de traer el valor de una propiedad en un diccionario")
print("La primera es por la sintaxis de brakets []. Título:", diccionario_pelicula["titulo"])
print("\nLa segunda es con el método get que permite poner un valor por defecto. Título:", diccionario_pelicula.get("titulo"))
print("Si se trata de traer una propieadad que no existe se usa el valor por defecto en vez de levantar una excepción. Valor por defecto:", diccionario_pelicula.get("personajes", "n/a"))


diccionario_pelicula["personajesPrincipales"] = ["Tony Stark", "Pepper Potts", "James Rhodes"]
print("Así se asigna un una llave valor", diccionario_pelicula)

personajes = diccionario_pelicula.pop("personajesPrincipales")
print("El pop borra la propiedad del diccionario:", diccionario_pelicula)
print("Y el método devuelve el valor barrado, el cual se puede almacenar en una variable:", personajes)

lista_items = list(diccionario_pelicula.items()) # items devuelve un objeto iterable, es más fácil de usar en una lista en este caso
llave, valor = lista_items[0] # sintaxis de desempaquetado de tuplas
print("\nMétodo items trae tuplas de la llave y valor para cada propiedad")
print("Llave: {}\nValor: {}".format(llave, valor))

# ver desempaquetado (**)?