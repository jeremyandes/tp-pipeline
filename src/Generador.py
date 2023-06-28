import datetime
from ComponentePipeline import ComponentePipeline
from Context import Context
import pandas as pd

from ContextoGenerico import ContextoGenerico


class Generador(ComponentePipeline):
    url_destino: str

    def __init__(self, url_destino: str):
        self.url_destino = url_destino

    def ejecutar(self, context: ContextoGenerico) -> ContextoGenerico:
        print(
            f"[{datetime.datetime.now()}] ⌛ Ejecutando generador del archivo '{self.url_destino}'")

        if (context.has_data()):

            df = pd.DataFrame(
                context.get_data_as_dataframe(),
                columns=context.get_columns_for_dataframe()
            )
            df.to_csv(self.url_destino, index=False)

        else:
            print(
                f"[{datetime.datetime.now()}] 🗨️ El contexto no tiene data para generar")

        print(
            f"[{datetime.datetime.now()}] ✅ Fin ejecucion generador de la url '{self.url_destino}'")
        return context
