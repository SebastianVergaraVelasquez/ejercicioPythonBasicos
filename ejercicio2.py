import random

def valorDolar(valoresDiarios,dias):
    for i in range(dias):
        dolarDia = random.uniform(100,999)
        valoresDiarios.append(dolarDia)
        print(f"Día {i+1}: {dolarDia}")
    return

def determinarAlzas(valoresDiarios,alzas,dias, bandera2):
    contador = 0
    while(bandera2 == True):
         for i in range(dias-1):
            if valoresDiarios[i+1] < valoresDiarios[i]:
                contador = contador + 1
                if contador == dias-1:
                    bandera2 = False
            else:
                bandera2 = False
    if contador == dias - 1:
            print('No hay alzas')
    else: 
         for i in range(dias-1):
            if valoresDiarios[i+1] > valoresDiarios[i]:
                alzas.append(valoresDiarios[i+1]-valoresDiarios[i])
         mayorAlza = max(alzas)
         print(f"la mayor alza fue de: {mayorAlza}")
    
    return

valoresDiarios = []
alzas = []
bandera1 = True
bandera2 = True

while(bandera1):
    print("Ingrese el periodo de días a estudiar")
    try:
        dias = int(input())
        if dias >= 2:
            bandera1 = False
        else:
            raise
    except:
        print("ingrese un valor mayor o igual a 2 >:(")
        bandera1 = True


valorDolar(valoresDiarios,dias)
determinarAlzas(valoresDiarios, alzas, dias, bandera2)

