import random

print("Vamos jogar um jogo?:D")

numero = input("Escolha um número: ")

if numero.isdigit():
    numero = int(numero)

    if numero <= 0:
        print("Por favor escolha um número maior que 0")
        quit()
else:
    print("Por favor digite um número na próxima vez")
    quit()

numero_aleatorio = random.randint(0, numero)

tentativas = 0

while True:
    tentativas += 1
    escolha_do_jogador = input("Adivinhe: ")
    if escolha_do_jogador.isdigit():
        escolha_do_jogador = int(escolha_do_jogador)
    else:
        print("Por favor digite um número na próxima vez")
        continue

    if escolha_do_jogador == numero_aleatorio:
        print("Você acertou!")
        break
    else:
        if escolha_do_jogador < numero_aleatorio:
            print("Chutou baixo")
        else:
            print("Chutou alto")

print("Você acertou com", tentativas, "tentativas")