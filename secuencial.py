#Ejercicios Taller Secuencial - Carlos Ayala

#1. Hacer un algoritmo que calcule el total a pagar por la compra de
#camisas. Si se compran tres camisas o mas se aplica un descuento
#del 30% sobre el total de la compra y si son menos de tres camisas
#un descuento del 10%.

# Ejercicio 1
def num1(n,price):
  total = price*n
  if n<3:
    desc = total*0.1
  else:
    desc = total*0.2
  print("Total a pagar: "+str(total-desc))    
  print("######################################################")    

#2. En un supermercado se hace una promoción, mediante la cual el
#cliente obtiene un descuento dependiendo de un número que se
#escoge al azar. Si el número escogido es menor que 74 el descuento
#es del 15% sobre el total de la compra, si es mayor o igual a 74 el
#descuento es del 20%. Obtener cuanto dinero se le descuenta.

# Ejercicio 2
def num2(n,total):
  if n<74:
    desc = total*0.15
  else:
    desc = total*0.2
  print("Total a pagar: "+str(desc))    
  print("######################################################")  

#3. Una compañía de seguros está abriendo un departamento de
#finanzas y estableció un programa para captar clientes, que conssite
#en lo siguiente: Si el monto por el que se efectúa la fianza es menor
#que $50.000 la cuota a pagar será por el 3% del monto, y si el monto
#es mayor que $50.000 la cuota a pagar será el 2% del monto. La
#afianzadora desea determinar cual será la cuota que debe pagar al
#cliente.

# Ejercicio 3
def num3(cap):
  if cap<50000:
    inter = cap*0.3
  else:
    inter = cap*0.2
  print("Total a pagar: "+str(cap + inter))    
  print("######################################################")  

#4. Una fábrica ha sido sometida a un programa de control de
#contaminación para lo cual se efectúa una revisión de los puntos de
#contaminación generados por la fábrica. El programa de control de
#contaminación consiste en medir los puntos que emite la fábrica en
#cinco días de una semana y si el promedio es superior a los 170
#puntos entonces tendrá la sanción de parar su producción por una
#semana y una multa del 50% de las ganancias diarias cuando no se
#detiene la producción. Si el promedio obtenido de puntos es de 170 o
#menos entonces no tendrá ni sanción ni multa. El dueño de la fábrica
#desea saber cuanto dinero perderá después de ser sometido a la
#revisión.

#5. Una persona se encuentra con un problema de comprar un automóvil
#o un terreno, los cuales cuestan exactamente lo mismo. Sabe que
#mientras el automóvil se devalúa, con el terreno sucede lo contrario.
#Esta persona comprará el automóvil si al cabo de tres años la
#devaluación de este no es mayor que la mitad del incremento del 
#valor del terreno. Ayúdale a esta pesona a determinar si debe o no
#comprar el automóvil.

#6. En una fábrica de computadoras se planea ofrecer a los clientes un
#descuento que dependerá del número de computadoreas que
#compre. Si las computadoras son menos de cinco se les dará un 10%
#de descuento sobre el total de la compra; si el número de
#computadoras es mayor o igual a cinco pero menos de diez se le
#otorga un 20% de descuento; y si son 10 o más se les da un 40%. El
#precio de cada computadora es de $11.000.

#7. Un proveedor de estéreos ofrece un descuento del 10% sobre el
#precio sin IVA, de algún aparato si este cuesta $2000 o más. Además,
#independientemente de esto, ofrece un 5% de descuento si la marca
#es NOSY. Determinar cuanto pagará, con IVA incluido, un cliente
#cualquiera por la compra de su aparato. IVA es del 16%.

#8. Una empresa quiere hacer una compra de varias piezas de la misma
#clase a una fábrica de refacciones. La empresa, dependiendo del
#monto total de la compra, decidirá que hacer para pagar al fabricante.
#Si el monto total de la compra excede de $500.000 la empresa tendrá
#la capacidad de invertir de su propio dinero un 55% del monto de la
#compra, pedir prestado al banco un 30% y el resto lo pagará
#solicitando un crédito al fabricante. Si el monto total de la compra no
#excede de $500.00 la empresa tendrá capacidad de invertir de su
#propio dinero un 70% y el restante 30% lo pagará solicitando crédito
#al fabricante. El fabricante cobra por concepto de interes un 20%
#sobre la cantidad que se le pague a crédito. Obtener la cantidad a
#inverir, valor del préstamo, valor del crédito y los intereses.

#9. Leer 2 números; si son iguales que lo multiplique, si el primero es
#mayor que el segundo que los reste y sino que los sume.

#10. Leer tres números diferentes e imprimir el número mayor de los
#tres.