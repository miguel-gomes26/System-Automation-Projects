# Bibliotecas usadas
import math
import time

# Pede ao utilizador que "Digite a senha para testar..."
senha = input("Digite a senha para testar a entropia: ")

# Se a senha for menor do que 8
if len(senha) < 8:
    print("Verificando a senha...")
    # Faz uma pausa de 2 segundos
    time.sleep(2)
    print("Senha em análise...")
    time.sleep(4)

    # Imprime que a senha é curta
    print(f"{senha} é uma senha curta!")

# Armazena o comprimento da senha na variável 'L'
L = len(senha)
# Inicializa a variável R, que representará o tamaho 
R = 0
# Se a senha contiver pelo menos uma letra minúscula, adiciona 26 possibilidades
if any(c.islower() for c in senha):
    R+= 26
# Se a senha contiver pelo menos uma letra Maiúscula, adciciona 26 possibilidades
if any(c.isupper() for c in senha):
    R+= 26
# Se a senha contiver pelo menos um digito, adiciona 10 possibilidades
if any(c.isdigit() for c in senha):
    R+= 10
# Calcula a entropia da senha usando a fórmula clássica - E = L * log2(R)
entropia = L * math.log2(R)
# Exibe o valor da entropia formatado com 2 casas decimais 
print(f"A entropia da senha é - {entropia:.2f} bits")
# Se a entropia for menor que 35, a senha é fraca
if entropia < 35:
    print("Senha fraca, facilmente quebrada por hackers!")
# Se a entropia for maior ou igual a 35 mas menor ou igual a 59, a senha é razoável
elif entropia >= 35 <= 59:
    print("Senha razoável, pode melhorar!")
# Se a entropia for maior ou igual a 60, a senha é segura
elif entropia >= 60:
    print("Senha segura!")