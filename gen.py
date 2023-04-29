import itertools

# Leitura do arquivo de entrada
filename = input("Digite o caminho do arquivo de senhas: ")
with open(filename, "r") as f:
    password_list = f.read().splitlines()

# Menu de seleção
min_length = int(input("Digite o tamanho mínimo de senha desejado: "))
max_length = int(input("Digite o tamanho máximo de senha desejado: "))
max_words = int(input("Digite a quantidade máxima de palavras pegas da lista inicial combinadas por linha: "))
output_file = input("Digite o nome do arquivo de saída: ")

# Geração das combinações
with open(output_file, "w") as f:
    for r in range(1, max_words + 1):
        for combination in itertools.product(password_list, repeat=r):
            password = "".join(combination)[:max_length]
            if len(password) >= min_length:
                f.write(password + "\n")

