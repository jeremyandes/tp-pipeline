from Context import Context
from Data import Data
from Extractor import Extractor
from FiltroEstado import FiltroEstado
from FormateadorFecha import FormateadorFecha
from Generador import Generador
from Pipeline import Pipeline
from Selector import Selector
from Validador import Validador

####### URL a la carpeta CSV ######
csvPath = '../csv/'

# Creando un componente extractor
extractor = Extractor(
    csvPath + "initial_dataset.csv")

# Creando un componente generador campo vacio
generadorCamposVacios = Generador(
    csvPath + "campos_vacios.csv")

# creando un componente generador para campos completos
generadorCompletas = Generador(
    csvPath + "encuestas_completas.csv")

# Creando un componente validador
validador = Validador(Data.get_columns_for_dataframe())

# Creando un componente formateador fecha
formateador_fecha = FormateadorFecha("fecha_inicial")

# Creando un componente formateador mayusculas paraje
formateador_mayusculas = FormateadorFecha("paraje")

# Creando un componente selector
selector = Selector()

# Creando un componente filtro estado por completas
filtro_estado_completas = FiltroEstado("Completa")

# Creando un componente pipeline
pipeline = Pipeline()

# Agregando el extractor y el generador al pipeline
pipeline.add_component(extractor)
pipeline.add_component(validador)
pipeline.add_component(formateador_fecha)
pipeline.add_component(formateador_mayusculas)
# Selector devuelve una tupla, el siguiente componente en el pipeline deberia tener una tupla de componentes a ejecutar
pipeline.add_component(selector)
pipeline.add_component((filtro_estado_completas, generadorCamposVacios))
pipeline.add_component(generadorCompletas)

# Correr programa principal
# Creando contexto inicial
context = Context()

# Ejecutar pipeline con contexto inicial
pipeline.ejecutar(context)
