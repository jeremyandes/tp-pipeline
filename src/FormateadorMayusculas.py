
import datetime
from ComponentePipeline import ComponentePipeline
from Context import Context
from ContextoGenerico import ContextoGenerico


class FormateadorMayusculas(ComponentePipeline):
    columna: str

    def __init__(self, columna: str):
        self.columna = columna

    def formatear(self, data):
        valor = getattr(data, f"get_{self.columna}")()
        if valor is not None:
            return valor
        return None

    def mayusculas(self, columna):
        valor = self.formatear(columna)
        if valor is not None:
            return valor.upper()
        return None

    def ejecutar(self, context: ContextoGenerico):
        print(
            f"[{datetime.datetime.now()}] ⌛ Ejecutando formateador de mayúsculas por la columna {self.columna}")

        lista_data = context.get_data()
        for data in lista_data:
            setattr(data, self.columna, self.mayusculas(data))

        context.set_data(lista_data)

        print(
            f"[{datetime.datetime.now()}] ⌛ Fin ejecucion formateador de mayúsculas por la columna {self.columna}")
        return context
