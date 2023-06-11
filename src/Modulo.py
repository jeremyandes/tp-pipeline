from abc import abstractmethod
import ComponentePipeline


class Modulo(ComponentePipeline):
    @abstractmethod
    def ejecutar(self, context):
        pass
