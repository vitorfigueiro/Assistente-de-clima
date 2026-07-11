import requests

def localization_complete():
    try:
        # Fazemos uma requisição GET para a API pública ip-api
        # O parâmetro ?lang=pt-br garante que os nomes venham em português
        response = requests.get("http://ip-api.com/json/?lang=pt-br")

        # Converte a resposta em um dicionário Python (JSON)
        data = response.json()

        # A API retorna um campo chamado 'status'. Se for 'success', deu certo!
        if data.get('status') == 'success':
            return {
                "city": data.get('city'),
                "lat": data.get('lat'),
                "lon": data.get('lon')
                }
        else:
            return None
        
    except Exception:
        # Se o usuário estiver sem internet ou a API estiver fora do ar, entra aqui
        return None
