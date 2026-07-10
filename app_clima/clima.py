import requests
from datetime import datetime

def get_weather(city_name):
    """
    Conecta à API HG Weather para buscar as condições climáticas da cidade.
    Retorna um dicionário com os dados ou None se houver falha.
    """
    # Criamos o link da API passando o nome da cidade como parâmetro de busca
    url = f"https://api.hgbrasil.com/weather?city_name={city_name}%2CSP&key=suachave"

    try:
        response = requests.get(url)
        data = response_json = response.json()

        # A HG Weather retorna os dados principais dentro da chave 'results'
        if 'results' in data:
            details = data['results']

            # ----CORREÇÃO DO PERÍODO----
            # vamos olhar a hora atual do computador para definir se é Matutino ou Vespertino
            current_time = datetime.now().hour
            original_period = details.get('currently') # "dia" ou "noite"

            if original_period == "noite":
                formatted_period = 'Noturno'
            else:
                if current_time < 12:
                    formatted_period = 'Matutino'
                else:
                    formatted_period = 'Verpertino'

            # Vamos extrair apenas as 3 informações que nos interessam:
            info_weather = {
                'temperature': details.get('temp'),
                'condition': details.get('description'),
                'period': formatted_period #Agora vai o texto bonito e correto!
            }
            return info_weather
        return None
    
    except Exception:
        # Caso ocorra erro de conexão
        return None
