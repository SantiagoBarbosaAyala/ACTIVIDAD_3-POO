import enum

class Inmueble:

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str):
        self._identificador_inmobiliario = identificador_inmobiliario
        self._area = area
        self._direccion = direccion
        self._precio_venta = 0.0  

    def calcular_precio_venta(self, valor_area: float) -> float:
        self._precio_venta = self._area * valor_area
        return self._precio_venta

    def imprimir(self):
        print(f"Identificador inmobiliario = {self._identificador_inmobiliario}")
        print(f"Area = {self._area}")
        print(f"Dirección = {self._direccion}")
        print(f"Precio de venta = ${self._precio_venta:,.2f}")

class InmuebleVivienda(Inmueble):

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int):
        super().__init__(identificador_inmobiliario, area, direccion)
        self._numero_habitaciones = numero_habitaciones
        self._numero_banos = numero_banos

    def imprimir(self):
        super().imprimir()
        print(f"Número de habitaciones = {self._numero_habitaciones}")
        print(f"Número de baños = {self._numero_banos}")

class Casa(InmuebleVivienda):

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int):
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos)
        self._numero_pisos = numero_pisos

    def imprimir(self):
        super().imprimir()
        print(f"Número de pisos = {self._numero_pisos}")

class Apartamento(InmuebleVivienda):

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int):
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos)

    def imprimir(self):
        super().imprimir() 

class CasaRural(Casa):

    _VALOR_AREA = 1500000.0  

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int,
                 distancia_cabecera: int, altitud: int):
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
        self._distancia_cabecera = distancia_cabecera
        self._altitud = altitud

    def imprimir(self):
        super().imprimir()
        print(f"Distancia a la cabecera municipal = {self._distancia_cabecera} km.")
        print(f"Altitud sobre el nivel del mar = {self._altitud} metros.")
        print()

class CasaUrbana(Casa):

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int):
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)

    def imprimir(self):
        super().imprimir() 
        print() 

class ApartamentoFamiliar(Apartamento):

    _VALOR_AREA = 2000000.0  

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, valor_administracion: int):
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos)
        self._valor_administracion = valor_administracion

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = ${self._valor_administracion:,.2f}")
        print()

class Apartaestudio(Apartamento):

    _VALOR_AREA = 1500000.0  
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str):
        super().__init__(identificador_inmobiliario, area, direccion, 1, 1)

    def imprimir(self):
        super().imprimir() 
        print()

class TipoLocal(enum.Enum):
    INTERNO = 1
    CALLE = 2

class Local(Inmueble):

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str, tipo_local: TipoLocal):
        super().__init__(identificador_inmobiliario, area, direccion)
        self._tipo_local = tipo_local

    def imprimir(self):
        super().imprimir()
        print(f"Tipo de local = {self._tipo_local.name}") 

class LocalComercial(Local):

    _VALOR_AREA = 3000000.0  
    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 tipo_local: TipoLocal, centro_comercial: str):
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self._centro_comercial = centro_comercial

    def imprimir(self):
        super().imprimir()
        print(f"Centro comercial = {self._centro_comercial}")
        print()

class Oficina(Local):

    _VALOR_AREA = 3500000.0  

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 tipo_local: TipoLocal, es_gobierno: bool):
        super().__init__(identificador_inmobiliario, area, direccion, tipo_local)
        self._es_gobierno = es_gobierno

    def imprimir(self):
        super().imprimir()
        print(f"Es oficina gubernamental = {self._es_gobierno}")
        print()

class CasaConjuntoCerrado(CasaUrbana):

    _VALOR_AREA = 2500000.0 

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int,
                 numero_pisos: int, valor_administracion: int, tiene_piscina: bool,
                 tiene_campos_deportivos: bool):
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
        self._valor_administracion = valor_administracion
        self._tiene_piscina = tiene_piscina
        self._tiene_campos_deportivos = tiene_campos_deportivos

    def imprimir(self):
        super().imprimir()
        print(f"Valor de la administración = {self._valor_administracion}")
        print(f"Tiene piscina? = {self._tiene_piscina}")
        print(f"Tiene campos deportivos? = {self._tiene_campos_deportivos}")
        print()

class CasaIndependiente(CasaUrbana):

    _VALOR_AREA = 3000000.0  

    def __init__(self, identificador_inmobiliario: int, area: int, direccion: str,
                 numero_habitaciones: int, numero_banos: int, numero_pisos: int):
        super().__init__(identificador_inmobiliario, area, direccion,
                         numero_habitaciones, numero_banos, numero_pisos)
    def imprimir(self):
        super().imprimir()
        print()

class Prueba:

    @staticmethod
    def main():
        apto1 = ApartamentoFamiliar(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
        print("Datos apartamento")
        apto1.calcular_precio_venta(ApartamentoFamiliar._VALOR_AREA)
        apto1.imprimir()
        print("Datos apartamento")
        aptestudio1 = Apartaestudio(12354, 50, "Avenida Caracas 30-15")
        aptestudio1.calcular_precio_venta(Apartaestudio._VALOR_AREA)
        aptestudio1.imprimir()

if __name__ == "__main__":
    Prueba.main()
