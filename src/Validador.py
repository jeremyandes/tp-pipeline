import Modulo


class Validador(Modulo):

    @staticmethod
    def create_instance():
        return Validador()

    def ejecutar(self, context):
        # TODO Implementar este metodo
        print("Validador executed")
