import csv

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
