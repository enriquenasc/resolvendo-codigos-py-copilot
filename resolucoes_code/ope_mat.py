# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicitar dois números ao usuário
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Realizar uma operação simples (soma) entre eles
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == '+':
    print (num1 + num2)
elif operacao == '-':
    print (abs(num1 - num2)) # Usando abs para garantir que o resultado seja positivo
elif operacao == '*':
    print (num1 * num2)
elif operacao == '/':
    if num2 != 0:
        print (num1 / num2)
    else:
        resultado = "Erro: Divisão por zero não é permitida."