from service.bibliotecaService import libroImpreso, libroDigital, libroPrestadoExepcion

def prestarLibro(libro):
    try: 
        return libro.prestado()
    except libroPrestadoExepcion as e:
        return f"Error {str(e)}"
    
def devolverLibro(libro):
        return libro.libroDevolver
    

