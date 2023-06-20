from ComponentePipeline import ComponentePipeline
from Context import Context
from ContextoGenerico import ContextoGenerico


class FiltroEstado(ComponentePipeline):

    def __init__(self, estado: str):
        self.estado = estado

    def filtrar_encuestas_completas(self, lista_data):
        resultado = []
        for fila in lista_data:
            if fila.estado_encuesta == self.estado:
                resultado.append(fila)
        return resultado

    def ejecutar(self, context: ContextoGenerico):
        print("Ejecutando filtro estado")
        new_lista_data = self.filtrar_encuestas_completas(context.get_data())
        new_context = Context()
        new_context.set_data(new_lista_data)
        print("Fin ejecucion filtro estado")
        return new_context
