#função de soma
def soma(a, b):
    return a + b

#função suntração
def subtracao(a, b):
    return a - b

#função e multiplicação
def multiplicacao(a, b):
    return a * b

#função de divisão
def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

#função para o menu
def menu():
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

while True:
    menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        print("Saindo... Obrigado!")
        break
    
    if opcao not in ["1", "2", "3", "4"]:
        print("Opção inválida! Tente novamente.")
        continue
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: por favor, digite números válidos!")
        continue

    if opcao == "1":
        print(f"Resultado: {soma(num1, num2)}")
    elif opcao == "2":
        print(f"Resultado: {subtracao(num1, num2)}")
    elif opcao == "3":
        print(f"Resultado: {multiplicacao(num1, num2)}")
    elif opcao == "4":
        print(f"Resultado: {divisao(num1, num2)}")
