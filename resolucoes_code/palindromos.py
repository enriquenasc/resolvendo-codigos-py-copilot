## 6 - Verificando Palíndromos 🔄
# Vamos testar se uma palavra é um palíndromo?!

def palindromo(palavra):
    palavra = palavra.lower().replace(" ", "")
    return palavra == palavra[::-1]

# Testando a função
palavra_teste = input("Digite uma palavra para verificar se é um palíndromo: ")
if palindromo(palavra_teste):
    print(f"'{palavra_teste}' é um palíndromo!")
else:
    print(f"'{palavra_teste}' não é um palíndromo.")

