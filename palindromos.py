#Vamos testar se uma palavra é um palíndromo?! Uma dica é: Utilize conceitos de manipulação de strings para inverter a palavra e comparar com a original.

# Solicita ao usuário para inserir a palavra
palavra = input("Digite uma palavra para verificar se é um palíndromo: ")

# Converte a palavra para minúsculas para tornar a comparação não sensível a maiúsculas e minúsculas
palavra = palavra.lower()

# Inverte a palavra
palavra_invertida = palavra[::-1]

# Verifica se a palavra original é igual à palavra invertida
if palavra == palavra_invertida:
    print("A palavra é um palíndromo!")
else:
    print("A palavra não é um palíndromo.")



