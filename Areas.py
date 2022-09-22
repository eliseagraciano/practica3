
def Area_cuadrado():
    Ladocuadrado=float(input("ingresa el valor de uno de los lados del cuadrado: "))
    area_cuadrado=Ladocuadrado*Ladocuadrado;
    print("El area del cuadrado es: ",area_cuadrado)

def Area_triangulo():
    base=0
    altura=0
    CONSTANTE_DIVISOR=2
    altura=float(input("ingresa el valor de la altura del triangulo: "))
    base=float(input("ingresa el valor de la base del triangulo: "))
    area_triangulo=(altura+base)/CONSTANTE_DIVISOR;
    print("El area del triangulo es: ",area_triangulo)

def Area_circulo():
    CONSTANTE_PI=3.141592
    radio=float(input("Ingresa el radio del circulo: "))
    area_circulo=(radio*radio)*CONSTANTE_PI;
    print("El area del circulo es: ",area_circulo)

def Menu():
    while True:
        print("Calcular Area\n");
        print("1)Calcular Area de un cuadrado\n")
        print("2)Calcular Area de un triangulo\n")
        print("3)Calcular Area de un circulo\n")
        opcion_menu=int(input("Escoge una opcion"))
        if opcion_menu== 1:
            Area_cuadrado();
        elif opcion_menu== 2:
            Area_triangulo();
        elif opcion_menu== 3:
            Area_circulo();
        else:
            print("La opcion no es valida")
Menu();