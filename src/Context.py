from typing import List
from Data import Data

# Otro comentario agregado
class Context:
    data: List(Data)

    def __init__(self):
        self.data = []

    def get_data(self) -> List(Data):
        return self.data

    def set_data(self, data: List(Data)):
        self.data = data

    def get_data_by_id(self, id: Data) -> Data | None:
        for data in self.data:
            if data.get_id() == id:
                return data
        return None

    def add_data(self, data: Data):
        self.data.append(data)

    def remove_data_by_id(self, id) -> bool:
        for data in self.data:
            if data.get_id() == id:
                self.data.remove(data)
                return True
        return False
