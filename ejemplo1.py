#Ingresar dos números
a=int(input("Ingrese un número: "))
b=int(input("Ingrese otro número: "))
#Operaciones matemáticas
suma=a+b
multi=a*b
print("La suma de "+ str(a)+ "Con el número" + str(b) + "es igual a: " + str(suma))
print("La multiplicación de "+ str(a)+ "Con el número" + str(b) + "es igual a: " + str(multi))
#Crear condición
if (a>b):
    print("El número: " + str(a) + "Es mayor a: "+ str(b))
elif (a<b):
    print("El número: " + str(b) + "Es mayor a: "+ str(a))
else:
    print("Los números son iguales.")

wait=input("")