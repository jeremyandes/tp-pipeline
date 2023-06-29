# Juan Andres Cherviere version 2
import datetime

from EstadoEncuesta import EstadoEncuesta
from ComponentePipeline import ComponentePipeline
from ContextoGenerico import ContextoGenerico


class Validador(ComponentePipeline):
    columnas_validar: list

    def __init__(self, columnas_validar):
        self.columnas_validar = columnas_validar

    def validar(self, data):
        for columna in self.columnas_validar:

            if not hasattr(data, columna):
                raise ValueError(
                    f"La columna {columna} no existe. | Data ID: {data.id}")

            valor = getattr(data, columna)
            if not self.validar_tipo(columna, valor):
                raise ValueError(
                    f"El valor ({valor}) de la columna {columna} no cumple con el tipo de dato esperado. | Data ID: {data.id}")

    def validar_tipo(self, columna, valor):
        # Si el tipo es válido, retorna True. De lo contrario, retorna False.
        if columna == "id" or columna == "cantidad_personas":
            return isinstance(valor, str) and valor.isdigit()
        elif columna == "fecha_inicial":
            return self.validar_fecha(valor)
        elif columna == "estado_encuesta":
            return valor in [estado.value for estado in EstadoEncuesta]
        else:
            # Si la columna no está definida en las condiciones anteriores, se considera válida
            return True

    def validar_fecha(self, fecha):
        try:
            datetime.datetime.fromisoformat(fecha)
            return True
        except ValueError:
            return False

    def ejecutar(self, context: ContextoGenerico):
        print(f"[{datetime.datetime.now()}] ⌛ Ejecutando validador")
        lista_data = context.get_data()
        
        for data in lista_data:
            self.validar(data)

        print(f"[{datetime.datetime.now()}] 🗨️  Todos los datos son válidos.")
        print(f"[{datetime.datetime.now()}] ✅ Fin ejecucion validador")
        return context

    @staticmethod
    def tryParseInt(value):
        try:
            return int(value), True
        except ValueError:
            return value, False
