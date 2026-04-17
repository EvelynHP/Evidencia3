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


    def get_calorias(self):
        return self.__calorias

    def set_calorias(self,nuevas_calorias):
        self.__calorias = nuevas_calorias


    def get_ejercicios(self):
        return self.__ejercicios
    
    def set_ejercicios(self,nuevos_ejercicios):
        self.__ejercicios = nuevos_ejercicios


    def get_nivel(self):
        return self.__nivel
    
    def set_nivel(self,nuevo_nivel):
        self.__nivel = nuevo_nivel



    def agregar_ejercicio(self,ejercicio):
        self.__ejercicios.append(ejercicio) 

    def calcular_calorias(self):
        return self.__duracion * self.__calorias  
    

    def mostar_info(self):
        print(f"Nombre: {self.__nombre} Duracion: {self.__duracion} Calorias: {self.__calorias} Ejercicios: {self.__ejercicios} Nivel: {self.__nivel}")
    

    





        



