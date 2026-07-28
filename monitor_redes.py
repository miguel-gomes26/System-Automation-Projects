# Bibliotecas usadas
import subprocess
import time

# Definição da função de varrimento de rede (recebe uma string com o IP)
def testar_conexao(ip_alvo):
    # Feedback visual para o utilizador no terminal
    print(f"Testando conexão com {ip_alvo}...")
    # Delay interativo para simular processamento
    time.sleep(6)

    # Executa o comando de ping no sistema operativo em segundo plano
    resultado = subprocess.run(
        ["ping", "-n", "1", "-w", "1000", ip_alvo],
        # Redireciona a saída padrão para o "vazio"
        stdout=subprocess.DEVNULL,
        # Redireciona a saída de erros para o "vazio"
        stderr=subprocess.DEVNULL
    )
    # Avaliação do Return Code da execução do comando
    # 0 = Sucesso (Host respondeu), Qualquer outro número = Falha (Timeout/Inacessível)
    if resultado.returncode == 0:
        print("Verificando o IP...")
        time.sleep(4)
        print(f"\n{ip_alvo} encontra-se ONLINE\n")
        return True
    else:
        # Se o código de retorno não for 0, o dispositivo falho no teste
        print(f"Erro: {ip_alvo} encontra-se OFFLINE...\n")
        return False

# Garante que o bloco abaixo só execute se o script for rodado diretamente
if __name__ == "__main__":
    print("="*40)
    print(" ===== MONITOR DE REDE EM TEMPO REAL ==== ")
    print("="*40)

    # Lista contendo as Strings dos endereços IPv4 (Hosts Alvos do ICMP Ping)
    dispostivos = ["8.8.8.8", "192.168.1.1"]

    # Bloco Try-Except para tratamento de interrupções de hardware/sistema
    try:
        # Loop infinito para manter o monitoramento rodando sem parar
        while True:
            # Percorre a lista de IP's e testa um de cada vez
            for ip in dispostivos:
                testar_conexao(ip)

            print("Aguardando o próximo teste...")
            # Intervalo de amostragem entre ciclos de varrimento
            time.sleep(6)
            print("-"*40)

    # Captura a interrupção especifica do utilizador
    except KeyboardInterrupt:
        print("Monitorização cancelada pelo utilizador...")
    

