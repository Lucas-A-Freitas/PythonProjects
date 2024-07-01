# 1- Dar boas vindas ao usuario;
# 2- Perguntar ao usuario se ele quer participar do questionario;
# 3- Se sim, fazer 5 perguntas
# 4- Mostrar ao final quantas perguntas ele acertou

print ("Bem vindo")

participar = input("Você quer participar do questionaio de geografia? ")

pontuacao = 0

if participar.lower() != "sim":
    print("Até a proxima")
    pontuacao += 1
else:
    print("Vamos lá então")

resposta_1 = input("1. Qual é a capital da França? ")
if resposta_1.lower() == "paris":
    print("Correto! :)")
    pontuacao += 1
else:
    print("Errou! :(")

resposta_2 = input("2. Qual continente é conhecido como 'o berço da humanidade'? ")
if resposta_2.lower() == "africa":
    print("Correto! :)")
    pontuacao += 1
else:
    print("Errou! :(")

resposta_3 = input("3. Qual país tem o formato aproximado de uma bota? ")
if resposta_3.lower() == "italia":
    print("Correto! :)")
    pontuacao += 1
else:
    print("Errou! :(")

resposta_4 = input("4. Qual é o deserto mais quente do mundo? ")
if resposta_4.lower() == "saara":
    print("Correto! :)")
    pontuacao += 1
else:
    print("Errou! :(")

resposta_5 = input("5. Qual é a montanha mais alta do mundo? ")
if resposta_5.lower() == "monte evereste":
    print("Correto! :)")
    pontuacao += 1
else:
    print("Errou! :(")

porcentagem = (pontuacao / 5) * 100
print("Você acertou ", pontuacao,"de 5 questões")
print("Isso equivale a", porcentagem,"%")