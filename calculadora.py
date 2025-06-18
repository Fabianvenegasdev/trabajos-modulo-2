def calculadora():
    """
    Función principal que ejecuta una calculadora básica.
    Permite realizar operaciones de suma, resta, multiplicación y división.
    Maneja errores comunes como entrada no numérica, división por cero y operadores inválidos.
    """
    try:
        # Pedir los números al usuario
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))

        # Pedir el operador deseado
        operacion = input("Ingresa la operación que deseas realizar (+, -, *, /): ")

        # Realizar la operación según el operador ingresado
        if operacion == '+':
            resultado = numero1 + numero2
        elif operacion == '-':
            resultado = numero1 - numero2
        elif operacion == '*':
            resultado = numero1 * numero2
        elif operacion == '/':
            # Verificar división por cero
            if numero2 == 0:
                raise ZeroDivisionError("No se puede dividir entre cero.")
            resultado = numero1 / numero2
        else:
            # Si el operador no es uno válido
            raise ValueError(f"Operador '{operacion}' no válido. Usa +, -, * o /.")

        # Mostrar el resultado final
        print(f"El resultado de {numero1} {operacion} {numero2} es: {resultado}")

    except ValueError as error_valor:
        # Captura errores al convertir a número o por operador inválido
        print(f"Error en los datos ingresados: {error_valor}")
    except ZeroDivisionError as error_division:
        # Captura intentos de dividir por cero
        print(f"Error matemático: {error_division}")
    finally:
        # Este bloque siempre se ejecuta, independientemente de si hubo errores
        print("La operación ha terminado.")

# Llamamos a la función para ejecutar la calculadora
calculadora()