
import datetime
from ComponentePipeline import ComponentePipeline
from ContextoGenerico import ContextoGenerico


class FormateadorFecha(ComponentePipeline):
    def __init__(self, columna: str):
        self.columna = columna

    def formatear(self, data):
        valor = getattr(data, f"get_{self.columna}")()
        if valor is not None:
            return valor
        return None

    def formatear_fecha(self, data):
        valor = self.formatear(data)
        if valor is not None and isinstance(valor, datetime.datetime):
            return valor.strftime("DD/MM/AAAA")
        return None

    def ejecutar(self, context: ContextoGenerico):
        # TODO: Verificar funcionamiento
        print("Ejecutando transformador")
        lista_data = context.get_data()
        for data in lista_data:
            # TODO: Transformar!
            pass

        # TODO: asignar la data transformada al nuevo context y devolver el nuevo context
        # new_context = Context()
        # new_context.set_data(new_data)

        print("Fin ejecucion transformador")
        return context
