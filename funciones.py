import math

h= 0
s= 0
m= 0
hora= [0,0,0]
option= 1

def horas(h,variabley):
   h+=variabley
   return h
    

def minutos(h,m,variabley):
    w = m+variabley
    if w>59:
        me=w/60 #Para Calcular la cantidad de horas
        tp=math.modf(me) #para separa la parte decimal de la parte flotante
        x=math.ceil(tp[1]) #para que la parte flotante sea redondada con el fin de obtener los minutos restantes
        me=math.ceil(tp[0]*60)#reemplaza la cantidad de horas, por exactamente horas de la parte entera
        h+=x
        m=me
        return h,m
    else:
        m=m+variabley
        return h,m

def segundos(h,m,s,variabley):
    w = s+variabley     
    if w>59:
        me=w/60
        tp=math.modf(me)
        x=math.ceil(tp[1])
        me=math.ceil(tp[0]*60)
        if me==60:
            me=59
        x+=m
        flipendo = minutos(h,x,0)
        
        s=me
        return flipendo[0],flipendo[1],s
    else:
        s=s+variabley
        return h,m,s

            

while option == 1:
    validar =""
    print("Bienvenido a la aplicacion para calcular la hora, en este momento estas en=> ",hora, " => hh:mm:ss" )
    validar = input("Que deseas añadir? horas(h) minutos(m) o segundos(s)? (X para salir)(Escriba alguna opcion dentro del parentesis)=> ")
    if validar == "h":
        cantidad = int(input("Cuantas horas desea ingresar al sistema?  => "))        
        hora[0]=horas(h, cantidad)
        h=hora[0]
    elif validar == "m":
        cantidad = int(input("Cuantos minutos desea ingresar al sistema?  => "))
        flipendo=minutos(h, m, cantidad)
        hora[0]=flipendo[0]
        hora[1]=flipendo[1]
        h=hora[0]
        m=hora[1]
    elif validar == "s":
        cantidad = int(input("Cuantos segundos desea ingresar al sistema?  => "))
        engordio=segundos(h,m,s,cantidad)
        print(type(engordio))
        hora[0]=engordio[0]
        hora[1]=engordio[1]
        hora[2]=engordio[2]
        h=hora[0]
        m=hora[1]
        s=hora[2]
    else:
        break




