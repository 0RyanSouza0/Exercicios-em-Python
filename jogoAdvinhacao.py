
jogador1 = int(input("Digite um numero de 1 a 10: "))
while (jogador1 <1 ) or (jogador1>10):
    print("Número invalido, digite novamente")
    jogador1 = int(input("Digite um numero de 1 a 10: "))

jogador2 = int

chances = 0
while jogador1 != jogador2:
    jogador2 = int(input("Adivinhe o numero digitado pelo jogador 1, o numero é de 1 a 10: "))
    chances +=1 
    if(jogador2 == jogador1):
        print("Voce acertou o numero ")
        print(f"Você acertou em {chances} vezes"  )
        
    

