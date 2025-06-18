# ¡Bienvenido! Este es un programa simple que interactúa contigo 
# y te dice si eres mayor de edad o no.

# Primero, vamos a preguntarte tu nombre y guardarlo en una variable
nombre = input("¿Cuál es tu nombre? ")

# Ahora te saludamos de manera personalizada usando una f-string
# (es como una plantilla que nos permite insertar variables en el texto)
print(f"¡Hola, {nombre}! Bienvenido al mundo de Python.")

# Aquí preguntamos tu edad
# Ojo: input() siempre devuelve texto, así que edad será un string
edad = input("¿Cuál es tu edad? ")

# Verificamos si eres mayor de edad
# NOTA: Esto podría mejorarse convirtiendo 'edad' a número entero con int()
if edad >= "18":
    print("Eres mayor de edad.")
else:
    # Si no eres mayor de 18, entonces...
    print("Eres menor de edad.")
