class RutinaGym:
    def __init__(self, nombre, duracion, calorias, ejercicios, nivel):
        self.__nombre = nombre
        self.__duracion = duracion
        self.__calorias = calorias
        self.__ejercicios = ejercicios 
        self.__nivel = nivel 

    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nuevo_nombre):
        self.__nombre = nuevo_nombre


    def get_duracion(self):
        return self.__duracion    
    
    def set_duracion(self,nueva_duracion):
        self.__duracion = nueva_duracion



        



