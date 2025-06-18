# hola.py
Descripción del Programa
Este script interactúa con el usuario preguntando su nombre y edad, y luego le indica si es mayor o menor de edad.

¿Qué hace?
Saluda al usuario por su nombre.
Pide la edad como entrada.
Compara la edad ingresada y muestra un mensaje indicando si es mayor o menor de edad.

Estructura básica
Usa input() para obtener datos del usuario.
Muestra mensajes personalizados con print() y f-strings.
Utiliza una estructura condicional (if/else) para evaluar la edad.

Notas importantes
La edad se recibe como texto y no se convierte a número, lo que puede causar comparaciones incorrectas.
No tiene manejo de errores. Es útil como ejemplo básico para principiantes.

----------------------------------------------------------------

# clasificacionporedad.py
Este script saluda al usuario, le pregunta su edad y lo clasifica en una categoría: menor de edad, adulto o adulto mayor. También ofrece un resumen opcional de las categorías usadas.

¿Qué hace?
Pide el nombre del usuario.
Solicita su edad y valida que sea un número.
Clasifica la edad en tres categorías.
Muestra un mensaje personalizado con la categoría correspondiente.
Ofrece un resumen de las categorías si el usuario lo desea.

Características clave
Uso de try/except para evitar errores al ingresar la edad.
Clasificación por rangos de edad.
Opción interactiva para mostrar más información o finalizar.

Notas importantes
El programa termina si el usuario no ingresa un número válido como edad.

--------------------------------------------------------------


# utilidades_matematicas.py
Este script contiene un conjunto de funciones básicas para realizar cálculos matemáticos comunes, como áreas de figuras geométricas, factoriales y verificación de números primos.

¿Qué hace?
Calcula el área de un círculo, rectángulo y triángulo.
Calcula el factorial de un número.
Determina si un número es primo.

Funciones disponibles
area_circulo(radio): Devuelve el área usando el radio dado.
area_rectangulo(ancho, alto): Calcula el área con base y altura.
area_triangulo(base, altura): Encuentra el área usando base y altura.
factorial(numero): Retorna el factorial del número ingresado.
es_primo(numero): Verifica si un número es primo (True o False).

Notas importantes
Todas las funciones asumen entradas válidas y numéricas.
No incluye manejo de errores, por lo que se recomienda usarlas con valores correctos.

----------------------------------------------------------------

# inventario.py
Este script implementa un sistema básico de gestión de inventario. Permite agregar, eliminar y actualizar productos, listar por categoría, calcular el valor total del inventario y exportar los datos a un archivo CSV.

Funcionalidades principales
Agregar productos : Nombre, cantidad, precio y categoría.
Eliminar productos : Por su nombre.
Actualizar información : Cantidad o precio de un producto existente.
Listar productos por categoría : Muestra todos los productos de una categoría específica.
Calcular valor total : Suma el valor total del inventario (cantidad × precio).
Exportar a CSV : Guarda todo el inventario en un archivo para compartir o analizar después.

Características clave
Uso de un diccionario para almacenar el inventario en memoria.
Validaciones básicas para evitar valores negativos o productos duplicados.
Manejo de errores al guardar archivos.
Ejemplo de uso incluido para probar rápidamente las funciones.

Notas importantes
Este programa está pensado como base para sistemas más complejos de control de inventarios.

-----------------------------------------------------------------

# persona.py
Este script define una clase básica llamada Persona que permite almacenar y gestionar información sobre una persona: nombre, edad y correo electrónico.

Características principales
Almacena los datos de una persona.
Muestra esos datos por pantalla.
Valida el formato del correo electrónico usando expresiones regulares.
Permite actualizar uno o varios atributos.
Verifica si la persona es mayor de edad (18 años o más).

Funcionalidades disponibles
__init__() – Inicializa una nueva persona con nombre, edad y correo.
mostrar_datos() – Imprime los datos de la persona.
validar_correo() – Comprueba si el correo tiene un formato válido.
actualizar_datos() – Modifica uno o más datos de la persona.
es_mayor_de_edad() – Devuelve True si la persona tiene 18 años o más.

Notas importantes
Este código no incluye manejo de errores al crear la persona, por lo que se asume que los datos son válidos al inicio.

----------------------------------------------------------------

# calculadora.py
Este script implementa una calculadora básica que permite realizar operaciones aritméticas comunes: suma, resta, multiplicación y división.

Funcionalidades principales
Solicita dos números al usuario.
Pide el tipo de operación a realizar.
Realiza la operación y muestra el resultado.
Incluye manejo de errores para:
Entradas no numéricas.
División por cero.
Operadores inválidos.

Características clave
Código sencillo y fácil de entender.
Uso de bloques try/except para controlar errores comunes.
Mensajes claros para mejorar la experiencia del usuario.
Ideal para aprender sobre funciones, entrada/salida y manejo de excepciones en Python.

Notas importantes
Es una versión simple y funcional, pensada para principiantes o como base para proyectos más grandes.
No permite repetir operaciones automáticamente, solo ejecuta una vez por llamada a la función.

------------------------------------------------------------

# Logros en este modulo:

Durante este módulo trabajé en varios proyectos sencillos que me ayudaron a aprender los conceptos básicos de programación en Python. Cada uno fue una práctica diferente, pero todos me permitieron avanzar paso a paso.

Lo que aprendí:

Uso de variables, condicionales y bucles.
Manejo de funciones para organizar código.
Programación orientada a objetos con la clase Persona.
Validación de datos y manejo de errores con try/except.
Uso de estructuras de datos como listas y diccionarios.
Exportación de datos a archivos CSV.
Aplicación de expresiones regulares para validar correos.

Logros principales:
Creé una calculadora básica funcional.
Desarrollé un sistema simple de gestión de inventario.
Implementé mi primera clase en Python.
Mejoré en el uso de funciones reutilizables y validaciones.

Habilidades desarrolladas:
Resolver problemas usando lógica de programación.
Escribir código más limpio y organizado.
Trabajar con entrada del usuario y gestionar posibles errores.
Usar herramientas básicas de Python para proyectos prácticos.

------------------------------------------------------------------

# Reflexiones realizadas en el módulo:

Al comenzar este módulo, me enfrenté a muchos desafíos que no solo eran técnicos, sino también mentales. Había días en los que veía el código y sentía que no entendía nada. Las palabras como "función", "clase" o "método" sonaban lejanas y abstractas. Pero poco a poco, con cada ejercicio, fui comprendiendo que programar no es tanto memorizar reglas como aprender a pensar de otra manera: paso a paso, con paciencia y mucha práctica.

Los primeros ejercicios, como el saludo al usuario o la clasificación por edad, me ayudaron a ganar confianza. Me di cuenta de que podía comunicarme con la computadora, que mis líneas de código podían tener sentido y propósito. Aunque al principio usaba variables sin entender bien cómo funcionaban, con el tiempo comencé a ver cómo organizar mejor las ideas y estructurar mi pensamiento lógico.

Cuando empecé a trabajar con funciones, noté que el código se volvía más limpio y reutilizable. Fue un momento clave: dejé de escribir todo dentro del mismo bloque y empecé a modularizar, a pensar en pequeñas piezas que juntas formaban algo más grande. Esto fue fundamental cuando trabajé en utilidades matemáticas o en la calculadora, donde separar cada operación en su propia función me permitió manejar mejor la complejidad.

La introducción a la programación orientada a objetos fue otro punto importante. Al crear la clase Persona, al principio me costó entender qué era lo que realmente representaba un objeto, pero luego vi que no era más que una forma de organizar datos y acciones relacionadas entre sí. Eso me abrió la mente a nuevas formas de diseñar programas, más cercanas a cómo vemos el mundo: con cosas que tienen propiedades y comportamientos.

También aprendí a convivir con los errores. En un principio, ver un mensaje rojo de error me frustraba mucho. Pensaba que había hecho algo malo. Pero ahora entiendo que los errores no son fallas, sino guías. El try/except no solo sirve para evitar que el programa se rompa, también me enseñó a anticiparme a posibles fallos del usuario y a mejorar la experiencia de uso.

El proyecto del inventario fue uno de los más completos. Allí tuve que integrar varias habilidades: usar diccionarios, validar entradas, exportar información… Y aunque no es un sistema profesional, me dio una idea de cómo podría desarrollarse una aplicación real. Ver cómo todo funcionaba junto me llenó de satisfacción.

Lo más importante que llevo de estos ejercicios es haber aprendido a no rendirme ante la dificultad. Programar no siempre es fácil, pero cada vez que logro resolver un problema (por pequeño que sea) siento que estoy avanzando. Cada línea de código ya no me asusta; ahora sé que detrás de ella hay una idea, una solución, un aprendizaje.

Este módulo no solo me enseñó Python, también me enseñó paciencia, constancia y a valorar los pequeños avances. Ahora tengo una base sólida, pero sobre todo tengo confianza en que puedo seguir aprendiendo, seguir mejorando y, poco a poco, construir cosas aún más grandes.
