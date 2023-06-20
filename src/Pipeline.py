from ComponentePipeline import ComponentePipeline
from ContextoGenerico import ContextoGenerico


class Pipeline(ComponentePipeline):
    components = []

    def __init__(self, nombre):
        self.components = []
        self.nombre = nombre

    def add_component(self, component):
        self.components.append(component)

    def ejecutar(self, context: ContextoGenerico):
        print(f"Ejecutando pipeline {self.nombre}")
        contexto_principal = context
        contexto_alternativo = None
        for componente in self.components:
            if not isinstance(componente, tuple):
                result = componente.ejecutar(contexto_principal)
            else:
                componente_principal, componente_alternativo = componente
                _ = componente_alternativo.ejecutar(contexto_alternativo)
                result = componente_principal.ejecutar(contexto_principal)

            if (result is not None):
                if not isinstance(result, tuple):
                    contexto_principal = result
                else:
                    contexto_principal, contexto_alternativo = result

        print(f"Fin pipeline {self.nombre}")

        return None
