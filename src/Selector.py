import Modulo


class Selector(Modulo):

    @staticmethod
    def create_instance():
        return Selector()

    def ejecutar(self, context):
        # TODO Implementar este metodo
        print("Selector executed")
