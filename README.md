## Monitoramento de Preços com Selenium e BeautifulSoup

Este projeto utiliza o Selenium e BeautifulSoup para monitorar os preços de produtos no site das Casas Bahia. O script extrai os dados do produto, como nome, valor e link, e os armazena em um arquivo CSV. Além disso, o script é programado para ser executado automaticamente a cada 30 minuto utilizando o módulo Schedule.

### Tecnologias Utilizadas

- **Selenium**: Utilizado para automatizar a navegação na web.
- **BeautifulSoup**: Utilizado para fazer o parsing do HTML e extrair os dados necessários.
- **Pandas**: Utilizado para manipulação e armazenamento de dados em formato CSV.
- **Schedule**: Utilizado para agendar a execução periódica da coleta de dados.
- **Logging**: Utilizado para registrar logs de execução e erros.

### Configuração do Projeto

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o script:
    ```bash
    python seu_script.py
    ```
