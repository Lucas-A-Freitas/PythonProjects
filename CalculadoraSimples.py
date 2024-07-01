print("Bem-vindo à Calculadora")

numero_1 = float(input ("Informe o primeiro número: "))

numero_2 = float(input( "Informe o segundo número: "))

operacao = input("Qual operação você gostaria de fazer? [+, -, /, *] ")

if operacao == "+":
    resultado = numero_1 + numero_2
    print(resultado)
elif operacao == "-":
    resultado = numero_1 - numero_2
    print(resultado)
elif operacao == "/":
    resultado = numero_1 / numero_2
    print(resultado)
elif operacao == "*":
    resultado = numero_1 * numero_2
    print(resultado)
else:
    print("Operação invalida")
