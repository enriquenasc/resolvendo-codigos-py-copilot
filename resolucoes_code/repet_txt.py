# Agora vamos solicitar uma string e um número inteiro como entrada. Depois teremos que retornar a string repetida o número de vezes informado.

# Solicitar uma string e um número inteiro como entrada
texto = input("Digite alguma palavras: ")
numero = int(input("Digite a quantidade de vezes que quer repetir: "))

# Retornar a string repetida o número de vezes informado
resultado = (texto + ' ') * numero
print("Resultado:", resultado)
