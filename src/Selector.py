from Context import Context
from ContextoGenerico import ContextoGenerico
from Data import Data
from typing import List


class Selector:
    def filtrar_campos_vacios(self, lista_data):
        resultados_campos_vacios = []
        resultados_campos_no_vacios = []
        for fila in lista_data:
            if '' in (fila.id, fila.fecha_inicial, fila.estado_encuesta, fila.paraje, fila.cantidad_personas):
                resultados_campos_vacios.append(fila)
            else:
                resultados_campos_no_vacios.append(fila)

        return (resultados_campos_vacios, resultados_campos_no_vacios)

    # def filtrar_encuestas_completas(self, lista_data):
    #     resultado = []
    #     for fila in lista_data:
    #         if fila.estado_encuesta == "Completa" and '' not in (fila.id, fila.fecha_inicial, fila.estado_encuesta, fila.paraje, fila.cantidad_personas):
    #             resultado.append(fila)
    #     return resultado

    def ejecutar(self, context: ContextoGenerico):
        print("Ejecutando selector")

        campos_vacios, campos_no_vacios = self.filtrar_campos_vacios(
            context.get_data())

        contexto_campos_vacios = Context()
        contexto_campos_vacios.set_data(campos_vacios)

        contexto_campos_no_vacios = Context()
        contexto_campos_no_vacios.set_data(campos_no_vacios)

        print("Fin ejecucion selector")
        return (contexto_campos_no_vacios, contexto_campos_vacios)
