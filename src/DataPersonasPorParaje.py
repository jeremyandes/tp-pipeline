class DataPersonasPorParaje:
    paraje: str
    cantidad_personas: int

    def __init__(self, paraje: str, cantidad_personas: int):
        self.paraje = paraje
        self.cantidad_personas = cantidad_personas

    def get_as_dataframe(self):
        return [self.paraje, self.cantidad_personas]

    def get_columns_for_dataframe(self):
        return ["paraje", "cantidad_personas"]
