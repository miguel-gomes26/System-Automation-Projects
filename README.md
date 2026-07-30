# Automação, Sistemas e Segurança 

Este repositório reúne um conjunto de ferramentas e utilitários desenvolvidos de forma autónoma em **Python**. O objetivo principal destes projetos é aplicar na prática, demonstrando aptidão em automação de infraestruturas, administração de sistemas operativos e fundamentos de cibersegurança.

---

## Portfólio de Projetos e Módulos

### Cibersegurança e Proteção de Dados
* **`analisar_sites.py`**: Ferramenta integrada de forma segura (via `os.getenv`) com a **API do VirusTotal**. Permite submeter URLs para análise de reputação e deteção de ameaças em tempo real com tratamento de respostas JSON.
* **`testador_senhas.py`**: Script focado em segurança de credenciais. Utiliza a fórmula matemática de **entropia de Shannon** ($E = L \times \log_2(R)$) para auditar a robustez e a complexidade de palavras-passe em bits.
* **`gerador_senhas.py`**: Utilitário para geração de credenciais seguras com base em conjuntos de caracteres e persistência local através da gravação automatizada num ficheiro estruturado `.txt`.

### Automação de Sistemas Operativos (Windows)
* **`limpar_ficheiros_temp.py`**: Script de manutenção preventiva que interage com as **variáveis de ambiente do Windows** (`os.environ.get('TEMP')`), isola ficheiros residuais de extensão `.tmp` e utiliza a biblioteca `send2trash` para limpeza segura do sistema de ficheiros.
* **`limpar_ficheiros.py`**: Ferramenta interativa de limpeza que valida caminhos absolutos no sistema, lista diretórios e move ficheiros em lote para a reciclagem de forma controlada.
* **`abrir_calculadora.py` & `abrir_programas_arranque.py`**: Demonstração avançada de gestão de subprocessos e manipulação de streams do sistema (`subprocess.DEVNULL`), permitindo a inicialização limpa de binários locais e automação de fluxos no navegador.

### Infraestrutura e Redes de Computadores
* **`monitor_redes.py`**: Monitor de conectividade em tempo real. Dispara pacotes cíclicos de diagnóstico **ICMP (Ping)** para múltiplos hosts e avalia o código de retorno do sistema (*Return Code*) para validar a integridade de endereços IPv4 locais e externos.

### Utilitários de Média e Captura
* **`resumo_IA.py`**: Extração automatizada de texto em formatos comerciais (`.pdf`, `.docx`, `.pptx`) combinada com o consumo da API da **Groq** para submissão de prompts ao modelo open-source **Llama**, gerando resumos analíticos automáticos.
* **`captar_audio.py`**: Interpolação de inputs de hardware através da biblioteca `sounddevice` e `keyboard` para gravação de fluxos de áudio comprimidos em formato WAVE estruturado.
* **`baixar_videos_youtube.py` & `teste_download.py`**: Scripts de automação para download persistente de conteúdos através do ecossistema `yt-dlp`.

---

## Tecnologias, Bibliotecas e Conceitos Aplicados
* **Linguagens principais**: Python 3(Lógica estruturada).
* **Consumo de APIs**: REST API (VirusTotal), LLM API (Groq Cloud) utilizando variáveis de ambiente seguras.
* **Sistemas e Redes**: Protocolo ICMP, Gestão de subprocessos, Variáveis de Ambiente.
