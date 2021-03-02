#Ejercicios Taller Secuencial - Carlos Ayala

# Ejercicio 1
def num1(i1,i2,i3):
  total = (i1 + i2 + i3)
  print(f"El porcentaje para la persona 1 es: {(i1/total)*100}%")
  print(f"El porcentaje para la persona 2 es: {(i2/total)*100}%")
  print(f"El porcentaje para la persona 3 es: {(i3/total)*100}%")
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

# Ejercicio 6
def num6(pal, tam, col):
  total = (pal*20000)+(tam*15000)+(col*25000)
  print(f"El total a cobrar por el aviso clasificado es: {total}")
("######################################################")  

# Ejercicio 7
def num7(year):
  total = 100000 + (120000*year)
  print(f"El monto por bono de antiguedad es: {total}")   
  print("######################################################")  

# Ejercicio 8
def num8(time):
  pago = (20000*time)
  total = pago - (pago * 0.05)
  print(f"El monto total a pagar al profesor es: {total}") 
  print("######################################################")  

# Ejercicio 9
def num9(init, finit):
  cons = init-finit
  rec = cons * 0.2
  total = cons + rec
  print(f"El total a cobrar al cliente es {total}") 
  print("######################################################")  

# Ejercicio 10
def num10(pic):
  net = pic * 1500
  total = net + (net * 0.16)
  print(f"El monto total por el revelado (Incluyendo IVA DE 16%) es: {total}")  
  print("######################################################")  

# Ejercicio 11
def num11(monto):
  gine = monto * 0.4
  trauma = monto * 0.3
  pedia = monto * 0.3
  print(f'''Para el monto total {monto}
  el área de ginecología recibirá {gine}
  el área de traumatología recibirá {trauma}
  y, el área de pediatría recibirá {pedia}''')   
  print("######################################################")  

def num12(cantidad,dias):
  total = (1500*dias)*(cantidad-1)
  print(f"El monto total a pagar por el alquiler de {cantidad} películas por {dias} días es: {total}") 
  print("######################################################")  

# Ejercicio 13
def num13(cantidad,dias):
  net = (25000*dias)*cantidad
  total = net + (net*0.12)
  print(f"El monto total a pagar es: {total}")  
  print("######################################################")  

# Ejercicio 14
def num14(dias):
  total = (100000)+(200000*(dias-1))
  print(f"El a pagar es: {total}")  
  print("######################################################")  

# Ejercicio 15
def num15(monto):
  interes = monto * (0.24)
  total = monto + interes
  esp = (total*0.5)/4
  ordi = (total*0.5)/20
  print(f"El monto total a pagar es: {total}, el valor de las cuatro cuotas especiales es: {esp} y el de las 20 {ordi}")  

num1(4,2,1)
num2(2,3000)
num3(120000)
num4(90)
num5(800000)
num6(23,2,310)
num7(10)
num8(20)
num9(20,50)
num10(2100)
num11(20000)
num12(20000,3)
num13(230,200)
num14(365)
num15(100000)
