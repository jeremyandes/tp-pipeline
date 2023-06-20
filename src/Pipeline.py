from ComponentePipeline import ComponentePipeline
from ContextoGenerico import ContextoGenerico


class Pipeline(ComponentePipeline):
    components = []

    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def ejecutar(self, context: ContextoGenerico):
        # TODO: Tirar excepcion si:
        # Es una tupla de 3 o mas
        # Es tupla vacia
        # Otros?
        print("Ejecutando pipeline")
        contexto_principal = context
        contexto_alternativo = None
        for componente in self.components:
            if not isinstance(componente, tuple):
                result = componente.ejecutar(contexto_principal)
            else:
                componente_principal, componente_alternativo = componente
                result = componente_principal.ejecutar(contexto_principal)
                _ = componente_alternativo.ejecutar(contexto_alternativo)

            if (result is not None):
                if not isinstance(result, tuple):
                    contexto_principal = result
                else:
                    contexto_principal, contexto_alternativo = result

        print("Fin pipeline")

        return None
