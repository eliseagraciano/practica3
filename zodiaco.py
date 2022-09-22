def Main():
    while True:
        dia_nacimiento=int(input("\nIngresa el día en que naciste: "));
        mes_nacimiento=int(input("Ingresa el mes en que naciste, rango de 1 a 12: "));
        
        if dia_nacimiento >= 21 and mes_nacimiento == 3 or dia_nacimiento <= 20 and mes_nacimiento == 4:
            print("Tu signo zodiacal es Aries.");
        elif dia_nacimiento >= 21 and mes_nacimiento == 4 or dia_nacimiento <= 20 and mes_nacimiento == 5:
            print("Tu signo zodiacal es Tauro.");
        elif dia_nacimiento >= 21 and mes_nacimiento == 5 or dia_nacimiento <= 21 and mes_nacimiento == 6:
            print("Tu signo zodiacal es Geminis.");
        elif dia_nacimiento >= 22 and mes_nacimiento == 6 or dia_nacimiento <= 22 and mes_nacimiento == 7:
            print("Tu signo zodiacal es Cancer.");
        elif dia_nacimiento >= 23 and mes_nacimiento == 7 or dia_nacimiento <= 23 and mes_nacimiento == 8:
            print("Tu signo zodiacal es Leo.");
        elif dia_nacimiento >= 24 and mes_nacimiento == 8 or dia_nacimiento <= 22 and mes_nacimiento == 9:
            print("Tu signo zodiacal es Virgo.");
        elif dia_nacimiento >= 23 and mes_nacimiento == 9 or dia_nacimiento <= 22 and mes_nacimiento == 10:
            print("Tu signo zodiacal es Libra.");
        elif dia_nacimiento >= 23 and mes_nacimiento == 10 or dia_nacimiento <= 22 and mes_nacimiento == 11:
            print("Tu signo zodiacal es Escorpio.");
        elif dia_nacimiento >= 23 and mes_nacimiento == 11 or dia_nacimiento <= 21 and mes_nacimiento == 12:
            print("Tu signo zodiacal es Sagitario.");
        elif dia_nacimiento >= 22 and mes_nacimiento == 12 or dia_nacimiento <= 20 and mes_nacimiento == 1:
            print("Tu signo zodiacal es Capricornio.");
        elif dia_nacimiento >= 21 and mes_nacimiento == 1 or dia_nacimiento <= 19 and mes_nacimiento == 2:
            print("Tu signo zodiacal es Acuario.");
        elif dia_nacimiento >= 20 and mes_nacimiento == 2 or dia_nacimiento <= 20 and mes_nacimiento == 3:
            print("Tu signo zodiacal es Picis.");
        else:
            print("Datos incorrectos...");
Main();