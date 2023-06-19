import csv
from ComponentePipeline import ComponentePipeline
from Context import Context
from ContextoGenerico import ContextoGenerico
from Data import Data


class Extractor(ComponentePipeline):
    def __init__(self, initial_dataset: str):
        self.initial_dataset = initial_dataset
        self.data = []

    def ejecutar(self, context: ContextoGenerico) -> ContextoGenerico:
        print("Ejecutando extractor")
        with open(self.initial_dataset, "r") as archivo_csv:
            fila = csv.reader(archivo_csv)
            next(fila)
            for columna in fila:
                id = columna[0]
                fecha_inicial = columna[1]
                estado_encuesta = columna[2]
                paraje = columna[3]
                cantidad_personas = columna[4]
                objeto_data = Data(id, fecha_inicial,
                                   estado_encuesta, paraje, cantidad_personas)
                self.data.append(objeto_data)

        new_context = Context()
        new_context.set_data(self.data)
        print("Fin ejecucion extractor")
        return new_context


# # Prueba
# extractor = Extractor(
#     "C:\\Users\\ariel\\OneDrive\\Escritorio\\CAECE\\tp-pipeline\\csv\\initial_dataset.csv")
# lista_data = extractor.ejecutar()
# for objeto in lista_data:
#     print(objeto.id, objeto.fecha_inicial, objeto.estado_encuesta,
#           objeto.paraje, objeto.cantidad_personas)
