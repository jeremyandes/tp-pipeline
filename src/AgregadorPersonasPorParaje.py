from ast import List
import datetime
from ComponentePipeline import ComponentePipeline
from ContextPersonasPorParaje import ContextPersonasPorParaje
from ContextoGenerico import ContextoGenerico
from Data import Data
from DataPersonasPorParaje import DataPersonasPorParaje


class AgregadorPersonasPorParaje(ComponentePipeline):
    def agruparPersonasPorParaje(self, lista_data: List(Data)) -> List(DataPersonasPorParaje):
        resultado = []
        # TODO: Agrupar
        resultado.append(DataPersonasPorParaje("paraje1", 1000))
        resultado.append(DataPersonasPorParaje("paraje2", 400))
        return resultado

    def ejecutar(self, context: ContextoGenerico):
        print(
            f"[{datetime.datetime.now()}] ⌛ Ejecutando agregador personas por paraje")
        new_lista_data = self.agruparPersonasPorParaje(context.get_data())
        new_context = ContextPersonasPorParaje()
        new_context.set_data(new_lista_data)
        print(
            f"[{datetime.datetime.now()}] ✅ Fin ejecucion agregador personas por paraje")
        return new_context
