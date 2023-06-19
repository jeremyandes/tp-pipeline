from ComponentePipeline import ComponentePipeline
from Context import Context
import pandas as pd

from ContextoGenerico import ContextoGenerico


class Generador(ComponentePipeline):
    url_destino: str

    def __init__(self, url_destino: str):
        self.url_destino = url_destino

    @staticmethod
    def create_instance(url_destino):
        return Generador(url_destino)

    def ejecutar(self, context: ContextoGenerico) -> ContextoGenerico:
        print("Ejecutando generador")
        df = pd.DataFrame(
            context.get_data_as_dataframe(),
            columns=context.get_columns_for_dataframe()
        )
        df.to_csv(self.url_destino, index=False)
        print("Fin ejecucion generador")
        return context
