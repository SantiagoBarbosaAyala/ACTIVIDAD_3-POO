class Persona:

    def __init__(self, nombre: str, direccion: str):
        self._nombre = nombre 
        self._direccion = direccion # guion bajo para indicar un atributo "protegido"

    def getNombre(self) -> str:
        return self._nombre

    def getDireccion(self) -> str:
        return self._direccion

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def setDireccion(self, direccion: str):
        self._direccion = direccion

    def __str__(self):
        return f"Nombre: {self._nombre}, Dirección: {self._direccion}"

class Estudiante(Persona):

    def __init__(self, nombre: str, direccion: str, carrera: str, semestre: int):
        super().__init__(nombre, direccion) 
        self._carrera = carrera 
        self._semestre = semestre 

    def getCarrera(self) -> str:
        return self._carrera

    def getSemestre(self) -> int:
        return self._semestre

    def setCarrera(self, carrera: str):
        self._carrera = carrera

    def setSemestre(self, semestre: int):
        self._semestre = semestre

    def __str__(self):
        return f"Estudiante: {super().__str__()}, Carrera: {self._carrera}, Semestre: {self._semestre}"

class Profesor(Persona):

    def __init__(self, nombre: str, direccion: str, departamento: str, categoria: str):
        super().__init__(nombre, direccion) 
        self._departamento = departamento 
        self._categoria = categoria 

    def getDepartamento(self) -> str:
        return self._departamento

    def getCategoria(self) -> str:
        return self._categoria

    def setDepartamento(self, departamento: str):
        self._departamento = departamento

    def setCategoria(self, categoria: str):
        self._categoria = categoria

    def __str__(self):
        return f"Profesor: {super().__str__()}, Departamento: {self._departamento}, Categoría: {self._categoria}"


if __name__ == "__main__":
    print("Universidad")

    print("\nPersona")
    persona1 = Persona("Ana García", "Calle 123 #55 sur")
    print(persona1)
    persona1.setDireccion("Avenida Colombia #50 centro")
    print(f"Dirección actualizada de {persona1.getNombre()}: {persona1.getDireccion()}")

    print("\nEstudiantes")
    estudiante1 = Estudiante("Carlos Bernal", "Barrio Kennedy calle 12", "Ingeniería de Sistemas", 3)
    estudiante2 = Estudiante("Laura Torres", "Barrio Laureles calle 54", "Diseño Gráfico", 5)
    print(estudiante1)
    print(estudiante2)

    estudiante1.setSemestre(4)
    print(f"Semestre actualizado para {estudiante1.getNombre()}: {estudiante1.getSemestre()}")
    print(f"Carrera de {estudiante2.getNombre()}: {estudiante2.getCarrera()}")

    print("\nProfesores")
    profesor1 = Profesor("Profesor Juan Martínez", "Poblado calle 10", "Ciencias de la Computación", "Titular")
    profesor2 = Profesor("Profesora Sofía Ruíz", "Rio Negro calle 40c", "Diseño", "Titular")
    print(profesor1)
    print(profesor2)
    profesor1.setCategoria("Temporal")
    print(f"Categoría actualizada para {profesor1.getNombre()}: {profesor1.getCategoria()}")
    print(f"Departamento de {profesor2.getNombre()}: {profesor2.getDepartamento()}")
