
valor1= float(input("Digite a primeira nota: "))
valor2= float(input(" Digite a segunda nota: "))

media= (valor1 + valor2)/2

print("Sua media é: ",media)
#print (" media= {}".format(media))

if media>=6:
    print("Aprovado 😁")

elif media >=3:
    print("Recuperação😑")
    valor3= float(input("Digite sua nota de recuperação: "))
    if (valor1+ valor2 + valor3)/ 3 >=6:
        print("Aprovado 😁")
    else:
        print("Reprovado mesmo assim 😭")
