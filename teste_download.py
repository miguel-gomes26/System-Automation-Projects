# Bibliotecas usadas
import asyncio
from yt_dlp import YoutubeDL

# Dicionário de configuração para o yt_dlp
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'musicas_guardadas/teste_musica',
    
}

# Definição da função que descarrega o video
def download():
    # Inicializador do gerenciador de contexto do YouTubeDL com as configurações definidas acima
    with YoutubeDL(ydl_opts) as ydl:
        # Executa o download da musica "Billie Jean - Michael Jackson"
        ydl.download(["ytsearch1:Billie Jean Michael Jackson"])

# Bloco de execução principal com tratamento de erros
try:
    print("A iniciar download de teste...")
    # Chama a função para iniciar a pesquisar e o download do áudio
    download()
    # Se o download terminar sem falhas, imprime a mensagem de sucesso
    print("Download concluído com sucesso!")
except Exception as e:
    # Caso ocorra algum erro, captura erro e imprime-o no terminal
    print(f"\n❌ ERRO DETETADO:\n{e}")