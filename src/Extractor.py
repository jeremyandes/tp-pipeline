import csv
import datetime
from ComponentePipeline import ComponentePipeline
from Context import Context
from ContextoGenerico import ContextoGenerico
from Data import Data


class Extractor(ComponentePipeline):
    initial_dataset: str
    data: list
    current_position: int

    def __init__(self, initial_dataset: str):
        self.initial_dataset = initial_dataset
        self.data = []

    def ejecutar(self, context: ContextoGenerico) -> ContextoGenerico:
        print(f"[{datetime.datetime.now()}] ⌛ Ejecutando extractor")
        with open(self.initial_dataset, "r") as archivo_csv:
            fila = csv.reader(archivo_csv)
            next(fila)
            for columna in fila:
                id_encuesta = columna[0]
                fecha_inicial = columna[1]
                estado_encuesta = columna[2]
                paraje = columna[3]
                cantidad_personas = columna[4]
                objeto_data = Data(id_encuesta, fecha_inicial,
                                   estado_encuesta, paraje, cantidad_personas)

                current_position = fila.line_num

                # Cortar operacion si hay datos erróneos
                if (objeto_data.id == ""):
                    print(
                        f"[{datetime.datetime.now()}] ⛔ Error en extractor: Se encontró un objeto erróneo, en la fila {current_position}.")
                    return Context()

                self.data.append(objeto_data)

        context.set_data(self.data)
        print(f"[{datetime.datetime.now()}] 🗨️  Cantidad de datos extraidos del archivo CSV inicial: {len(self.data)}")
        print(f"[{datetime.datetime.now()}] ✅ Fin ejecucion extractor")
        return context


# # Prueba
# extractor = Extractor(
#     "C:\\Users\\ariel\\OneDrive\\Escritorio\\CAECE\\tp-pipeline\\csv\\initial_dataset.csv")
# lista_data = extractor.ejecutar()
# for objeto in lista_data:
#     print(objeto.id, objeto.fecha_inicial, objeto.estado_encuesta,
#           objeto.paraje, objeto.cantidad_personas)
