from .localizador import localization_ip
from .clima import get_weather
from .sugestoes import generate_suggestions

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
            print(f"Temperatura: {data_weather['temperature']}°C")
            print(f"Condição: {data_weather['condition']}")
            print(f"Período: Matutino/Vespertino ({data_weather['period']})")

            # -----------------------------
            #         ATUALIZAÇÃO
            #------------------------------
            ideas = generate_suggestions(data_weather)
            print("\n----Sugestôes para o seu Dia----")
            print(f"🎵 Playlist Recomendada: {ideas['playlist']}")
            print(f"💻 Comando de Produtividade: {ideas['command']}")
            print(f"🎨 Estilo de Ambiente: {ideas['environment']}")
        else:
            print("Não consegui buscar os dados de clima. ❌")
    else:
        print('Não conseguimos te achar!')

if __name__ == '__main__':
    main()
