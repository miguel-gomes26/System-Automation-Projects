# Bibliotecas usadas
import os
from pathlib import Path
from send2trash import send2trash
import time

# Definição da função que limpa os ficheiros temporários
def limpar_pasta():
    # Recupera a variável de ambiente 'TEMP' do Windows 
    caminho_temp = os.environ.get('TEMP')
    # Instancia um objeto Path da biblioteca pathlib e valida o caminho absoluto no sistema de ficheiros
    pasta = Path(caminho_temp).resolve()

    # Verifica se o caminho obtido existe e se é uma pasta
    if not pasta.exists() or not pasta.is_dir():
        print(f"Erro: A pasta {pasta} não foi encontrada...")
        # Interrompe a função caso a pasta não exista
        return 

    # List comprehension que percorre a pasta e filtra apenas o que for ficheiro e tiver a extensão '.tmp'
    ficheiros = [f for f in pasta.iterdir() if f.is_file() and f.suffix.lower() == '.tmp']

    # Se a lista de ficheiros estiver vazia, avisao o utilizador e encerra a função
    if not ficheiros:
        print(f"A pasta {pasta} já está limpa de ficheiro .tmp")
        return

    # Imprime no terminal a quantidade de ficheiros temporários encontrados
    print(f"\nEncontrei {len(ficheiros)} ficheiro(s) .tmp para limpar ")
    # Delay interativo de 1 segundo
    time.sleep(1)
    # Percorre a lista de ficheiros encontrados para mover um por um para a lixeira
    for ficheiro in ficheiros:
        try:
            # Envia o ficheiro para a lixeira
            send2trash(str(ficheiro))
            # Imprime apenas o nome do ficheiro que foi removido
            print(f"\n{ficheiro.name} enviado para a lixeira")
        except Exception as e:
            # Se o ficheiro estiver em uso pelo Windows ou outro programa, captura o erro e avisa
            print(f"Erro: {e} | Não foi possivel apagar o ficheiro - {ficheiro.name}")
    print("\nLimpeza concluída!")
# Garante que o bloco abaixo só execute se o script for executado diretamente     
if __name__ == "__main__":
    print("=" *40)
    print("=== LIMPEZA DE FICHEIROS ===")
    print("=" *40)

    # Chama a função automática de limpeza
    limpar_pasta()