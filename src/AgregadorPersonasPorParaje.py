from ast import List
import datetime
from ComponentePipeline import ComponentePipeline
from ContextPersonasPorParaje import ContextPersonasPorParaje
from ContextoGenerico import ContextoGenerico
from Data import Data
from DataPersonasPorParaje import DataPersonasPorParaje
import pandas as pd

class AgregadorPersonasPorParaje(ComponentePipeline):

    def reading_list(self, df:pd.DataFrame) -> list:
        return list(map(lambda key, value: DataPersonasPorParaje(key, value), df.keys(), df.values.tolist()))

    def agruparPersonasPorParaje(self, df: pd.DataFrame) -> List(DataPersonasPorParaje):
        resultado = []
        df['cantidad_personas'] = df['cantidad_personas'].astype(int)
        count = df.groupby('paraje')['cantidad_personas'].sum()
        resultado = self.reading_list(count)
        return resultado

    def ejecutar(self, context: ContextoGenerico):
        print(
            f"[{datetime.datetime.now()}] ⌛ Ejecutando agregador personas por paraje")
        
        if (context.has_data()):
            df = pd.DataFrame(
                context.get_data_as_dataframe(),
                columns=context.get_columns_for_dataframe()
            )
            new_lista_data = self.agruparPersonasPorParaje(df)
            new_context = ContextPersonasPorParaje()
            new_context.set_data(new_lista_data)
        
        else:
            print(
                f"[{datetime.datetime.now()}] 🗨️ El contexto no tiene datos para agrupar")

            new_context = ContextPersonasPorParaje()

        print(
            f"[{datetime.datetime.now()}] ✅ Fin ejecucion agregador personas por paraje")
        
        return new_context