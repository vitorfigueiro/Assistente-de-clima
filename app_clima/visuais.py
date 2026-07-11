from rich.console import Console
from rich.panel import Panel

# Inicializa o controlador do Rich
console = Console()

def Show_Assistant_screen(city, climate_date, ideas):
    """
    Usa a biblioteca Rich para criar painéis estilizados e coloridos
    no terminal baseando-se no tipo de ambiente sugerido.
    """
    environment = ideas["environment"]
    # 1 - Definindo as cores de cada tema
    if environment == 'frio':
        color_teme = "bold cyan"
        style_edge = "cyan"
    elif environment == "noturno":
        color_teme = "bold magenta"
        style_edge = "magenta"
    elif environment == "quente":
        color_teme = "bold yellow"
        style_edge = "yellow"
    else:
        color_teme = "bold white"
        style_edge = "white"

    # 2 - Limpa o terminal para deixar com efeito de aplicativo
    console.clear()

    # 3 - Cabeçalho
    console.print(Panel(
        f"[{color_teme}]⚡ ASSISTENTE DE CLIMA E PRODUTIVIDADE ⚡[/{color_teme}]",
        expand = False,
        border_style = style_edge
    ))

    # 4 - Painel de informações
    text_climate = (
        f"📍 [bold]Localização:[/bold] {city}\n"
        f"🌡️ [bold]Temperatura:[/bold] {climate_date['temperature']}°C\n"
        f"🔺 [bold]Máxima de Hoje:[/bold] [bold red]{climate_date['maximum']}°C[/bold red] |"
        f"🔻 [bold]Mínima de Hoje:[/bold] [bold blue]{climate_date['minimum']}°C[/bold blue]\n"
        f"🌧️ [bold]Chance de Chuva:[/bold] {climate_date['chance_rain']}%\n"
        f"☁️ [bold]Condição:[/bold] {climate_date['condition']}\n"
        f"🕒 [bold]Período:[/bold] {climate_date['period']}"
    )
    console.print(Panel(text_climate, title = "🌍 Condições do Mundo Real", border_style = style_edge))

    # 5 - Painel de sugestões
    text_suggestions = (
        f"🎵 [bold]Playlist Recomendada:[/bold] {ideas['playlist']}\n"
        f"💻 [bold]Comando Sugerido:[/bold]  `{ideas['command']}`"
    )
    console.print(Panel(text_suggestions, title = "🚀 Sugestões para o seu Momento", border_style = style_edge))
