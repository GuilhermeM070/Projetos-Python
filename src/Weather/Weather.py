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

