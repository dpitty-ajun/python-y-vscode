import json
from pprint import pprint


def mejor_dc_y_marvel(dict_dc, dict_marvel):
    mejor_dc = _mejor_rating(dict_dc)
    mejor_marvel = _mejor_rating(dict_marvel)
    return (mejor_dc, mejor_marvel)

def _mejor_rating(registros):
    mejor = None
    for registro in registros:
        if (mejor == None):
            mejor = registro
        elif (mejor["rating"] < registro["rating"]):
            mejor = registro
    return mejor

def filtro_peliculas(peliculas, rating_minimo):
    resultados = []
    for pelicula in peliculas:
        if pelicula["rating"] >= rating_minimo:
            resultados.append(pelicula)
    return resultados

def carga_diccionarios_dc_marvel():
    archivo_dc = open("peliculas-dc.json", "r")
    archivo_marvel = open("peliculas-marvel.json", "r")

    lista_dc = json.load(archivo_dc)
    lista_marvel = json.load(archivo_marvel)

    archivo_dc.close()
    archivo_marvel.close()

    return (lista_dc, lista_marvel)

def num_pelicula_por_personaje(peliculas):
    resultado = {}
    for pelicula in peliculas:
        for personaje in pelicula["personajesPrincipales"]:
            if personaje not in resultado:
                resultado[personaje] = 0
            resultado[personaje] += 1
                # resultado[personaje] = []
            # resultado[personaje].append(pelicula)
    return resultado


if __name__ == "__main__":
    lista_dc, lista_marvel = carga_diccionarios_dc_marvel() # tuplas
    mejor_dc, mejor_marvel = mejor_dc_y_marvel(lista_dc, lista_marvel) # tuplas
    print("\nLa película de DC con mejor rating es:", mejor_dc)
    print("\nLa película de Marvel con mejor rating es:", mejor_marvel)

    todas_las_peliculas = [
        *lista_dc,
        *lista_marvel
    ]

    resultados = filtro_peliculas(todas_las_peliculas, 8.5)
    print("\nPeliculas con raiting mayor o igual a 8.5")
    pprint(resultados)

    diccionario_personajes = num_pelicula_por_personaje(lista_dc)
    print("\nPeliculas por personaje")
    pprint(diccionario_personajes)
# for cada registro, hacer un array de las palabras del título
