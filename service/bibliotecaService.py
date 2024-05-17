from abc import ABC, abstractmethod

class biblioteca(ABC):
    def __init__(self,titulo, prestado):
        self.titulo = titulo
        self.prestado = prestado

    @abstractmethod
    def devolucion(self):
        pass 
    
class libroPrestadoExepcion(Exception):
    pass 

class libroImpreso(biblioteca):
    def prestado(self):
        if self.esPrestado:
            raise libroPrestadoExepcion(f"Libro impreso'{self.titulo}' ya esta prestado")
        self.esPrestado = True
        return "Libro impreso '{self.titulo}' prestado"
        
    def devolverLibro(self):
        if not self.esPrestado: 
            return "Libro impreso '{self.titulo}' no estaba prestado"
        self.esPrestado = False
        return "Libro impreso '{self.titulo}' devuelto"
class libroDigital(biblioteca): 
    def prestar(self):
        if self.esPrestado:
            raise libroPrestadoExepcion(f"Libro digital'{self.titulo}' ya esta prestado")
        self.esPrestado = True
        return "Libro digital '{self.titulo}' prestado"
    def devolverLibro(self):
        if not self.esPrestado: 
            return "Libro digital '{self.titulo}' no estaba prestado"
        self.esPrestado = False
        return "Libro digital '{self.titulo}' devuelto"
    







