import sys

from calculadora import OPERADORES_VALIDOS, calcular


# Verifica si se proporcionaron suficientes argumentos
if len(sys.argv) < 4:
    print("Favor intentar de nuevo con todos los parámetros:")
    print("python <operando1> <operando2> <operador>")
    exit

# Obtén los parámetros de la línea de comandos
operando1 = sys.argv[1]
operando2 = sys.argv[2]
operador = sys.argv[3]

# Validar parámetros
if (not operando1.isdecimal() or not operando2.isdecimal()):
    print("Los operandos deben ser números sin punto decimal")
    exit
else:
    operando1 = int(operando1)
    operando2 = int(operando2)

if (operador not in ["suma", "resta", "multiplicador", "divisor"]):
    operadores_validos_str = ", ".join(OPERADORES_VALIDOS)
    print("El operador es incorrecto, estos son los operadores válidos:", operadores_validos_str)
    exit

# Realiza cálculo
resultado = calcular(operando1, operando2, operador)
print(resultado)

