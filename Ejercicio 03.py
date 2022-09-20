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
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#TODO: Seguir realizando la verificación del codigo
class Taller:
    def __init__(self, fechaentr, cost, model, año, dueño):
        self.fechaentr = fechaentr
        self.cost = cost
        self.model = model
        self.año = año
        self.dueño = dueño
    def empleados (self, nombreem, cargoem, salarioem, vehiculoem, documentoem):
        self.nombreem=nombreem
        self.cargoem=cargoem
        self.salarioem=salarioem
        self.vehiculoem=vehiculoem
        self.documentoem=documentoem
    def garage (self,tiempog):
        costog=100000*tiempog
        self.costog=costog
        print('Por mantener el vehículo bajo el cuidado del local durante', tiempog, 'horas, se le ha generado una factura por', self.costog,'$')
    def caja(self, paga):
        dinero_dispo=1000000000
        dinero_dispo+=paga
        listacaja=[]
        if paga >= self.cost:
            y = paga - self.cost
            print("El vehiculo ha sido retirado con éxito, se le han devuelto ", y, "$ pesos.")
            self.caja='El vehículo ha sido retirado.'
            x='Vehiculo', self, 'ha sido retirado.'
            dinero_dispo=dinero_dispo-y
            listacaja.append(x)
        else:
            print("Para poder retirar este vehiculo, es necesaria una mayor suma de dinero.")
    def admin_contra(self,proced,nombrea,cargoa,salarioa,vehiculoa,documentoa):
        listanuev = []
        if proced=='Despedir':
            z=input('Identificacion del empleado')
            for i in listanuev:
                if i==z:
                    listanuev.pop[i]
        elif proced=='Contratar':
            listanuev.append(admin_contra(self,nombrea,cargoa,salarioa,vehiculoa,documentoa))
    def pagar_em(self,cantidad):
        self.salarioem=salarioem+cantidad
    def base_datos(self,nombreu):
        for j in listanuev:
            if j==nombreu:
                print('El usuario ha sido encontrado y su vehículo es:',self.modelo)
            else:
                tr=False
        if tr==False:
            print('Lo sentimos, el usuario no ha sido encontrado')

# Lista de los vehículos registrados anteriormente.

v_01 = Taller('19/09/2009', 90000000, 'Toyota', 2008, 'Erick Ortiz')
v_02 = Taller('11/03/2011', 65000000, 'Chevrolet', 2009, 'Mateo Flores')
v_03 = Taller('31/05/2022', 150000000, 'Tesla', 2021, 'Kevin Rodriguez')
#Para ingresar un vehículo al taller ejecutar mediante la consola lo siguiente:
#v_04(número del vehículo)= Taller('Fecha', valor, 'Modelo', Año, 'Nombre')

#Lista de los empleados.
#p_01.empleados ('Laura Rodriguez', 'Gerente', 5000000, 'Susuki gixxer', 102387699)
#p_02.empleados ('Juan Muñoz', 'Jefe de ventas', 2000000, 'Toyota yaris', 108723902)
#p_03.empleados ('Mauro Zapata', 'Supervisor', 3000000, 'Tesla model 3', 101245671)
#p_04.empleados ('Johana Gutierrez', 'Contadora', 1800000, 'Chevrolet camaro', 105334118)
