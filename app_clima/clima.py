import os
import requests
from datetime import datetime
from dotenv import load_dotenv

# Carrega as variáveis salvas no arquivo .env
load_dotenv()

# Busca a chave secreta que você salvou
API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(lat, lon):
    """
    Conecta à API WeatherAPI oficial usando a chave de API do usuário
    """
    # RASTREADOR 1: Verificando se a chave foi lida do arquivo .env
    if not API_KEY:
        print("\n[DIAGNÓSTICO] ❌ Erro: A variável WEATHER_API_KEY não foi encontrada no arquivo .env!")
        return None
    
    # A WeatherAPI aceita o nome da cidade direto no parâmetro 'q'
    url = f"http://api.weatherapi.com/v1/forecast.json?key={API_KEY}&q={lat},{lon}&days=1&aqi=no&lang=pt"

    try:
        response = requests.get(url)
        data = response.json()

        #[RATREADOR 2]
        # Se a API retornar algum erro (como chave inválida), tratamos aqui
        if "error" in data:
            print(f"\n[DIAGNÓSTICO] ❌ A WeatherAPI recusou a requisição. Resposta do servidor: {data['error']['message']}")
            print(f'[DIAGNOSTICO DA API] ❌ Código do erro: {data['error'].get('code')}')
            return None
        
        # Extraindo os dados reais da estrutura da WeatherAPI
        current = data['current']
        # Pegamos os dados do dia de hoje dentro da estrutura de previsão
        forecast_today = data["forecast"]["forecastday"][0]["day"]
        # Verificação exata do período usando a hora atual
        current_time = datetime.now().hour
        is_day = current.get("is_day") # A API retorna 1 para dia e 0 para noite

        if is_day == 0:
            formatted_period = "Noturno"
        else:
            formatted_period = "Matutino" if current_time < 12 else "Vespertino"

        # Vamos extrair apenas as 3 informações que nos interessam:
        info_weather = {
            'temperature': current.get("temp_c"), # Temperatura em Celsius convertida para inteiro
            'condition': current.get("condition", {}).get("text"), # Texto em português ex: "Ensolarado"
            'period': formatted_period, #Agora vai o texto bonito e correto!
            # Novos dados de previsão
            'maximum': round(float(forecast_today.get('maxtemp_c',0))),
            'minimum': round(float(forecast_today.get('mintemp_c',0))),
            'chance_rain': forecast_today.get('daily_chance_of_rain', 0)
        }
        return info_weather
    
    except Exception as e:
        # Caso ocorra erro de conexão
        print(f'[DIAGNOSTICO] Erro inesperado no código: {e}')
        return None
