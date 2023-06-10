import Modulo


class Generador(Modulo):
    def __init__(self, url_destino):
        self.url_destino = url_destino

    @staticmethod
    def create_instance(url_destino):
        return Generador(url_destino)

    def execute(self, context):
        # TODO Implementar este metodo
        print("Generador executed")
