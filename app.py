
dato1 = input("Ingresa un numero ")

try:
    dato1 = int (dato1)
    if dato1 > 5:
        print("el color es rojo")
    elif dato1 == 3:
        print("el color es amarillo")
    elif dato1 < 10:
        print("el color es azul")
except ValueError:
    print("El color no existe")
    

hora = input("Ingrese una hora del dia (0-23)") 
hora=int(hora)
if hora>=6 and hora<12:
    print("Buenos dias")
elif hora>=13 and hora<18:
    print("Buenas tardes")
else:
    print("Buenas noches")


numero1 = int(input("Ingrese primer numero "))
numero2 = int(input("Ingrese segundo numero "))

suma = numero1 + numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2
resta = numero1 - numero2

print ("La suma de los dos numeros es: ", suma)
print ("La resta de los dos numeros es: ", resta)
print ("La multiplicación de los dos numeros es: ", multiplicacion)
print ("La división de los dos numeros es: ", division)


edad = int(input("Ingrese su edad: "))

if edad in range(0,5):
    print("Eres un infante")
elif edad in range(6,11):
    print("Eres un niño")
elif edad in range(13,20):
    print("Eres un adolescente")
elif edad in range(21,25):
    print("Eres un joven")
elif edad in range(26,60):
    print("Eres un adulto")
elif edad in range(60,100):
    print("Eres un anciano")
else:
    print("Estás pagando horas extras")
    