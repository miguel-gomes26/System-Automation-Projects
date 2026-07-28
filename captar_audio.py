# Bibliotecas usadas 
import sounddevice as sd
import numpy as np 
import wave 
import sys
import time
import keyboard

# Definição da função que captura a tecla 
def capturar_tecla(arquivo_saida: str = "captura.wav",
                taxa: int = 16000, canais: int = 1):
    
    
    # Imprime a instrução inicial e bloqueia o código até que a tecla 'n' seja pressionada
    print("PRESSIONE A TECLA 'N' PARA GRAVAR")
    keyboard.wait('n')

    print("GRAVANDO... (LARGUE A TECLA 'N' PARA TERMINAR!)")

    # Regista o momento exato em que a gravação começou
    tempo_inicio = time.time()

    # Cria uma lista vazia para armazenar os blocos de áudio capturados
    audio_frames =  []

    # Define o tamanho de cada bloco de leitura
    tamanho_bloco = int(taxa * 0.1)

    try:
         # Abre o fluxo de entrada do microfone com as configurações de taxa, canais e formato de 16 bits
         with sd.InputStream(samplerate=taxa, channels=canais, dtype='int16') as stream:
            # Mantém a gravação ativa enquanto a tecla 'n' continuar pressionada
            while keyboard.is_pressed('n'):
                # Lê um bloco de dados de áudio do microfone 
                dados_bloco, _ = stream.read(tamanho_bloco)
                # Adiciona o bloco de áudio capturado à nossa lista 
                audio_frames.append(dados_bloco)
                # Delay interativo de micro segundos (0.05)
                time.sleep(0.05)
    except Exception as e:
        # Se houver falha ao aceder ao microfone, imprime o erro e fecha o script 
        sys.exit(f"\nERRO NA CAPTURA... {e}")
    # Calcula o tempo total da gravação subtraindo o tempo atual pelo tempo inicio
    tempo_total = time.time() - tempo_inicio

    # Verifica se nenhum bloco de áudio foi gravado
    if len(audio_frames) == 0:
        print("NENHUMA AUDIO CAPTADO TENTA MANTER A TECLA PRESSIONADA MAIS TEMPO...")
        
    try:
        # Junta todos os pequenos blocos de áudio da lista num único array do NumPy
        audio = np.concatenate(audio_frames, axis=0)
        with wave.open(arquivo_saida, 'wb') as wf:
            # Define o número de canais - 1 para Mono - 2 para Estéreo
            wf.setnchannels(canais)
            # Define a largura da amostra - 2 bytes = 16 bits
            wf.setsampwidth(2)
            # Define a taxa de amostragem - 16000Hz
            wf.setframerate(taxa)
            # Converte o array do NumPy em bytes puros e grava no ficheiro
            wf.writeframes(audio.tobytes())
            print(f"ÁUDIO SALVO EM {arquivo_saida}...")
    except Exception as e:
        raise RuntimeError(f"ERRO {e} - AO SALVAR AQUIVO WAV...")

# Garante que o bloco abaixo só execute se o script for rodado diretamente
if __name__ == "__main__":
    # Inicia a função definindo o nome do ficheiro final - 'texte.wav'
    capturar_tecla("teste.wav")

            
