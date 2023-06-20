# Juan Andres Cherviere version 2
import datetime

from ComponentePipeline import ComponentePipeline
from ContextoGenerico import ContextoGenerico


class Validador(ComponentePipeline):
    def __init__(self, columnas_validar):
        self.columnas_validar = columnas_validar

    def validar(self, data):
        for columna in self.columnas_validar:
            print(columna)

            if not hasattr(data, columna):
                raise ValueError(
                    f"La columna {columna} no existe en el objeto Data.")
            valor = getattr(data, columna)
            print(valor)
            if not self.validar_tipo(columna, valor):
                raise ValueError(
                    f"El valor ({valor}) de la columna {columna} no cumple con el tipo de dato esperado.")

    def validar_tipo(self, columna, valor):
        # Si el tipo es válido, retorna True. De lo contrario, retorna False.
        if columna == "id" or columna == "cantidad_personas":
            valor, es_parseable = self.tryParseInt(valor)
            return es_parseable and valor > 0
        elif columna == "fecha_inicial":
            return self.validar_fecha(valor)
        elif columna == "estado_encuesta":
            return valor in ['', 'Completa', 'Imposibilitada', 'De Prueba', 'En proceso']
        else:
            # Si la columna no está definida en las condiciones anteriores, se considera válida
            return True

    def validar_fecha(self, fecha):
        try:
            datetime.datetime.strptime(fecha, '%d/%m/%Y')
            return True
        except ValueError:
            return False

    def ejecutar(self, context: ContextoGenerico):
        print("Ejecutando validador")
        lista_data = context.get_data()
        # for data in lista_data:
        #     self.validar(data)
        print("Fin ejecucion validador")
        return context

    @staticmethod
    def tryParseInt(value):
        try:
            return int(value), True
        except ValueError:
            return value, False
