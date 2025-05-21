class Cuenta:
    def __init__(self, saldo, tasaAnual):
        self._saldo = saldo
        self._numeroConsignaciones = 0
        self._numeroRetiros = 0
        self._tasaAnual = tasaAnual
        self._comisionMensual = 0

    def consignar(self, cantidad):
        self._saldo += cantidad
        self._numeroConsignaciones += 1

    def retirar(self, cantidad):
        nuevoSaldo = self._saldo - cantidad
        if nuevoSaldo >= 0:
            self._saldo -= cantidad
            self._numeroRetiros += 1
        else:
            print("La cantidad a retirar excede el saldo actual.")

    def calcularInteres(self):
        tasaMensual = self._tasaAnual / 12
        interesMensual = self._saldo * tasaMensual
        self._saldo += interesMensual

    def extractoMensual(self):
        self._saldo -= self._comisionMensual
        self.calcularInteres()

class CuentaAhorros(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        self._active = saldo >= 10000

    def retirar(self, cantidad):
        if self._active:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        if self._active:
            super().consignar(cantidad)

    def extractoMensual(self):
        if self._numeroRetiros > 4:
            self._comisionMensual += (self._numeroRetiros - 4) * 1000
        super().extractoMensual()
        if self._saldo < 10000:
            self._active = False

    def imprimir(self):
        print(f"Saldo = $ {self._saldo}")
        print(f"Comisión mensual = $ {self._comisionMensual}")
        print(f"Número de transacciones = {self._numeroConsignaciones + self._numeroRetiros}")
        print()

class CuentaCorriente(Cuenta):
    def __init__(self, saldo, tasa):
        super().__init__(saldo, tasa)
        self._sobregiro = 0

    def retirar(self, cantidad):
        resultado = self._saldo - cantidad
        if resultado < 0:
            self._sobregiro -= resultado
            self._saldo = 0
        else:
            super().retirar(cantidad)

    def consignar(self, cantidad):
        residuo = self._sobregiro - cantidad
        if self._sobregiro > 0:
            if residuo > 0:
                self._sobregiro = residuo
                self._saldo = 0
            else:
                self._sobregiro = -residuo
                self._saldo = 0
        else:
            super().consignar(cantidad)

    def extractoMensual(self):
        super().extractoMensual()

    def imprimir(self):
        print(f"Saldo = ${self._saldo}")
        print(f"Cargo mensual = ${self._comisionMensual}")
        print(f"Número de transacciones = {self._numeroConsignaciones + self._numeroRetiros}")
        print(f"Valor de sobregiro = ${self._sobregiro}")
        print()

if __name__ == "__main__":
    print("******Cuenta de ahorros******")

    try:
        saldoInicialAhorros = float(input("Ingrese saldo inicial: $"))
        tasaAhorros = float(input("Ingrese tasa de interes: "))

        cuenta1 = CuentaAhorros(saldoInicialAhorros, tasaAhorros)
        cantidadDepositar = float(input("Ingresar cantidad a consignar: $"))
        cuenta1.consignar(cantidadDepositar)

        cantidadRetirar = float(input("Ingresar cantidad a retirar: $"))
        cuenta1.retirar(cantidadRetirar)
        cuenta1.extractoMensual()
        cuenta1.imprimir()

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")
