from ContextEncuentasPorParaje import ContextEncuestasPorParaje
from DataEncuentasPorParaje import DataEncuentasPorParaje
from Extractor import Extractor
import pandas as pd

from Generador import Generador

print(pd.__version__)


# # Ejemplo de la clase generador able to crear archivos con distintas columnas
# extractor = Extractor(
#     "C:\\Users\\ariel\\OneDrive\\Escritorio\\CAECE\\tp-pipeline\\csv\\initial_dataset.csv")
# context = extractor.ejecutar()

# generador1 = Generador(context,
#                        "C:\\Users\\ariel\\OneDrive\\Escritorio\\CAECE\\tp-pipeline\\csv\\final_dataset.csv")

# generador1.ejecutar()

# contextEncuestasPorParaje = ContextEncuestasPorParaje()
# dataEncuestasPorParaje1 = DataEncuentasPorParaje("paraje1", 4)
# dataEncuestasPorParaje2 = DataEncuentasPorParaje("paraje2", 6)
# contextEncuestasPorParaje.add_data(dataEncuestasPorParaje1)
# contextEncuestasPorParaje.add_data(dataEncuestasPorParaje2)

# generador2 = Generador(
#     contextEncuestasPorParaje, "C:\\Users\\ariel\\OneDrive\\Escritorio\\CAECE\\tp-pipeline\\csv\\encuestas_parajes.csv")

# generador2.ejecutar()
