import Modulo


class Calculador(Modulo):

    @staticmethod
    def create_instance():
        return Calculador()

    def ejecutar(self, context):
        # TODO Implementar este metodo
        print("Calculador executed")
