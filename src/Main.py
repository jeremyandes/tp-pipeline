from AgregadorEncuestasPorParaje import AgregadorEncuestasPorParaje
from AgregadorPersonasPorParaje import AgregadorPersonasPorParaje
from Context import Context
from Data import Data
from Extractor import Extractor
from FiltroEstado import FiltroEstado
from FormateadorFecha import FormateadorFecha
from FormateadorMayusculas import FormateadorMayusculas
from Generador import Generador
from Pipeline import Pipeline
from Selector import Selector
from Validador import Validador

# Creando contexto inicial
context = Context()

# Creando un componente extractor
extractor = Extractor("initial_dataset.csv")

# Creando un componente generador campo vacio
generadorCamposVacios = Generador("campos_vacios.csv")

# Creando un componente validador
validador = Validador(Data.get_columns_for_dataframe())

# Creando un componente formateador fecha
formateador_fecha = FormateadorFecha("fecha_inicial", '%d/%m/%Y')

# Creando un componente formateador mayusculas paraje
formateador_mayusculas = FormateadorMayusculas("paraje")

# Creando un componente selector
selector = Selector()

# Creando un componente filtro estado por completas
filtro_estado_completas = FiltroEstado("Completa")

# Creando un pipeline para agregador encuestas por paraje
agregador_encuestas_por_paraje = AgregadorEncuestasPorParaje()
generadorEncuestasPorParaje = Generador("encuestas_por_paraje.csv")

# Creando un pipeline para agregador encuestas por paraje
pipeline_encuestas_por_paraje = Pipeline("Pipeline encuestas por paraje")
pipeline_encuestas_por_paraje.add_component(agregador_encuestas_por_paraje)
pipeline_encuestas_por_paraje.add_component(generadorEncuestasPorParaje)

# Creando un pipeline para agregador personas por paraje
agregador_personas_por_paraje = AgregadorPersonasPorParaje()
generadorPersonasPorParaje = Generador("personas_por_paraje.csv")
pipeline_personas_por_paraje = Pipeline("Pipeline personas por paraje")
pipeline_personas_por_paraje.add_component(agregador_personas_por_paraje)
pipeline_personas_por_paraje.add_component(generadorPersonasPorParaje)

# Creando el pipeline PRINCIPAL
pipeline = Pipeline("Pipeline Principal")


##################  Agregando componentes al pipeline ##################
pipeline.add_component(extractor)
pipeline.add_component(validador)
pipeline.add_component(formateador_fecha)
pipeline.add_component(formateador_mayusculas)

# Selector devuelve una tupla, el siguiente componente en el pipeline deberia tener una tupla de componentes a ejecutar
pipeline.add_component(selector)
pipeline.add_component((filtro_estado_completas, generadorCamposVacios))

# Los siguientes pipelines deberian tomar el contexto que devuelve filtro_estado_completas
pipeline.add_component(pipeline_encuestas_por_paraje)
pipeline.add_component(pipeline_personas_por_paraje)

# Generador final del pipeline principal
generador_final = Generador("final_dataset.csv")
pipeline.add_component(generador_final)

# Correr programa principal
# Ejecutar pipeline con contexto inicial
pipeline.ejecutar(context)
