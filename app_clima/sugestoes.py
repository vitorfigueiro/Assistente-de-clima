def generate_suggestions(climate_data):
    """
    Recebe os dados do clima e retorna um dicionário com sugestôes
    da playlist, comandos de produtividade e uma cor para o terminal
    """
    condition = climate_data["condition"].lower() #deixa o texto em minúsculo
    period = climate_data["period"] 
    
    # 1 - vamos criar sugestões para se caso o clima não seguir nenhuma regra especifica
    suggestions = {
        "playlist": "Foco Profundo / Deep Focus Intellect",
        "command": "todo list (Revise suas tarefas pendentes)",
        "environment": "padrão"
    }

    # Dias de CHUVA
    if "chuva" in condition or "tempestade" in condition:
        suggestions["playlist"] = "Lo-fi Beats para codar em Dias de Chuva 🌧️"
        suggestions["command"] = "pomodoro star 25 (Foco total no código)"
        suggestions["environment"] = "frio" #Vamos usar depois para pintar o terminal
    # Noites limpas ou nubladas
    elif period == "noturno":
        suggestions["playlist"] = "Skillet / Revolution 🌌"
        suggestions["command"] = "git status (Hora de revisar o dia e corrigir erros)"
        suggestions["environment"] = "noturno"
    # Dias ensolarados
    elif "limpo" in condition or "sol" in condition or "nublado" in condition:
        suggestions["playlist"] = "BlueRay energético / Rock pesado ☕"
        suggestions["command"] = "git add (Criar novos projetos, estudar!)"
        suggestions["environment"] = "quente"

    return suggestions
    