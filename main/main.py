from controller.bibliotecaController import prestarLibro, devolverLibro 
from service.bibliotecaService import libroDigital, libroImpreso

def main():
    libro_impreso = libroImpreso("El tesoro escondido")
    libro_digital = libroDigital("1993")

    print(prestarLibro(libro_impreso))
    print(devolverLibro(libro_impreso))
    print(prestarLibro(libro_digital))
    print(devolverLibro(libro_digital))

if __name__=="__main__":
    main()
    



