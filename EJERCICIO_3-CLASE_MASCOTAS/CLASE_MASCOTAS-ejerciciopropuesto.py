class Mascota:

    def __init__(self, nombre: str, edad: int, color: str):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def imprimir_detalles(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad} años")
        print(f"Color: {self.color}")

class Perro(Mascota):
    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool):
        super().__init__(nombre, edad, color)
        self.peso = peso
        self.muerde = muerde

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Peso: {self.peso} kg")
        print(f"¿Muerde?: {'Sí' if self.muerde else 'No'}")

    @staticmethod
    def sonido():
        print("Sonido: Los perros ladran.")

class Gato(Mascota):

    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float):
        super().__init__(nombre, edad, color)
        self.altura_salto = altura_salto
        self.longitud_salto = longitud_salto

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Altura de salto: {self.altura_salto} metros")
        print(f"Longitud de salto: {self.longitud_salto} metros")

    @staticmethod
    def sonido():
        print("Sonido: Los gatos maúllan y ronronean.")

class PerroPequeno(Perro):

    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: str):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Tamaño: Pequeño")
        print(f"Raza: {self.raza}")

class PerroMediano(Perro):

    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: str):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Tamaño: Mediano")
        print(f"Raza: {self.raza}")

class PerroGrande(Perro):

    def __init__(self, nombre: str, edad: int, color: str, peso: float, muerde: bool, raza: str):
        super().__init__(nombre, edad, color, peso, muerde)
        self.raza = raza

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Tamaño: Grande")
        print(f"Raza: {self.raza}")

class GatoSinPelo(Gato):

    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: str):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Tipo de Pelo: Sin Pelo")
        print(f"Raza: {self.raza}")

class GatoPeloLargo(Gato):

    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: str):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Tipo de Pelo: Pelo Largo")
        print(f"Raza: {self.raza}")

class GatoPeloCorto(Gato):

    def __init__(self, nombre: str, edad: int, color: str, altura_salto: float, longitud_salto: float, raza: str):
        super().__init__(nombre, edad, color, altura_salto, longitud_salto)
        self.raza = raza

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print(f"Tipo de Pelo: Pelo Corto")
        print(f"Raza: {self.raza}")

class TiendaMascotas:
    @staticmethod
    def main():
        print("Detalles de Mascotas")

        perro1 = PerroPequeno("GUARO", 3, "Marrón", 5.5, False, "Caniche")
        print("\nDetalles del Perro Pequeño:")
        perro1.imprimir_detalles()
        perro1.sonido() 
        perro2 = PerroGrande("Max", 5, "Negro y Marrón", 40.0, True, "Doberman")
        print("\nDetalles del Perro Grande:")
        perro2.imprimir_detalles()
        Perro.sonido() 

        gato1 = GatoPeloLargo("Persia", 2, "Blanco", 1.8, 2.5, "Angora")
        print("\nDetalles del Gato de Pelo Largo:")
        gato1.imprimir_detalles()
        gato1.sonido() 
        gato2 = GatoSinPelo("Bills", 1, "Gris", 1.5, 2.0, "Esfinge")
        print("\nDetalles del Gato Sin Pelo:")
        gato2.imprimir_detalles()
        Gato.sonido() 

if __name__ == "__main__":
    TiendaMascotas.main()
