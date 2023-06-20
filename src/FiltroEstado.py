from Context import Context
from ContextEncuentasPorParaje import ContextEncuestasPorParaje
from ContextoGenerico import ContextoGenerico
from Data import Data
from typing import List


class FiltroEstado:

    def __init__(self, estado: str):
        self.estado = estado

    def filtrar_encuestas_completas(self, lista_data):
        resultado = []
        for fila in lista_data:
            print(fila.estado_encuesta)
            if fila.estado_encuesta == self.estado:
                resultado.append(fila)
        return resultado

    def ejecutar(self, context: ContextoGenerico):
        print("Ejecutando filtro estado")
        new_lista_data = self.filtrar_encuestas_completas(context.get_data())
        new_context = Context()
        new_context.set_data(new_lista_data)
        print(new_lista_data)
        print("Fin ejecucion filtro estado")
        return new_context
