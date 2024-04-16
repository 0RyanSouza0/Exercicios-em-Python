idade= int(input("Digite sua idade: "))

while idade <5:
    print("Número invalido, digite novamente")
    idade= int(input("Digite sua idade: "))

if idade >=5 and idade <=7:
    print("Sua categoria é infantil A ")

elif idade >=8 and idade <=10:
    print("Sua categoria é infantil B ")

elif idade >=11 and idade <=13:
    print("Sua categoria é juvenil A ")

elif idade >=14 and idade <=17:
    print("Sua categoria é juvenil B ")
else:
    print("Sua categoria é ADULTO")


