from ContextoGenerico import ContextoGenerico
from DataPersonasPorParaje import DataPersonasPorParaje

# Este contexto puede ser devuelto por el agregador


class ContextPersonasPorParaje(ContextoGenerico):
    data: list[DataPersonasPorParaje] = []

    def __init__(self):
        # self.create_example_list()
        pass

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_data_by_id(self, id) -> DataPersonasPorParaje | None:
        for data in self.data:
            if data.get_id() == id:
                return data
        return None

    def add_data(self, data: DataPersonasPorParaje):
        self.data.append(data)

    def remove_data_by_id(self, id) -> bool:
        for data in self.data:
            if data.get_id() == id:
                self.data.remove(data)
                return True
        return False
