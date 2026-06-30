from .localizador import localization_ip

def main():
    print('============================================')
    print('A Sua Assistente de Clima! A sua disposição!')
    print('============================================\n')

    print('Buscando sua localização pelo seu IP.\n')

    # Chamamos a função
    city = localization_ip()

    if city:
        print(f'Atualmente você está nessa localização {city}')
    else:
        print('Não conseguimos te achar!')

if __name__ == '__main__':
    main()

# Chamamos a função