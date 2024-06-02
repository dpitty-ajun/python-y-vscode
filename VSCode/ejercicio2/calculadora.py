OPERADORES_VALIDOS = ["suma", "resta", "multiplicador", "divisor"]


def calcular(operando1, operando2, operador):
    """ Metodo para calcular dos operandos """
    if (operador == "suma"):
        return _suma(operando1, operando2)
    elif (operador == "resta"):
        return _resta(operando1, operando2)
    elif (operador == "multiplicador"):
        return _multiplicacion(operando1, operando2)
    elif (operador == "divisor"):
        return _division(operando1, operando2)


# Funciones privadas

def _suma(operando1, operando2):
    """ Función de suma """
    return operando1 + operando2


def _resta(operando1, operando2):
    """ Función de resta """
    return operando1 - operando2


def _multiplicacion(operando1, operando2):
    """ Función de multiplicacion """
    return operando1 * operando2


def _division(operando1, operando2):
    """ Función de division """
    return operando1 / operando2
