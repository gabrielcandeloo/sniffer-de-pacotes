# 🕵️‍♂️ Sniffer de Pacotes de Rede (Network Packet Sniffer)

## 📖 Sobre o Projeto
Este projeto é um analisador de tráfego de rede (sniffer) desenvolvido em Python. A ferramenta coloca a placa de rede em modo de escuta para capturar, filtrar e traduzir pacotes de dados em tempo real. O objetivo é demonstrar como o tráfego flui pela rede e como ferramentas de monitoramento de segurança operam nos bastidores.

## 🚀 Funcionalidades
* **Captura Estratégica:** Intercepta pacotes de rede ao vivo na camada de enlace e rede.
* **Filtragem de Hardware (BPF):** Utiliza *Berkeley Packet Filters* para isolar cirurgicamente protocolos específicos (como TCP), ignorando o "ruído de fundo" da rede (como ARP e IGMP).
* **Bypass de Limitação do Windows:** Implementa vinculação direta de interface (`dev_from_index`) para garantir que o filtro de hardware funcione perfeitamente em ambientes Windows com Npcap, resolvendo bugs comuns de escuta global.
* **Tradução de Dados Brutos:** Converte zeros e uns em resumos legíveis para análise humana de *headers* (cabeçalhos) e portas.

## 🛠 Tecnologias e Bibliotecas
* **Linguagem:** Python 3
* **Biblioteca Principal:** `scapy` (Manipulação e captura avançada de pacotes)
* **Driver de Rede:** `Npcap` (Para suporte à captura em modo promíscuo no Windows)

## 🧠 Conceitos de Cibersegurança Aplicados
* **Modo Promíscuo:** Manipulação da placa de rede para ler pacotes que não são destinados diretamente ao host local.
* **Análise de Tráfego (Traffic Analysis):** Inspeção de protocolos nas camadas 2 (Ethernet), 3 (IP) e 4 (TCP/UDP) do Modelo OSI.
* **Troubleshooting de Infraestrutura:** Resolução de conflitos entre bibliotecas Python de alto nível e drivers de sistema operacional de baixo nível.

## 💻 Como Executar

1. Clone o repositório.
2. Certifique-se de ter o Python 3 e o driver Npcap instalados (necessário para usuários Windows).
3. Instale as dependências:
   `pip install scapy`
4. Descubra o índice da sua placa de rede ativa (usando `scapy.all.show_interfaces()`) e ajuste no código.
5. Execute o script com privilégios de Administrador/Root:
   `python sniffer.py`

---
⚠️ **Aviso Ético:** Esta ferramenta foi desenvolvida com propósitos educacionais para o estudo de Segurança da Informação. Interceptar tráfego em redes corporativas, públicas ou de terceiros sem a devida autorização explícita constitui violação de privacidade e crime cibernético. Utilize esta ferramenta apenas em sua rede local sob seu controle.
