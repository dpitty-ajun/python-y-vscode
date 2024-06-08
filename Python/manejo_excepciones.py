try:
    # Código que podría generar una excepción
    numero = int(input("Introduce un número: "))
    resultado = 10 / numero
    print("El resultado es:", resultado)
except ZeroDivisionError:
    # Manejo de la excepción específica para división por cero
    print("Error: No puedes dividir entre cero.")
except ValueError:
    # Manejo de la excepción específica para un valor no válido (por ejemplo, si el usuario no ingresa un número)
    print("Error: Debes ingresar un número válido.")
except Exception as e:
    # Manejo de cualquier otra excepción no anticipada
    print("Ha ocurrido un error:", e)