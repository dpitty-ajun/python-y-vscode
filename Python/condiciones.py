persona = {
    "nombre": "Juan",
    "edad": 30,
    "profesion": "ingeniero",
}

# persona = {
#     "nombre": "María",
#     "edad": 15,
# }

# persona = {
#     "nombre": "Ana",
#     "edad": 11,
# }

edad = persona["edad"]
if edad >= 18:
    print("{} es mayor de edad.".format(persona['nombre']))
elif edad >= 12:
    print("{} es adolescente.".format(persona['nombre']))
else:
    print("{} es niño o niña.".format(persona['nombre']))


if "profesion" in persona:
    print("{} es {}.".format(persona['nombre'], persona['profesion']))
