import datetime
from ComponentePipeline import ComponentePipeline
from Context import Context
from ContextoGenerico import ContextoGenerico


class FiltroEstado(ComponentePipeline):
    estado: str

    def __init__(self, estado: str):
        self.estado = estado

    def filtrar_encuestas_por_estado(self, lista_data):
        resultado = []
        for fila in lista_data:
            if fila.estado_encuesta.lower() == self.estado.lower():
                resultado.append(fila)
        return resultado

    def ejecutar(self, context: ContextoGenerico):
        print(
            f"[{datetime.datetime.now()}] ⌛ Ejecutando filtro por estado '{self.estado}'")
        new_lista_data = self.filtrar_encuestas_por_estado(context.get_data())
        new_context = Context()
        new_context.set_data(new_lista_data)
        print(
            f"[{datetime.datetime.now()}] ✅ Fin filtro por estado '{self.estado}'")
        return new_context
