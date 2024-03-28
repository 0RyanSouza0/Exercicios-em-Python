tam=int(input("Digite a quantidade de vezes que deseja saber o consumo de taxa do combustivel: "))
for x in range (0,tam,+1): 
    print("_________________________________")
    km=float(input("Digite o KM percorrido do carro: "))
    gasolina=float(input("Digite o combustivel consumido do carro: "))
    conv= km/gasolina

    if(conv <=8 ):
        print("O automovel esta consumindo  muito  combustivel ",conv, "L")
    else:
        print("A taxa de consumo do automovel esta boa: ", conv,"L")
    print("__________FIM DO PROGRAMA____________")