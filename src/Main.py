from Context import Context
from Extractor import Extractor
from Generador import Generador
from Pipeline import Pipeline
from Selector import Selector

####### URL a la carpeta CSV ######
csvPath = '../csv/'

# Creando un componente extractor
extractor = Extractor(
    csvPath + "initial_dataset.csv")

# Creando un componente generador
generadorCamposVacios = Generador(
    csvPath + "campos_vacios_dataset.csv")

generadorCamposCompletos = Generador(
    csvPath + "campos_completos_dataset.csv")

generadorExtraParaEjemplo = Generador(
    csvPath + "ejemplo_dataset.csv")

# Creando un componente selector
selector = Selector()

# Creando un componente pipeline
pipeline = Pipeline()

# Agregando el extractor y el generador al pipeline
pipeline.add_component(extractor)
pipeline.add_component(selector)
pipeline.add_component((generadorCamposCompletos, generadorCamposVacios))
# Este componente sigue con el context que devuelve el componente generadorCamposCompletos
pipeline.add_component(generadorExtraParaEjemplo)

# Creando contexto inicial
context = Context()

# Ejecutar pipeline con contexto inicial
pipeline.ejecutar(context)
