from abc import ABC, abstractmethod

from ContextoGenerico import ContextoGenerico


class ComponentePipeline(ABC):
    @abstractmethod
    def ejecutar(self, context: ContextoGenerico) -> ContextoGenerico:
        pass
