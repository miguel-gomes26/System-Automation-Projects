# Bibliotecas usadas
import os
from send2trash import send2trash
import time

# Definição da função que limpa as pastas 
def limpar_pasta(caminho_pasta):
    # Corrige a formatação das barras invertidas do Windows para barras comuns 
    caminho_pasta = caminho_pasta.replace('\\', '/')

    # Verifica se a pasta indicada realmente existe no computador
    if not os.path.exists(caminho_pasta):
        print("Verficando a pasta...")
        # Delay interativo de 4 segundos
        time.sleep(4)
        print(f"Erro: A pasta {caminho_pasta} não foi encontrada...")
        # Interrompe a execução da função
        return 
    # Obtém uma lista com tudo o que está dentro da pasta
    conteudo = os.listdir(caminho_pasta)

    # Filtra a lista para guardar apenas o que for realmente um ficheiro
    ficheiros = [f for f in conteudo if os.path.isfile(os.path.join(caminho_pasta, f))]

    # Se a lista de ficheiros estiver vazia, avisa o utilizador e encerra a função
    if not ficheiros:
        print(f"A pasta {caminho_pasta} já está limpa")
        return
    
    # Especifica quantos ficheiros existem dentro da pasta
    print(f"\nEncontrei {len(ficheiros)} ficheiro(s) para limpar ")
    # Delay interativo de 1 segundo 
    time.sleep(1)

    # Pergunta ao utiliador se tem a certeza de que quer enviar os ficheiros para a lixeira
    confirmacao = input(f"\nDeseja enviar {len(ficheiros)} ficheiro(s) para a lixeira ? s/n: ").lower()
    # Se a resposta for 's' (SIM)
    if confirmacao == 's':
        # Percorre a lista de ficheiros e trata um por um 
        for ficheiro in ficheiros:
            # Cria o caminho completo do ficheiro 
            caminho_completo = os.path.join(caminho_pasta, ficheiro)
            try:
                # Envia os ficheiros de forma segura para a lixeira do Sistema Operativo 
                send2trash(caminho_completo)
                # Imprime que os ficheiros já foram enviados
                print(f"{ficheiro} enviado para a lixeira")
            except Exception as e:
                # Se o ficheiro estiver aberto em outro programa, captura o erro e avisa
                print(f"Erro: {e} | Não foi possivel apagar o ficheiro - {ficheiro}")
            print("Limpeza concluída!")
        # Se a resposta for 'n' (NÃO)
    else: 
        print("Operação cancelada pelo utilizador|")
# Garante que o bloco abaixo só execute se o script for executado diretamente          
if __name__ == "__main__":
    print("=" *40)
    print("=== LIMPEZA DE FICHEIROS ===")
    print("=" *40)
    
    # Pede ao utilizador que identifique a pasta que deseja limpar
    pasta_alvo = input("\nQual a pasta que deseja limpar ?")

    # Executa a função passando a pasta que foi informada
    limpar_pasta(pasta_alvo)