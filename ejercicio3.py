alimentos = [["A", "B", "C"], [270,340,390]]
contador = 0
opcionEscogida = 0
bandera = True
bandera2 = True

def compraRealizada (alimentos, bandera2):
    sumaMonedas = 0
    
    while(bandera2):
        try:
            print("Ingrese una moneda, solo de 10, 50 o 100")
            while(sumaMonedas < alimentos[1][opcionEscogida]):
                valorMoneda = int(input(""))
                if valorMoneda == 10 or valorMoneda == 50 or valorMoneda == 100:
                    sumaMonedas = sumaMonedas + valorMoneda
                    bandera2 = False
                else:
                    raise 
        except: 
            print("Asegurese de ingresar la moneda indicada")
            bandera2 = True
       
    print("Aqui tiene su vuelto")
    return sumaMonedas

def entregaVuelto (alimentos,x):
    vuelto = x - alimentos[1][opcionEscogida]

    if vuelto < 50 and vuelto != 0:
        while(vuelto > 0):
            print("10")
            vuelto = vuelto - 10
    elif vuelto == 50:
        print(f"{vuelto}")
    elif vuelto > 50:
        print(f"50")
        vuelto = vuelto - 50
        while(vuelto > 0):
            print("10")
            vuelto = vuelto - 10
    elif vuelto == 0:
        print("0")
    return

while(bandera):
    print("Elegir el producto")
    for i in alimentos[0]:
        print(f"\t{contador}. {i}")
        contador+=1
    try:
        opcionEscogida = int(input("\n"))
        if opcionEscogida <= len(alimentos[0])-1 and opcionEscogida>=0: 
            bandera = False      
        else: raise
        print(f"Ha elegido el producto {alimentos[0][opcionEscogida]}: valor {alimentos[1][opcionEscogida]}")
    except:
        print("usuario en serio sea serio >:(")
        bandera = True
        contador = 0

x = compraRealizada(alimentos, bandera2)
entregaVuelto(alimentos,x)