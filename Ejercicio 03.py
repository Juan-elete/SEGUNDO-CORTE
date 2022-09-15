'EJERCICIOS 03'



#Demuestre por inducción que, para todo n mayor o igual que 4, n!>2^n


#Primero se deben seguir los pasos de inducción matemática, iniciando con la comprobación de que cuando n=4 esto se cumple.
#Este proceso se evidencia en el primer ASSERT en la parte final del código.
#Ahora, es necesario plantear la hipótesis de inducción, suponiendo que esta ecuación es cierta para K que pertenezca a los números naturales, teniendo en cuenta que K es mayor o igual que 4.
#Este proceso se evidencia en el segundo ASSERT en la penúltima linea del código.
#Para realizar el primer paso, se crea la funcion:
def ecuacion (num):
    fact = 1
    while (num > 1):
        fact *= num
        num -= 1
    #print(fact)
    ec1 = fact
    ec2 = 2**num
    if ec1>ec2:
        print("Correcto.")
        return True
    else:
        print("Incorrecto.")
        return False
#Para realizar el segundo paso se crea la funcion con K:
#RECORDAR QUE K=NUM+1
def ecuacion2 (k):
    fact = 1
    while (k > 1):
        fact *= k
        k -= 1
    # print(fact)
    ec1 = fact
    ec2 = 2 ** k
    if ec1 > ec2:
        print("Correcto.")
        return True
    else:
        print("Incorrecto.")
        return False
#Para finalizar y hacer uso de la recursión, se puede modificar el código de la siguiente manera:
def ecuacionr (num):
    fact = 1
    while (num > 1):
        fact *= num
        num -= 1
    #print(fact)
    ec1 = fact
    ec2 = 2**num
    if ec1>ec2:
        print("Correcto.")
        return True
    else:
        print("Incorrecto.")
        return False
    k=ecuacionr(num+1)         #Se llama la función ella misma para verificar el paso 3, si tomando en cuenta el número natural k+1 el código sigue funcionando.
assert ecuacion(4)==True #En esta linea se puede evidenciar que cuando n=4 la ecuacion es CORRECTA.
assert ecuacion2(4+1)==True #En esta segunda linea se evidencia que en el momento que la variable sea k+1 la ecuacion es CORRECTA.
assert ecuacionr(5)==True #Última verificación, para demostrar que por recursión el código funciona perfectamente.


#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#Un granjero ha comprado una pareja de conejos para criarlos y luego venderlos.
#   Si la pareja de conejos produce una nueva pareja cada mes y la nueva pareja
#   tarda un mes más en ser también productiva, ¿cuántos pares de conejos podrá
#   poner a la venta el granjero al cabo de un año?

def conejos(m):       #Inicio de la funcion
    n1 = 1       #Se asigna la primera y la segunda variable
    n2 = 0
    l_vacia = []     #Se crea una lista para administar los valores
    for i in range(0, m + 1):      #Bucle para crear la serie de Fibonacci
        n2 = n2 + n1
        n1 = n2 - n1
        l_vacia.append(n1)
    print("El granjero podrá vender", l_vacia[12],"parejas de conejos.")  # El resultado de la serie de Fibonacci se da en parejas de conejos, es decir, si dice 1 es que hay 2 conejos, si dice 2 hay 4, etc.
conejos(12)  #Se evalúa la función con el número de meses

