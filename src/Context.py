from ContextoGenerico import ContextoGenerico
from Data import Data


class Context(ContextoGenerico):
    data: list[Data] = []

    def get_data(self):
        return self.data

    def set_data(self, data):
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

    def create_example_list(self):
        self.data = [
            Data(0, "2021-08-19", "Completa", "breayoj", 3),
            Data(1, "2021-08-19", "Completa", "breayoj", 5),
            Data(2, "2021-08-19", "Completa", "breayoj", 6),
            Data(3, "2021-08-19", "Completa", "breayoj", 1),
            Data(4, "2021-08-19", "Completa", "breayoj", 6),
            Data(5, "2021-08-19", "Completa", "breayoj", 1),
            Data(6, "2021-08-18", "Completa", "breayoj", 3),
            Data(7, "2021-08-18", "Completa", "breayoj", 8),
            Data(8, "2021-08-18", "Completa", "breayoj", 1),
            Data(9, "2021-08-14", "Completa", "breayoj", 2),
            Data(10, "2021-08-16", "Completa", "taquello", 2),
            Data(11, "2021-08-16", "Completa", "taquello", 4),
            Data(12, "2021-08-17", "Completa", "breayoj", 3),
            Data(13, "2021-08-17", "Completa", "breayoj", 6),
            Data(14, "2021-08-17", "Completa", "breayoj", 4),
            Data(15, "2021-08-17", "Completa", "breayoj", 4),
            Data(16, "2021-08-18", "Completa", "breayoj", 3),
            Data(17, "2021-08-18", "Completa", "breayoj", 8),
            Data(18, "2021-08-16", "Completa", "taquello", 4),
            Data(19, "2021-08-16", "Completa", "taquello", 1),
            Data(20, "2021-08-16", "Completa", "taquello", 6),
            Data(21, "2021-08-16", "Completa", "taquello", 5),
            Data(22, "2021-08-17", "Completa", "breayoj", 3),
            Data(23, "2021-08-17", "Completa", "breayoj", 1),
            Data(24, "2021-08-24", "Completa", "", 5),
            Data(25, "2021-08-23", "", "breayoj", 7),
            Data(26, "2021-08-24", "Completa", "breayoj", 3),
            Data(27, "2021-08-24", "Completa", "breayoj", 2),
            Data(28, "2021-08-24", "", "breayoj", 3),
            Data(29, "2021-08-24", "Completa", "", 8),
            Data(30, "2021-08-23", "Completa", "breayoj", 1),
            Data(31, "2021-08-23", "Completa", "breayoj", 6),
            Data(32, "2021-08-23", "Completa", "breayoj", 9),
            Data(33, "2021-08-23", "Completa", "breayoj", 5),
            Data(34, "2021-08-23", "Completa", "breayoj", 6),
            Data(35, "2021-08-13", "Completa", "colonia real sur", 4)
        ]
