salario = float(input("Digite seu salario R$: "))
aumento = float(input("Digite o percentual do aumento % "))
novosalario= ((salario / 100) * aumento) + salario
print("Seu novo salario é: ",round( novosalario, 2))