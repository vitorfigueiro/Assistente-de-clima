from .localizador import localization_ip
from .clima import get_weather
from .sugestoes import generate_suggestions
from .visuais import Show_Assistant_screen

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
        climate_date = get_weather(city)

        if climate_date:
            ideas = generate_suggestions(climate_date)
            Show_Assistant_screen(city, climate_date, ideas)
        else:
            print("Não consegui buscar os dados de clima. ❌")
    else:
        print('Não conseguimos te achar!')

if __name__ == '__main__':
    main()
