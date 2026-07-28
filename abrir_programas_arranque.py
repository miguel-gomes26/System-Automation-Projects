# Bibliotecas usadas
import webbrowser
import time
import sys
from pathlib import Path

# Define a função principal que abre os sites definidos 
def abrir_sites():
    # Armazena os links do Gemini e do YouTube em variáveis de texto 
    gemini = "https://gemini.google.com/u/6/app?hl=pt-PT&pageId=none"
    youtube= "https://www.youtube.com/?form=MT00MG"

    # Abre o linke do Gemini no navegador
    webbrowser.open(gemini)
    # Faz uma pausa de 3 segundos
    time.sleep(3)
    # Abre o link do YouTube no navegador 
    webbrowser.open(youtube)
    # Faz uma pausa de 3 segundos 
    time.sleep(3)

# Garante que o bloco abaixo só execute se o script for executado diretamente
if __name__ == "__main__":
    print("="*40)
    print("="*40)

    # Pergunta ao utilizador se ele deseja abrir os sites e converte a resposta para letras minúsculas
    resposta = input("ABRIR GEMINI E YOUTUBE? s/n: ").lower()

    # Se a resposta seja 'S' de SIM
    if resposta == 's':
        # Chama a função criada no inicio
        abrir_sites()

        # Encerra a execução do programa com sucess
        sys.exit(0)

    # Se a resposta for 'N' de NÃO
    else: 
        # Encerra a execução do programa com sucesso
        sys.exit(0)