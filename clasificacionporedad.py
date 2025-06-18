# Pedir nombre y edad al usuario
nombre = input("Por favor, dime tu nombre: ")
try:
    edad = int(input("Ahora ingresa tu edad (solo números): "))
except ValueError:
    print("Oops, parece que ingresaste algo incorrecto. ¡Recuerda escribir solo números!")
    exit()

# Clasificar según la edad
if edad < 18:
    categoria = "menor de edad"
elif edad < 60:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

# Mostrar mensaje personalizado
print(f"\nHola, {nombre}! Según tu edad, perteneces a la categoría '{categoria}'.")

# Preguntar si desea ver un resumen general de las categorías
ver_resumen = input("¿Te gustaría ver un resumen de todas las categorías? (s/n): ").strip().lower()

if ver_resumen == 's':
    print("\n--- Categorías de Edad ---")
    print("Menor de edad: menos de 18 años")
    print("Adulto: de 18 a 59 años")
    print("Adulto mayor: 60 años o más")
else:
    print("\nResumen omitido. ¡Gracias por participar!")