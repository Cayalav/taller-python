#Ejercicios Taller Secuencial - Carlos Ayala

# Ejercicio 1
def num1(i1,i2,i3):
  total = (i1 + i2 + i3)
  print("El porcentaje para la persona 1 es: "+(i1/total)*100+"%")
  print("El porcentaje para la persona 2 es: "+(i2/total)*100+"%")
  print("El porcentaje para la persona 3 es: "+(i3/total)*100+"%")
  print("######################################################")    


# Ejercicio 2
def num2(hi,sal):
  bono = hi*80000
  total = sal + bono
  print("Total bono: "+str(bono))    
  print("Total a pagar: "+str(total))  
  print("######################################################")  



# Ejercicio 3
def num3(si):
  sf=si+(si*0.015)
  print("Total a saldo final: "+str(sf))  
  print("######################################################")  



# Ejercicio 4
def num4(metcua):
  deuda = metcua * 80000
  ci = deuda * 0.35
  print("Cuota inicial: "+str(ci))
  print("Cuotas por 12: "+str(deuda*0.75/12))
  print("######################################################")  



# Ejercicio 5
def num5(sb):
  lp=sb*0.01
  ss=sb*0.04
  sd=sb*0.005
  ca=sb*0.05
  mt=sb-lp-ss-sd-ca
  print ('Valor de caja de ahorro: ' + str (ca))
  print ('Valor de ley de politica habitacional: ' + str (lp))
  print ('Valor de monto total a pagar: ' + str (mt))
  print ('Valor de seguro de desempleo: ' + str (sd))
  print ('Valor de seguro social: ' + str (ss))
  print("######################################################")  

#6. El periódico el Informador cobra por un aviso clasificado un monto
#que depende del número de palabras, tamaño en cetímetros y
#número de colores. Cada palabra tiene un costo de $20.000, cada
#centímetro tiene un costo de $15.000 y cada color tiene un costo de
#$25.000. Realice un algoritmo que determine el monto a pagar por un
#aviso clasificado.

# Ejercicio 6
def num6(cap):
  if cap<50000:
    inter = cap*0.3
  else:
    inter = cap*0.2
  print("Total a pagar: "+str(cap + inter))    
  print("######################################################")  

#7. Una empresa paga a sus empleados un bono por antigüedad que
#consiste en $100.000 por el primer año laboral y $120.000 por cada
#año siguiente. Realice un programa en Java que determine el monto
#del bono a pagar a un trabajador que tiene varios años en la empresa.

# Ejercicio 7
def num7(cap):
  if cap<50000:
    inter = cap*0.3
  else:
    inter = cap*0.2
  print("Total a pagar: "+str(cap + inter))    
  print("######################################################")  

#8. Una Universidad le paga a sus profesores $20.000 la hora y le hace
#un descuento del 5% por concepto de caja de ahorro. Determine el
#monto del descuento y el monto total a pagar al profesor.

# Ejercicio 8
def num8(cap):
  if cap<50000:
    inter = cap*0.3
  else:
    inter = cap*0.2
  print("Total a pagar: "+str(cap + inter))    
  print("######################################################")  

#9. Un centro de comunicaciones alquilan tarjetas para realizar llamadas
#y cobran el monto consumido de la tarjeta mas un recargo del 20%.
#Teniendo como dato de entrada el monto inicial y el monto final de la
#tarjeta, determine el costo de la llamada.

# Ejercicio 9
def num9(cap):
  if cap<50000:
    inter = cap*0.3
  else:
    inter = cap*0.2
  print("Total a pagar: "+str(cap + inter))    
  print("######################################################")  

#10. En una fototienda cobran por el revelado de un rollo $1.500 por cada
#foto. Realice un programa en Java que determine el monto a pagar
#por un revelado completo sabiendo que adiconalmente le cobran el
#IVA (16%).

# Ejercicio 10
def num10(cap):
  if cap<50000:
    inter = cap*0.3
  else:
    inter = cap*0.2
  print("Total a pagar: "+str(cap + inter))    
  print("######################################################")  

#10. En una fototienda cobran por el revelado de un rollo $1.500 por cada
#foto. Realice un programa en Java que determine el monto a pagar
#por un revelado completo sabiendo que adiconalmente le cobran el
#IVA (16%).
#Gineco=40%
#Trauma=30%
#Pediatria=30%
#Obtener la cantidad de dinero que recibirá cada área, para cualquier
#monto presupuestal.

# Ejercicio 11
def num11(cap):
  if cap<50000:
    inter = cap*0.3
  else:
    inter = cap*0.2
  print("Total a pagar: "+str(cap + inter))    
  print("######################################################")  

#12. Una video tienda alquila DVD a $1.500 el día. Tiene una promoción
#que consiste en dejar gratis el alquiler de una película. Realice un
#programa en Java que teniendo como dato de entrada el total de
#películas alquiladas, y el número de días de alquiler, determine el
#monto a pagar.

# Ejercicio 12
def num12(cap):
  if cap<50000:
    inter = cap*0.3
  else:
    inter = cap*0.2
  print("Total a pagar: "+str(cap + inter))    
  print("######################################################")  

#13. Una Agencia de viajes cobra por un Tour a Cartagena $25.000
#diarios por persona. Realice un programa en Java que determine el
#monto a pagar por una familia que desee realizar dicho Tour
#sabiendo que también cobran el 12% de IVA.

# Ejercicio 13
def num13(cap):
  if cap<50000:
    inter = cap*0.3
  else:
    inter = cap*0.2
  print("Total a pagar: "+str(cap + inter))    
  print("######################################################")  

#14. Un Hotel 5 Estrellas de Santa Marta tiene una promoción para sus
#clientes. Cobra por una habitación $100.000 el primer día y por el
#resto $200.000 por día. Realice un programa en Java que determine
#el valor total a pagar por la habitación si la estadía fue de varios
#días.

# Ejercicio 14
def num14(cap):
  if cap<50000:
    inter = cap*0.3
  else:
    inter = cap*0.2
  print("Total a pagar: "+str(cap + inter))    
  print("######################################################")  

#15. El banco del Pueblo da microcréditos a empresarios para ser
#cancelados en un lapso de 2 años (24 meses). Al monto del
#préstamo se le cobra un interés del 24%. El empresario debe pagar
#la mitad del préstamo en 4 cuotas especiales y la otra mitad en 20
#cuotas ordinarias. Realice un algoritmo que teniendo como dato de
#entrada el monto del préstamo, determine el monto total a pagar por
#el préstamo, el monto de las cuotas especiales y el monto de las
#cuotas ordinarias.

# Ejercicio 15
def num15(cap):
  if cap<50000:
    inter = cap*0.3
  else:
    inter = cap*0.2
  print("Total a pagar: "+str(cap + inter))    
  print("######################################################")  