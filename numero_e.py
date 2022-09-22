def factorial(numero):
    iterador=1
    numero2=1
    while iterador <=numero:
        numero2=iterador *numero2
        iterador+=1
    return numero2

def Menu():
    while True:
        limite=int(input("ingrese el limite deseado:"));
        n=0
        e=0
        while n < limite:
           
           e+= (1/factorial(n))
           n=n+1;
        print("El valor de e es: ",e);
Menu();