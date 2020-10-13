#Crear ciclo que permita ingresar 10 números contar y mostrar: cuantos son pares y cuantos impares.

par=0
impar=0
for x in range(10):
    num=int(input("Digite un número: "))
    if (num%2==0):
        par=par+1
    else:
        impar=impar+1

print ("La cantidad de números pares es: "+ str(par) +
 " La cantidad de números impares es: " +str(impar))