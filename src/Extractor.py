import csv

<<<<<<< HEAD
# import Modulo
# Cambie el nombre del archivo por initial_dataset

class Extractor:
    def __init__(self,initial_dataset):
        self.initial_dataset = initial_dataset
        self.data= []
     
    def ejecutar(self):
        with open (self.initial_dataset, "r") as file:
            csv_reader = csv.reader(file)
            self.data = list(csv_reader)
    
    def get_data (self):
        return self.data

# Prueba
#extractor = Extractor("C:/initial_dataset.csv")
#extractor.ejecutar()
#data =  extractor.get_data()
#for row in data:
#	print(row)
=======

class Extractor(Modulo):
    def __init__(self, url_origen):
        self.url_origen = url_origen

    @staticmethod
    def create_instance(url_origen):
        return Extractor(url_origen)

    def execute(self, context):
        # TODO Implementar este metodo
        print("Extractor executed")
>>>>>>> bebb15aeefaf09f74b3ff91851a7e6122bda8fcd
