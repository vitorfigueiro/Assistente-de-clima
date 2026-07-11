def generate_suggestions(climate_data):
    """
    Recebe os dados do clima e retorna um dicionário com sugestôes
    da playlist, comandos de produtividade e uma cor para o terminal
    """
    current_temp = climate_data['temperature']
    maximum = climate_data['maximum']
    minimum = climate_data['minimum']
    chance_rain = climate_data['chance_rain']
    period = climate_data['period']
    
    # 1 - Ambiente base
    if period == 'Noturno':
        environment = 'Noturno'
        playlist = 'Lofi Sleep & Chill 🌌'
        command = 'Programa os alarmes e revise os logs do dia.'
    elif current_temp > 28:
        environment = 'Quente'
        playlist = 'Skillet / Retrowave Focus ☀️'
        command = 'Beba água! Perfeito para focar em códigos complexos no ar-condicionado.'
    elif current_temp > 20:
        environment = 'Frio'
        playlist = 'Deep Focus / Ambient Piano ☕'
        command = 'Pegue um café e bora buildar.'
    else:
        environment = 'Padrao'
        playlist = 'Productive Flow / Chillhop 🍃'
        command = 'Clima agradáve. Ótimo ritmo para srpint de desenvolvimento.'

    # 2 - Sistema de alertas inteligentes
    alert = []

    # Alerta de Chuva
    if chance_rain and chance_rain > 50:
        alert.append(f"🌧️ [bold red]Alerta de Chuva ({chance_rain}%):[/bold red] Evite atividades externas no fim do dia.")
    elif chance_rain and chance_rain > 20:
        alert.append(f"⛅ [bold yellow]Tempo Instável ({chance_rain}% de chuva):[/bold yellow] Vale a pena ficar de olho no céu.")
    
    # Alerta de Amplitude Térmica
    if maximum and minimum and (maximum - minimum) > 10:
        alert.append(f"🌡️ [bold cyan]Mudança Brusca de Temp:[/bold cyan] O dia vai de {minimum}°C a {maximum}°C. Leve um casaco!")
    
    # se não houver nenhum alerta especial
    if not alert:
        alert.append(f"✅ [bold green]Condições Estáveis:[/bold green] Sem alertas climáticos para as próximas horas.")
    
    return {
        "environment": environment,
        "playlist": playlist,
        "command": command,
        "alert": alert
    }