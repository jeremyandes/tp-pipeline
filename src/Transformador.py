import Modulo


class Transformador(Modulo):

    @staticmethod
    def create_instance():
        return Transformador()

    def ejecutar(self, context):
        # TODO Implementar este metodo
        print("Transformador executed")
