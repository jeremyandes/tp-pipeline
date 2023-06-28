from ast import List
import datetime
from ComponentePipeline import ComponentePipeline
from ContextEncuentasPorParaje import ContextEncuestasPorParaje
from ContextoGenerico import ContextoGenerico
from DataEncuentasPorParaje import DataEncuentasPorParaje
import pandas as pd


class AgregadorEncuestasPorParaje(ComponentePipeline):

    def reading_list(self, df:pd.DataFrame) -> list:
        return list(map(lambda key, value:DataEncuentasPorParaje(key, value), df.keys(), df.values.tolist()))

    def agruparEncuestasPorParaje(self, df: pd.DataFrame) -> List(DataEncuentasPorParaje):
        resultado = []
        count = df.groupby('paraje')['id'].count()
        resultado = self.reading_list(count)
        return resultado

    def ejecutar(self, context: ContextoGenerico):
        print(
            f"[{datetime.datetime.now()}] ⌛ Ejecutando agregador encuestas por paraje")

        if (context.has_data()):
            df = pd.DataFrame(
                context.get_data_as_dataframe(),
                columns=context.get_columns_for_dataframe()
            )
            new_lista_data = self.agruparEncuestasPorParaje(df)
            new_context = ContextEncuestasPorParaje()
            new_context.set_data(new_lista_data)

        else:
            print(
                f"[{datetime.datetime.now()}] 🗨️ El contexto no tiene datos para agrupar")

            new_context = ContextEncuestasPorParaje()

        print(
            f"[{datetime.datetime.now()}] ✅ Fin ejecucion agregador encuestas por paraje")

        return new_context
