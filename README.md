# Projetos Python - Dio.me

Este repositório contém uma coleção de projetos desenvolvidos durante os cursos e desafios da plataforma **Dio.me**, com foco em aplicações práticas de Python. Os projetos abrangem diferentes áreas da linguagem, incluindo automação, análise de dados, desenvolvimento web e muito mais.

## Estrutura do Repositório

- **projetos/**: Diretório principal contendo os códigos de cada projeto.
  - **sistema_bancario/**: Projeto de simulação de um sistema bancário, permitindo operações como depósitos, saques e transferências.
  - **calculadora/**: Uma calculadora simples com operações matemáticas básicas implementadas em Python.
  - **jogo_adivinhacao/**: Jogo interativo onde o usuário tenta adivinhar um número gerado aleatoriamente pelo sistema.

## Projetos Destacados

### Sistema Bancário
![Sistema Bancário](images/sistema_bancario.png)
Implementação de um sistema bancário que suporta:
- Depósitos e saques.
- Transferências entre contas.
- Consulta de saldo.

### Calculadora
![Calculadora](images/calculadora.png)
Um aplicativo de linha de comando que permite realizar operações matemáticas como:
- Soma
- Subtração
- Multiplicação
- Divisão

### Jogo da Adivinhação
![Jogo da Adivinhação](images/jogo_adivinhacao.png)
Um jogo divertido onde o usuário tenta adivinhar um número entre 1 e 100, com feedback fornecido após cada tentativa.

## Como Usar

1. Clone o repositório:
   ```bash
   git clone https://github.com/GuilhermeM070/Projetos-Python-DIO
   ```

2. Navegue até o diretório do projeto desejado:
   ```bash
   cd Projetos-Python-DIO/projetos/<nome_do_projeto>
   ```

3. Execute o projeto:
   ```bash
   python main.py
   ```

## Requisitos

- Python 3.8 ou superior

# 🌤 Consulta de Previsão do Tempo  

Este script em Python busca a previsão do tempo para qualquer cidade usando a API do OpenWeatherMap.  

## 🚀 Como Usar  

1. **Crie uma conta** no [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).  
2. **Obtenha sua API Key** na aba "API Keys".  
3. **Instale a biblioteca `requests` (se necessário):**  
   ```bash
   pip install requests
Substitua "SUA_CHAVE_AQUI" pela sua API Key no código abaixo.
Execute o script e digite o nome da cidade desejada.
📜 Código Atualizado
python
Copiar
Editar
import requests

API_KEY = "SUA_CHAVE_AQUI"
city = input("Escreva o nome da cidade: ")

url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&lang=pt_br&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperatura = data["main"]["temp"]
    descricao = data["weather"][0]["description"]

    print(f'Clima em {city}:')
    print(f'Temperatura: {temperatura}°C')
    print(f'Descrição: {descricao.capitalize()}')

else:
    print("Cidade não encontrada, cheque o nome e tente novamente.")
🎯 Recursos
Busca a previsão do tempo em qualquer cidade do mundo.
Retorna temperatura e descrição do clima em português.
Usa a API OpenWeatherMap para maior precisão.
🔥 Exemplo de Saída
bash
Copiar
Editar
Escreva o nome da cidade: São Paulo
Clima em São Paulo:
Temperatura: 28°C
Descrição: Céu limpo
⚠️ Observações
Certifique-se de substituir "SUA_CHAVE_AQUI" pela chave da API OpenWeatherMap.
O script retorna temperatura em graus Celsius (units=metric).
📌 Autor: Desenvolvido para facilitar consultas meteorológicas de forma rápida e prática.

nginx
Copiar
Editar

Agora seu projeto está bem documentado e pronto para ser compartilhado!

## Contribuições

Contribuições são bem-vindas! Caso encontre bugs ou tenha ideias de melhorias, abra uma issue ou envie um pull request.

## Licença

Este repositório está licenciado sob a [MIT License](LICENSE).

## Contato

- **Autor**: Guilherme de Matos Costa
- **Email**: guimatos070@gmail.com
- **LinkedIn**: [Perfil do LinkedIn](https://www.linkedin.com/in/guilherme-matos-413400200)

---

Explore os projetos e aproveite para expandir seus conhecimentos em Python!
