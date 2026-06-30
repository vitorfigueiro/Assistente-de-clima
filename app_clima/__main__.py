from .localizador import localization_ip
from .clima import get_weather

def main():
    print('============================================')
    print('A Sua Assistente de Clima! A sua disposição!')
    print('============================================\n')

    print('Buscando sua localização pelo seu IP.\n')

    # Chamamos a função
    city = localization_ip()

    if city:
        print(f'Atualmente você está nessa localização {city}📍')
        print(f'Consultando as condições climaticas da cidade de {city}!')

        # Chamamos a nova engrenagem passando a cidade detectada
        data_weather = get_weather(city)

        if data_weather:
            print("\n--- Condições Atuais ---")
            print(f"Temperatura: {data_weather['temperatura']}°C")
            print(f"Condição: {data_weather['condicao']}")
            print(f"Período: Matutino/Vespertino ({data_weather['periodo']})")
        else:
            print("Não consegui buscar os dados de clima. ❌")
    else:
        print('Não conseguimos te achar!')

if __name__ == '__main__':
    main()
