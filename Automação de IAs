import openai
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import time

# Configurar a chave da API do OpenAI (substitua pela sua)
openai.api_key = 'sua_api_key_aqui'

# Função para gerar respostas baseadas em IA
def gerar_resposta(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Função para agendar compromissos
def agendar_compromisso(titulo, data, hora):
    try:
        compromisso = {
            'titulo': titulo,
            'data': data,
            'hora': hora
        }
        print(f"Compromisso '{titulo}' agendado para {data} às {hora}.")
        return compromisso
    except Exception as e:
        print(f"Erro ao agendar o compromisso: {e}")

# Função para enviar um email automatizado
def enviar_email(destinatario, assunto, mensagem):
    try:
        remetente = 'seuemail@example.com'
        senha = 'suasenha'  # Use uma senha de app ou autenticação forte

        msg = MIMEMultipart()
        msg['From'] = remetente
        msg['To'] = destinatario
        msg['Subject'] = assunto
        msg.attach(MIMEText(mensagem, 'plain'))

        # Estabelecer conexão com o servidor SMTP
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(remetente, senha)

        # Enviar email
        texto = msg.as_string()
        server.sendmail(remetente, destinatario, texto)
        server.quit()
        print(f"Email enviado para {destinatario} com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar email: {e}")

# Função para simular previsão do tempo (pode integrar com APIs reais)
def obter_previsao_tempo(cidade):
    previsao = f"A previsão do tempo para {cidade} é: Sol com algumas nuvens, temperatura de 25°C."
    print(previsao)
    return previsao

# Função para realizar cálculos básicos
def calculadora(expressao):
    try:
        resultado = eval(expressao)
        print(f"Resultado de {expressao}: {resultado}")
        return resultado
    except Exception as e:
        print(f"Erro no cálculo: {e}")

# Função principal do assistente
def assistente_virtual():
    print("Assistente Virtual Ativado! (Digite 'sair' para encerrar)")
    while True:
        print("\nOpções: 1. Chat IA 2. Agendar Compromisso 3. Enviar Email 4. Previsão do Tempo 5. Calculadora")
        comando = input("\nDigite uma opção ou uma tarefa específica: ").lower()

        if comando == 'sair':
            print("Assistente: Até logo!")
            break

        # Opção 1: Chat com IA
        elif comando == '1':
            pergunta = input("Você: ")
            resposta = gerar_resposta(pergunta)
            print(f"Assistente: {resposta}")

        # Opção 2: Agendar Compromisso
        elif comando == '2':
            titulo = input("Título do compromisso: ")
            data = input("Data do compromisso (formato AAAA-MM-DD): ")
            hora = input("Hora do compromisso (formato HH:MM): ")
            agendar_compromisso(titulo, data, hora)

        # Opção 3: Enviar Email
        elif comando == '3':
            destinatario = input("Digite o email do destinatário: ")
            assunto = input("Assunto do email: ")
            mensagem = input("Digite sua mensagem: ")
            enviar_email(destinatario, assunto, mensagem)

        # Opção 4: Obter Previsão do Tempo
        elif comando == '4':
            cidade = input("Digite o nome da cidade: ")
            obter_previsao_tempo(cidade)

        # Opção 5: Calculadora
        elif comando == '5':
            expressao = input("Digite a expressão matemática: ")
            calculadora(expressao)

        else:
            print("Comando não reconhecido. Tente novamente.")

if __name__ == "__main__":
    assistente_virtual()
