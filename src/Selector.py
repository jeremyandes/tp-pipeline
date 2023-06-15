from Data import Data
from typing import List

class Selector:

    def __init__(self, lista_data):
        self.lista_data = lista_data

    def campos_vacios (self):
        for fila in self.lista_data:
            if '' in (fila.id, fila.fecha_inicial, fila.estado_encuesta, fila.paraje, fila.cantidad_personas):
                return True
        return False
        


# lista_data = [Data(10, "2021-08-19", "", "breayoj", 6),Data(4,"2021-08-19", "Completa", "breayoj", 6)]
# selector = Selector(lista_data)
# if selector.campos_vacios():
#     print("La fila tiene Objeto Data con campos vacios")
#else:
#     print("La fila NO tiene Objeto Data con campos vacios")

