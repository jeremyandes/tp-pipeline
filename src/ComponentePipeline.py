from abc import ABC, abstractmethod


class ComponentePipeline(ABC):
    @abstractmethod
    def ejecutar(self, context):
        pass
