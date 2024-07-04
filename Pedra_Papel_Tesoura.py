#usuario vai esolher o que fazer ( escolher entre pedra, papel ou tesoura ou sair do programa)
#conferir se usuario escolheu entre as opções
#conferir quem ganhou
#marcar os pontos entre usuario e a maquina
import random

usuario_ganhou = 0
maquina_ganhou = 0

opcoes = ["pedra", "papel", "tesoura"]



while True:
    escolha_usuario = input("Escolha entre Pedra/Papel/Tesoura ou digite 'Sair' para encerrar o programa: ").lower()

    if escolha_usuario == "sair":
        break

    if escolha_usuario not in opcoes:
        continue

    numero_aleatorio = random.randint(0,2)
    escolha_maquina = opcoes[numero_aleatorio]
    
    print(f"Você escolheu {escolha_usuario} e a maquina escolheu {escolha_maquina}")

    if escolha_maquina == escolha_usuario:
        print("empate!")

    elif escolha_usuario == "pedra" and escolha_maquina == "tesoura" or \
    escolha_usuario == "papel" and escolha_maquina == "pedra" or \
    escolha_usuario == "tesoura" and escolha_maquina == "papel":
        print("Você ganhou!")
        usuario_ganhou += 1
    else:
        print("Maquina ganhou!")
        maquina_ganhou += 1

    print("\n-------------")

print("Jogador ganhou: ", usuario_ganhou, "vezes.")
print("Maquina ganhou: ", maquina_ganhou, "vezes.")
print("Obrigado, volte sempre!")