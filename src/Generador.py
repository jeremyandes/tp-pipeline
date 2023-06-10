import Modulo


class Generador(Modulo):
    def __init__(self, url_destino):
        self.url_destino = url_destino

<<<<<<< HEAD
    def ejecutar(self):
         # TODO Implementar este metodo
        pass
=======
    @staticmethod
    def create_instance(url_destino):
        return Generador(url_destino)

    def execute(self, context):
        # TODO Implementar este metodo
        print("Generador executed")
>>>>>>> bebb15aeefaf09f74b3ff91851a7e6122bda8fcd
