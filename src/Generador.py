from Context import Context
import pandas as pd


class Generador():
    context: Context
    url_destino: str

    def __init__(self, context: Context, url_destino: str):
        self.context = context
        self.url_destino = url_destino

    @staticmethod
    def create_instance(url_destino):
        return Generador(url_destino)

    def ejecutar(self):
        df = pd.DataFrame(
            self.context.get_data_as_dataframe(),
            columns=self.context.get_columns_for_dataframe()
        )
        df.to_csv(self.url_destino, index=False)
