# Bibliotecas usadas
import subprocess
import time
from pathlib import Path

# Define o programa
programa = "calc.exe"

# Definição da função que abre a calculadora
def abrir_calculadora(programa):
    print("Abrindo o programa...")
    # Delay interativo de 4 segundos
    time.sleep(4)

    # Cria um subprocesso no Sistema Operativo para executar o binário indicado
    resultado = subprocess.run(
        [programa],
        # Redireciona a saída padrão para o "vazio"
        stdout=subprocess.DEVNULL,
        # Redireciona a saída de erros para o "vazio"
        stderr=subprocess.DEVNULL
    )

# Garante que o bloco abaixo só execute se o script for executado diretamente 
if __name__ == "__main__":
    print("="*40)
    print(" ------ CALCULADORA ABRINDO ------ ")
    print("="*40)

    # Executa a função que abre a calculadora
    abrir_calculadora(programa)