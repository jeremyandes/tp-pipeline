from abc import abstractmethod
import ComponentPipeline


class Modulo(ComponentPipeline):
    @abstractmethod
    def ejecutar(self, context):
        pass
