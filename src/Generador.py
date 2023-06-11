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
        # TODO Implementar este metodo
        print("Generador executed")

# Prueba de clase Generador


# generador = Generador(Context(), "test.csv")
# generador.ejecutar()
# df = pd.DataFrame(
#     generador.context.get_data_as_dataframe(),
#     columns=["id", "fecha_inicial", "estado_encuesta",
#              "paraje", "cantidad_personas"]
# )
# df.to_csv(generador.url_destino, index=False)
