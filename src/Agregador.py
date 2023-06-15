#Agregador version 1
from typing import List
from Context import Context
from Data import Data

class Agregador:
    def __init__(self, lista_data):
        self.lista_data = lista_data

    def cantidad_encuestas_por_paraje(self):
        encuestas_por_paraje = {} # diccionario, para guardar el recuento

        for fila in self.lista_data:
            paraje = fila.paraje
            if paraje in encuestas_por_paraje:
                encuestas_por_paraje[paraje] = encuestas_por_paraje[paraje] + 1
            else:
                encuestas_por_paraje[paraje] = 1

        return encuestas_por_paraje

    def cantidad_personas_por_paraje(self):
        personas_por_paraje = {}

        for fila in self.lista_data:
            paraje = fila.paraje
            cantidad_personas = fila.cantidad_personas
            if paraje in personas_por_paraje:
                personas_por_paraje[paraje] = personas_por_paraje[paraje] + cantidad_personas
            else:
                personas_por_paraje[paraje] = cantidad_personas

        return personas_por_paraje

