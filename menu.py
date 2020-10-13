import os

def Temperaturas():
    suma=0
    print ("--- Opción de Temperaturas ---")
    veces=int(input("Cuantas temperaturas ingresa ?: "))
    for x in range(veces):
        tempe=float(input("Ingrese temperatura: "))
        suma=suma+tempe
    print("El promedio de las temperaturas es: ", round((suma/veces),2))
    wait=input("")

def Personas():
    cont=0
    conta=0
    print ("--- Opción de Datos de Personas ---")
    veces=int(input("Cuantas personas ingresa ?: "))
    for x in range(veces):
        edad=int(input("Ingrese edad: "))
        if(edad>=18):
            cont=cont+1 
        elif(edad<=17):
            conta=conta+1    
    print("La cantidad de personas que son mayores de edad son: "+ str(cont))
    print("La cantidad de personas que son menores de edad son: "+ str(conta))
    wait=input("")

    

seguir=True
while seguir:
    os.system('cls')
    print ("1. Temperaturas")
    print ("2. Datos de personas")
    print ("3. Salir.")
    op=int(input("Ingrese opción 1,2,3: "))
    if(op==1):
        Temperaturas()      #invocamos a una función
    if(op==2):
        Personas()          #invocamos a una función
    if(op==3):
        print("Programa Finalizado")
        break

