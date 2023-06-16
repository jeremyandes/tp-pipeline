# Juan Andres Cherviere version 3
from Context import Context
from Data import Data
import pandas as pd

class Agregador:
    context: Context

    def __init__(self, context: Context):
        self.context = context

    def contar(self) -> Context:
        parajes = {}
        for data in self.context.get_data():
            paraje = data.get_paraje()
            if paraje in parajes:
                parajes[paraje] += 1
            else:
                parajes[paraje] = 1

        resumen = []
        for paraje, cantidad_encuestas in parajes.items():
            resumen.append([paraje, cantidad_encuestas])

        resumen_context = Context()
        for row in resumen:
            data = Data(0, None, None, row[0], row[1])
            resumen_context.add_data(data)

        return resumen_context

    def sumar(self) -> Context:
        parajes = {}
        for data in self.context.get_data():
            paraje = data.get_paraje()
            cantidad_personas = data.get_cantidad_personas()
            if paraje in parajes:
                parajes[paraje] += cantidad_personas
            else:
                parajes[paraje] = cantidad_personas

        resumen = []
        for paraje, cantidad_personas in parajes.items():
            resumen.append([paraje, cantidad_personas])

        resumen_context = Context()
        for row in resumen:
            data = Data(0, None, None, row[0], row[1])
            resumen_context.add_data(data)

        return resumen_context


'''Ejemplo:

from Context import Context
from Data import Data
from Agregador import Agregador

# Crear un contexto con datos de ejemplo
context = Context()
context.create_example_list()

# Crear una instancia de Agregador
agregador = Agregador(context)

# Realizar el conteo de encuestas por paraje
resumen_contar = agregador.contar()
print("Resumen contar:")
for data in resumen_contar.get_data():
    data.print_data()

# Realizar la suma de cantidad de personas por paraje
resumen_sumar = agregador.sumar()
print("Resumen sumar:")
for data in resumen_sumar.get_data():
    data.print_data()
'''