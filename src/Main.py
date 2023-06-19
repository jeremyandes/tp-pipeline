from Context import Context
from Extractor import Extractor
from Generador import Generador
from Pipeline import Pipeline

####### URL a la carpeta CSV ######
csvPath = '../csv/'

# Creando un componente extractor
extractor = Extractor(
    csvPath + "initial_dataset.csv")

# Creando un componente generador
generadorCamposVacios = Generador(
    csvPath + "campos_vacios_dataset.csv")

# Creando un componente pipeline
pipeline = Pipeline()

# Agregando el extractor y el generador al pipeline
pipeline.add_component(extractor)
pipeline.add_component(generadorCamposVacios)

# Creando contexto inicial
context = Context()

# Ejecutar pipeline con contexto inicial
pipeline.ejecutar(context)
