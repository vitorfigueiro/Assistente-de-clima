import sys
from .localizador import localization_complete
from .clima import get_weather
from .sugestoes import generate_suggestions
from .visuais import Show_Assistant_screen

def automated_assistant():
    print('============================================')
    print('A Sua Assistente de Clima! A sua disposição!')
    print('============================================\n')

    print('Buscando sua localização pelo seu IP.\n')

    # Chamamos a função
    info_location = localization_complete()

    if info_location:
        city = info_location["city"]
        lat = info_location["lat"]
        lon = info_location["lon"]

        # Chamamos a nova engrenagem passando a cidade detectada
        climate_date = get_weather(lat, lon)

        if climate_date:
            ideas = generate_suggestions(climate_date)
            Show_Assistant_screen(city, climate_date, ideas)
        else:
            print("Não consegui buscar os dados de clima. ❌")
    else:
        print('Não conseguimos te achar!')

def manual_assistant():
    """
    Permite ao usuário digitar qualquer cidade para consultar.
    """
    city = input("\n🔎 Digite o nome da cidade (ex: Caocal, Porto Velho): ").strip()
    if not city:
        print("Nome Inválido!")
        return
    
    print(f'Buscando clima para: {city}')

    # A WeatherAPI aceita tanto cordenadas "lat, lon" quanto o NOME da cidade diretamente no parâmetro "q"
    # Então podemos passar o nome da cidade no lugar de latitude e longitude
    climate_data = get_weather(city, "")

    if climate_data:
        ideas = generate_suggestions(climate_data)
        Show_Assistant_screen(city, climate_data, ideas)
    else:
        print(f"❌ Nãoo encontrei dados para {city}. Verifique a grafia ou sua chave API.")

def main():
    # Primeira execução automática ao iniciar
    automated_assistant()

    while True:
        print('\n' + '=' * 40)
        print(" MENU DO ASSISTENTE ")
        print("[1] Atualizar clima atual (Localização automática)")
        print("[2] Consultar outra cidade manualmente")
        print("[3] Sair")
        print('=' * 40)

        option = input("Escolha uma opção: ").strip()

        if option == "1":
            automated_assistant()
        elif option == "2":
            manual_assistant()
        elif option == "3":
            print("\nObrigado por usar o Assistente de Clima! Até mais! 👋")
            sys.exit()
        else:
            print("❌ Opção Inválida! Digite uma opção entre 1 e 3!")

if __name__ == '__main__':
    main()
