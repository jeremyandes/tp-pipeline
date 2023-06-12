#Agregador version 1
from typing import List
from Context import Context
from Data import Data

class Agregador:
    #utilizo como parametro la columna por la cual quiero ralizar la agregacion por ejemplo paraje
    def __init__(self, columnas_agregacion: List[str]):
        self.columnas_agregacion = columnas_agregacion

    def contar_encuestas_por_paraje(self, context: Context) -> Context:
        resultados = {}
        for data in context.get_data():
            paraje = data.get_paraje()
            if paraje in resultados:
                resultados[paraje] += 1
            else:
                resultados[paraje] = 1

        nuevo_contexto = Context()
        for paraje, cantidad_encuestas in resultados.items():
            nueva_data = Data(paraje=paraje, cantidad_encuestas=cantidad_encuestas)
            nuevo_contexto.add_data(nueva_data)

        return nuevo_contexto

    def sumar_personas_por_paraje(self, context: Context) -> Context:
        resultados = {}
        for data in context.get_data():
            paraje = data.get_paraje()
            cantidad_personas = data.get_cantidad_personas()
            if paraje in resultados:
                resultados[paraje] += cantidad_personas
            else:
                resultados[paraje] = cantidad_personas

        nuevo_contexto = Context()
        for paraje, cantidad_personas in resultados.items():
            nueva_data = Data(paraje=paraje, cantidad_personas=cantidad_personas)
            nuevo_contexto.add_data(nueva_data)

        return nuevo_contexto
