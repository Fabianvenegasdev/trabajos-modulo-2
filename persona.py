import re  # Para validar el formato del correo electrónico


class Persona:
    def __init__(self, nombre, edad, correo_electronico):
        """
        Inicializa una nueva instancia de Persona con los datos proporcionados.
        """
        self.nombre = nombre
        self.edad = edad
        self.correo_electronico = correo_electronico

    def mostrar_datos(self):
        """
        Muestra en pantalla los datos de la persona: nombre, edad y correo.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Correo electrónico: {self.correo_electronico}")

    def validar_correo(self):
        """
        Verifica si el correo electrónico tiene un formato válido usando una expresión regular.
        Retorna True si es válido, False en caso contrario.
        """
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, self.correo_electronico) is not None

    def actualizar_datos(self, nombre=None, edad=None, correo_electronico=None):
        """
        Permite actualizar uno o varios atributos de la persona.
        Solo se modifican los valores que se pasan como argumento.
        """
        if nombre:
            self.nombre = nombre
        if edad:
            self.edad = edad
        if correo_electronico:
            self.correo_electronico = correo_electronico

    def es_mayor_de_edad(self):
        """
        Devuelve True si la persona tiene 18 años o más.
        """
        return self.edad >= 18