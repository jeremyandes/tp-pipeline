from Context import Context
from ContextoGenerico import ContextoGenerico
from Data import Data
from typing import List


class Selector:
    def filtrar_campos_vacios(self, lista_data):
        resultado = []
        for fila in lista_data:
            if '' in (fila.id, fila.fecha_inicial, fila.estado_encuesta, fila.paraje, fila.cantidad_personas):
                resultado.append(fila)
        return resultado

    def filtrar_encuestas_completas(self, lista_data):
        resultado = []
        for fila in lista_data:
            if fila.estado_encuesta == "Completa" and '' not in (fila.id, fila.fecha_inicial, fila.estado_encuesta, fila.paraje, fila.cantidad_personas):
                resultado.append(fila)
        return resultado

    def ejecutar(self, context: ContextoGenerico):

        encuestas_completas = self.filtrar_encuestas_completas(
            context.get_data())
        contexto_encuestas_completas = Context()
        contexto_encuestas_completas.set_data(encuestas_completas)

        campos_vacios = self.filtrar_campos_vacios(context.get_data())
        contexto_campos_vacios = Context()
        contexto_campos_vacios.set_data(campos_vacios)

        return (contexto_encuestas_completas, contexto_campos_vacios)
