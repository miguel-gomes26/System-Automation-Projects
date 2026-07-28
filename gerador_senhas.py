# Bibliotecas usadas
import random
import string 
import sys
import time

# Exibe o título
print("=== Gerador de SENHAS ===")

# Declara as variáveis da quantidade padrão e máxima
quantidade_p = 1
quantidade_m = 100

# Loop infinito para obter uma quantidade válida de senhas de utilizadores
while True:
    try:
        # Pede ao utilizador a quantidade de senhas que deseja gerar
        senha = input(f"Quantas senhas deseja gerar [1-{quantidade_m}]")
        # Se o utilizador apenas pressionar 'Enter' a quantidade será a padrão 
        if not senha:
            quantidade = quantidade_p
            print(f"Gerando {quantidade} senha.")
            break
        # Converte a entrada para um número inteiro
        quantidade = int(senha)
        # Verifica se a quantidade está dentro do limite 
        if 1 <= quantidade <= quantidade_m:
            break
        else:
            print(f"Erro: A quantidade deve estar entre 1 e {quantidade_m}")
            
    except ValueError:
        # Captura o erro caso o utilizador digite letras ou simbolos
        print("Erro: Por favor, digite um número inteiro válido.")
    except (EOFError, KeyboardInterrupt):
        # Captura atalhos de interrupção e encerra o programa# Captura atalhos de interrupção e encerra o programa
        print("Operação cancelada pelo utilizador.")
        sys.exit(0)
# Define as variáveis de configuração do comprimento da senha
comprimento_p = 16
comprimento_min = 8
comprimento_max = 64
# Loop infinito para obter um comprimento de senha válido 
while True:
    try:
        # Pede ao utilizador que defina o comprimento da senha
        ent_comprimento = input(f"Digite o comprimento de cada senha [{comprimento_min}-{comprimento_max}]")
        # Se a entrada for vazia, assume o comportamento padrão
        if not ent_comprimento:
            print(f"Usando comprimento padrão: {comprimento_p}.")
            break
        comprimento = int(ent_comprimento)
        # Verifica se o comprimento está dentro dos limites 
        if comprimento_min <= comprimento <= comprimento_max:
            break
        else:
            print(f"Erro: O comprimento deve estar entre {comprimento_min} e {comprimento_max}.")

    except ValueError:
         # Captura o erro caso o utilizador digite letras ou simbolos
        print("Erro: Por favor, digite um número inteiro válido.")
    except (EOFError, KeyboardInterrupt):
        # Captura atalhos de interrupção e encerra o programa
        print("Operação cancelada pelo utilizador.")
        sys.exit(0)     
# Loop infinito para selecionar quais tipos de caracteres farão parte da senha
while True:
    try:
        # As perguntas comparam a resposta com 'n'. Se for diferente de 'n', assume True (SIM)
        minusculas = input("Incluir letras minúsculas (a-z)? (s/n, padrão: s): ").lower() != 'n'
        maiusculas = input("Incluir letras maiúsculas (A-Z)? (s/n, padrão: s): ").lower() != 'n'
        digitos = input("Incluir digitos (0-9)? (s/n, padrão: s): ").lower() != 'n'
        # Filtra os simbolos removendo aspas duplas, aspas simples e crase para evitar problemas de formatação
        simbolos = string.punctuation.replace('"', '').replace("\\'", '').replace('`', '')
        simbolos_uso = input(f"Incluir símbolos ({simbolos})? (s/n, padrão: s): ").lower() != 'n'
        # Cria uma string vazia para juntar todos os grupos de caracteres escolhidos 
        caracteres_disponiveis = ""
        if minusculas:
            caracteres_disponiveis += string.ascii_lowercase
        if maiusculas:
            caracteres_disponiveis += string.ascii_uppercase
        if digitos:
            caracteres_disponiveis += string.digits
        if simbolos_uso:
            caracteres_disponiveis += simbolos
        # Se pelo menos um tipo de caracteren for escolhido, sai do loop
        if caracteres_disponiveis:
            break
        else:
            print("Erro: Deve escolher pelo menos um tipo de caractere para a senha ser forte!")


    except (EOFError, KeyboardInterrupt):
        # Captura atalhos de interrupção e encerra o programa
        print("Operação cancelada pelo utilizador!")
        sys.exit(0)
# Abertura do ficheiro de forma segura para guardar as senhas
f = open("guardar_senhas.txt", "w")
with open(r"guardar_senhas.txt", "w") as f:
    print("Gerando a senha...")
    time.sleep(3)
    # Loop para gerar a quantidade de senhas solicitadas pelo utilizador
    for i in range(quantidade):
        # Escolhe aleatoriamente os caracteres do pool disponivel e junta-os numa única string
        senha = ''.join(random.choices(caracteres_disponiveis, k=comprimento))
        # Exibe a senha na tela com formatação dos dois digitos no índice
        print(f"SENHA {i+1:02d}: {senha}")
        # Escreve a senha formatada dentro do ficheiro de texto
        f.write(f"SENHA {i+1:02d}: {senha}\n")
# Abre novamente o ficheiro mas em modo leitura
with open(r"guardar_senhas.txt") as f:
    print(f.read())










