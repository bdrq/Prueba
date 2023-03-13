validar = 1
while validar == 1:
    numerador = int(input("Por favor ingrese el nummerador=> "))
    denominador = int(input("Por favor ingrese el denominador=> "))
    try:
        result = numerador/denominador
    except:
        print("El denominador no puede ser igual a cero")
        continue
    else:
        print("El resultado de la division es => ",result)
        validar = int(input("Desea operar de nuevo?=> "))
        print(validar)