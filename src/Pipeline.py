from ComponentePipeline import ComponentePipeline
from ContextoGenerico import ContextoGenerico


class Pipeline(ComponentePipeline):
    components = []

    def __init__(self):
        self.components = []

    def add_component(self, component: ComponentePipeline):
        self.components.append(component)

    def ejecutar(self, context: ContextoGenerico) -> ContextoGenerico:
        print("Ejecutando pipeline")
        new_context = context
        for componente in self.components:
            new_context = componente.ejecutar(new_context)

        print("Fin pipeline")

        return new_context
