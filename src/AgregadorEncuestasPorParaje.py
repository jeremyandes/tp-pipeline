from ast import List
import datetime
from ComponentePipeline import ComponentePipeline
from ContextEncuentasPorParaje import ContextEncuestasPorParaje
from ContextoGenerico import ContextoGenerico
from Data import Data
from DataEncuentasPorParaje import DataEncuentasPorParaje


class AgregadorEncuestasPorParaje(ComponentePipeline):
    def agruparEncuestasPorParaje(self, lista_data: List(Data)) -> List(DataEncuentasPorParaje):
        resultado = []
        # TODO: Agrupar
        resultado.append(DataEncuentasPorParaje("paraje1", 4))
        resultado.append(DataEncuentasPorParaje("paraje2", 10))
        return resultado

    def ejecutar(self, context: ContextoGenerico):
        print(
            f"[{datetime.datetime.now()}] ⌛ Ejecutando agregador encuestas por paraje")
        new_lista_data = self.agruparEncuestasPorParaje(context.get_data())
        new_context = ContextEncuestasPorParaje()
        new_context.set_data(new_lista_data)
        print(
            f"[{datetime.datetime.now()}] ✅ Fin ejecucion agregador encuestas por paraje")

        return new_context
