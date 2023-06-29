from ContextoGenerico import ContextoGenerico
from DataEncuentasPorParaje import DataEncuentasPorParaje

# Este contexto puede ser devuelto por el agregador


class ContextEncuestasPorParaje(ContextoGenerico):
    data: list[DataEncuentasPorParaje] = []

    def __init__(self):
        # El constructor no es necesario, llamamos a sus métodos luego de inicializarse.
        pass

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_data_by_id(self, id: DataEncuentasPorParaje) -> DataEncuentasPorParaje | None:
        for data in self.data:
            if data.get_id() == id:
                return data
        return None

    def add_data(self, data: DataEncuentasPorParaje):
        self.data.append(data)

    def remove_data_by_id(self, id) -> bool:
        for data in self.data:
            if data.get_id() == id:
                self.data.remove(data)
                return True
        return False
