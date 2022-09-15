'RECURSION'

'EJERCICIO 01'

def f_contar(s_num): # se inicia la función, esta debe tener un parametro que sirva como memoria del sistema
    if s_num < 10: # si el número actual es menor que 10, aumentar en uno y volver a correr la función
        print (s_num) #se imprime el valor que se va contando
        s_num+=1
        return f_contar(s_num) # al correr nuevamente la función, ingresa con s_num + 1 como parametro por lo que cada vez incrementa
    else:
        return s_num # finalmente cuando se cumple la condición se retorna el valor final

print(f_contar(1))

'EJERCICIO 02'
def f_contar(s_num,s_obj): # se inicia la función, esta debe tener un parametro que sirva como memoria del sistema y el objetivo, es decir, el número que finaliza la secuencia.
    if s_num < s_obj+1: # si el número actual es menor que 10, aumentar en uno y volver a correr la función
        print(s_num)  #Tomando como base el código anterior
        s_num+=1
        return f_contar(s_num,s_obj) # al correr nuevamente la función, ingresa con s_num + 1 como parametro por lo que cada vez incrementa
    else:
        return s_num # finalmetne cuando se cumple la condición se retorna el valor final

f_contar(1,10)


'EJERCICIO 03'
def f_contar(s_num,s_obj,s_paso): # se inicia la función, esta debe tener un parametro que sirva como memoria del sistema
    if s_num < s_obj-1: # si el número actual es menor que 10, aumentar en uno y volver a correr la función
        print(s_num) #Se escribe el número registrado
        s_num+=s_paso  #Aqui el cambio que se observa es en la suma, ya no es 1 sino que es el paso, es decir, si una persona desea ir de 2 en 2 el código se ira sumando por 2 .
        return f_contar(s_num,s_obj,s_paso) # al correr nuevamente la función, ingresa con s_num + s_paso como parametro por lo que cada vez incrementa
    else:
        return s_num # finalmetne cuando se cumple la condición se retorna el valor final
#Ejecutar en la consola-


'TORRE DE HANOI'

def torre_H(d,A,B,C): #Inciia la funcion tomando como base el número de discos y las 3 columnas.
  if(d>0):     #Condicional que permite crear un bucle que analiza las opciones para pasar el disco de una torre a otra
    torre_H(d-1,A,B,C)   #Recursión, se le resta 1 al número de discos
    print('Pasar el primer anillo de la torre '+str(A)+ ' hasta la torre ' +str(B)) #Instrucción
    torre_H(d-1,C,B,A)  #Recusión 2, se toman las columnas en orden descendente para continuar el bucle.
torre_H(1,'A','B','C')