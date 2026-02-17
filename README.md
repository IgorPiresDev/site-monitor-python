# 🚀 Monitor de Disponibilidade (DevOps Study)

Este projeto foi desenvolvido como parte dos meus estudos em **Python** e **Infraestrutura (DevOps)**. O objetivo é monitorar o status de disponibilidade de diversos sites e registrar os dados de forma estruturada para futuras análises.

## 🛠️ O que o script faz:
- Realiza requisições HTTP para uma lista de URLs pré-definidas.
- Simula um navegador real usando `User-Agent` para evitar bloqueios simples.
- **Logs Estruturados**: Salva o timestamp, a URL e o status code (ex: 200, 403) em um arquivo `logs.json`.
- Roda em um loop contínuo com intervalo de 10 segundos entre as verificações.

## 🧰 Tecnologias Utilizadas:
- **Python 3**: Linguagem principal.
- **Requests**: Biblioteca para chamadas HTTP.
- **JSON**: Formato de saída para persistência de dados.
- **Git/GitHub**: Controle de versão e gerenciamento de branches.

## 🚀 Como executar:
1. Clone o repositório.
2. Certifique-se de ter o Python instalado.
3. Instale a biblioteca de dependência:
   ```bash
   pip install requestspy-security-logs
