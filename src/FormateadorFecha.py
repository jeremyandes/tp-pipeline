
import datetime
from ComponentePipeline import ComponentePipeline
from ContextoGenerico import ContextoGenerico


class FormateadorFecha(ComponentePipeline):
    columna: str
    formato: str

    def __init__(self, columna: str, formato: str = '%d-%m-%Y'):
        self.columna = columna
        self.formato = formato

    def transformar_fecha(self, fecha):
        return datetime.datetime.strptime(fecha, '%Y-%m-%d').strftime(self.formato)

    def ejecutar(self, context: ContextoGenerico):
        print(f"[{datetime.datetime.now()}] ⌛ Ejecutando formateador de fecha")

        lista_data = context.get_data()
        for data in lista_data:
            fecha = getattr(data, self.columna)
            setattr(data, self.columna, self.transformar_fecha(fecha))

        context.set_data(lista_data)

        print(f"[{datetime.datetime.now()}] 🗨️  Fechas transformadas correctamente al formato {self.formato}")
        print(f"[{datetime.datetime.now()}] ✅ Fin ejecucion formateador de fecha")
        return context
