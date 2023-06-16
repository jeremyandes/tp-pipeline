from Extractor import Extractor
import pandas as pd

from Generador import Generador

print(pd.__version__)

extractor = Extractor(
    "C:\\Users\\ariel\\OneDrive\\Escritorio\\CAECE\\tp-pipeline\\csv\\initial_dataset.csv")
context = extractor.ejecutar()

generador = Generador(context,
                      "C:\\Users\\ariel\\OneDrive\\Escritorio\\CAECE\\tp-pipeline\\csv\\final_dataset.csv")

generador.ejecutar()
