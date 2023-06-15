# Juan Andres Cherviere version 2
import datetime

class Transformador:
    def __init__(self, data):
        self.data = data

    def formatear(self, columna):
        valor = getattr(self.data, f"get_{columna}")()
        if valor is not None:
            return valor
        return None

    def mayusculas(self, columna):
        valor = self.formatear(columna)
        if valor is not None:
            return valor.upper()
        return None

    def minusculas(self, columna):
        valor = self.formatear(columna)
        if valor is not None:
            return valor.lower()
        return None

    def quitar_espacios(self, columna):
        valor = self.formatear(columna)
        if valor is not None:
            return valor.strip()
        return None

    def invertir(self, columna):
        valor = self.formatear(columna)
        if valor is not None:
            return valor[::-1]
        return None

    def formatear_fecha(self, columna, formato):
        valor = self.formatear(columna)
        if valor is not None and isinstance(valor, datetime.datetime):
            return valor.strftime(formato)
        return None

'''
Ejemplo:

data = Data(1, datetime.datetime.now(), "Completa", "Paraje 1", 10)
transformador = Transformador(data)

# Aplicar transformación de fecha y obtener el valor transformado en formato DD/MM/AAAA
fecha_transformada = transformador.formatear_fecha("fecha_inicial", "%d/%m/%Y")

# Imprimir la fecha transformada
print(fecha_transformada)

'''