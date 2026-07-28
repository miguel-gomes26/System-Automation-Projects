# Bibliotecas usadas
import time
import requests
import string
import os

# Define a função principal que analisa se o site é seguro     
def link_site():
    #Solicita o link ao utilizador e remove espaços extras
    link = input("Qual o link que deseja analisar?\n").strip()
    #Faz uma pausa de 1 segundo 
    time.sleep(1)
    print("\nVerificando o link...")
    #Faz outra pausa de 1 segundo antes de iniciar a comunicação com a API
    time.sleep(1)

    # Recupera a chave da API do VirusTotal armazenada nas variáveis de ambiente do sistema
    chave = os.getenv("VIRUSTOTAL_API_KEY")

    # Define o endpoint da API do VirusTotal para análise de URLs
    url_api = "https://www.virustotal.com/api/v3/urls"

    # Define o cabeçalho da requisição, passando a chave da API para autenticação
    headers = {
        "x-apikey": chave
    }

    # Define os parâmetros de consulta enviados na URL
    params = {
        "resource": link
    }

    # Define o corpo da requisição contendo a URL que será analisada pela API
    dados = {
        "url": link
    }

    # Envia uma requisição do tipo POST para a API do VirusTotal com os dados e cabeçalhos
    resposta = requests.post(url_api, headers=headers, params=params, data=dados)

    # Descodifica o corpo da resposta HTTP de formato JSON para um dicionário nativo do Python
    resultado = resposta.json()

    # Exibe o resultado bruto retornado pela API na tela
    print("\n ==== RESPOSTA ====")
    print(resultado)

# Garante que a função link_site() só será executada se este arquivo for executado diretamente
if __name__ == "__main__":
    link_site()
    