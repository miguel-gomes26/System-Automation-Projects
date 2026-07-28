# Biblioteca usada
import yt_dlp

# Definição da função que descarrega o video
def video_descarregador(url):
    try:
        # Ciclo de execução contínua para persistência do processo de download
        while True:
            # Dicionário de configuração para o yt_dlp
            ydl_opts = {
                'format': 'best',
                'outtmpl': '%(title)s.%(ext)s',
            }
            # Inicializa o gerenciador de contexto do YouTubeDL com as configurações definidas acima
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                # Executa o download propriamente dito, passando a URL dentro de uma lista
                ydl.download([url])
        
    except KeyboardInterrupt:
        # Captura a interrupção especifica do utilizador
        print("\nDOWNLOAD INTERROMPIDO")
# Pede ao utilizador para colar o link do vídeo desejado 
url = input("ESCREVA A URL DO VIDEO QUE DESEJA FAZER DOWNLOAD...")

# Chama a função principal passando a URL informada pelo utilizador 
video_descarregador(url)