
# Leer un numero entero y determinar si es negativo

num = int(input("Ingrese un numero: "))

if num < 0:
    print(f"El {num} es negativo")
else: 
    print(" el numero es positivo")


#Leer un numero entero y determinar cuantos digitos tiene

num2 = input("Ingrese un numero entero: ").strip()

if num2.startswith('-'):
    num2= num2[1:]  #modificacion apra eliminar un signo negativo
print(f"El numero tiene {len(num2)} digitos.")


## Leer un numero entero y determinar si es primo

num3 = int(input("Inregrese un numero: "))

def es_primo(n):

    if n<= 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            return False
    return True
    
if es_primo(num3):
    print("El numero es primo.")
else:
    print("El numero no es primo")

#Leer 4 enteros, alamcenarlos en una lista y determinar en que 
#posicion de la lista esta el mayor numero leido

num4= []
for i in range(4):
    num8 = int(input(f"Ingrese el numero {i+1}: "))
    num4.append(num8)

mayor = max(num4)
posicion = num4.index(mayor)

print(f"El numero mayor es {mayor} y esta en la posicion {posicion} de la lista")



numeross = [1,1,2,3,3,2,5,6,2,7,8,4,3,1]
numeros_sin_dupl= list(dict.fromkeys(numeross))
print(f"Aqui esta la lista sin los duplicados {numeros_sin_dupl}")


