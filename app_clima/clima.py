import requests

def get_weather(city_name):
    """
    Conecta à API HG Weather para buscar as condições climáticas da cidade.
    Retorna um dicionário com os dados ou None se houver falha.
    """
    # Criamos o link da API passando o nome da cidade como parâmetro de busca
    url = f"https://api.hgbrasil.com/weather?key=development&city_name={city_name}"

    try:
        response = requests.get(url)
        data = response_json = response.json()

        # A HG Weather retorna os dados principais dentro da chave 'results'
        if 'results' in data:
            details = data['results']

            # Vamos extrair apenas as 3 informações que nos interessam:
            info_weather = {
                'temperatura': details.get('temp'),
                'condicao': details.get('description'),
                'periodo': details.get('currently')
            }
            return info_weather
        return None
    
    except Exception:
        # Caso ocorra erro de conexão
        return None
