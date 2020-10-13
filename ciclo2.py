#Ingresar un número donde n es un número ingresado por el teclado (ciclo while)
#Mostrar cuantos son positivos, negativos e iguales a 0.

veces=int(input("Cuántos números desea ingresar?: "))
x=1
pos=0
neg=0
cero=0
while(x<=veces):
    num=int(input("Digite un número: "))
    if(num>0):
        pos=pos+1
    elif(num<0):
        neg=neg+1
    else:
        cero=cero+1
    x=x+1
print("La cantidad de números positivos es: "+str(pos)+ 
" La cantidad de números negativos es: "+str(neg) +
" La cantidad de ceros es: "+ str(cero))