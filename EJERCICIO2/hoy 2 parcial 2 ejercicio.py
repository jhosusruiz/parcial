# 2 ejercicio clases de jugador

# la clase de la persona
class Persona:
    def __init__(self, nombre, nif, fecha_nacimiento):
        self.nombre = nombre
        self.nif = nif
        self.fecha_nacimiento = fecha_nacimiento

# la clase del jugador
class Jugador:
    def __init__(self, numero_federacion, persona):
        self.numero_federacion = numero_federacion
        self.persona = persona
    
    def mostrar_datos(self):
        print("--- Datos del Jugador ---")
        print("Nombre: " + str(self.persona.nombre))
        print("NIF: " + str(self.persona.nif))
        print("Fecha de Nacimiento: " + str(self.persona.fecha_nacimiento))
        print("Numero de Federacion: " + str(self.numero_federacion))

# persona creada
persona1 = Persona("Jhosua Ruiz", "12345678A", "07/11/2007")

# jugador creado con la persona creada
jugador1 = Jugador(1001, persona1)

# mostrar el tipo de informacion acerca del jugador{}
jugador1.mostrar_datos()