from abc import ABC, abstractmethod

from Data import Data


class ContextoGenerico(ABC):
    def get_data_as_dataframe(self):
        data_frame = []
        for data in self.data:
            data_frame.append(data.get_as_dataframe())
        return data_frame

    def get_columns_for_dataframe(self):
        return self.data[0].get_columns_for_dataframe()

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def set_data(self, data):
        pass

    @abstractmethod
    def get_data_by_id(self, id: Data) -> Data | None:
        pass

    @abstractmethod
    def add_data(self, data: Data):
        pass

    @abstractmethod
    def remove_data_by_id(self, id) -> bool:
        pass
