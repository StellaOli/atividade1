def validar_nota(nota):
    """Valida se a nota esta entre 0 e 10."""
    return 0 <= nota <= 10

def calcular_media(*notas):
    """Media ignorando inválidas."""
    if notas:
        notas = [nota for nota in notas if nota >= 0 and nota <= 10]
        if notas:
            return sum(notas)/len(notas)

def obter_situacao(media):
    """Aprovado/Recuperacao/Reprovado."""
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperacao"
    else:
        return "Reprovado"

def calcular_estatisticas(*notas):
    """Calcula estatísticas básicas: média, mínimo e máximo."""
    notas_validas = [nota for nota in notas if 0 <= nota <= 10]
    if not notas_validas:
        return None
    media = sum(notas_validas) / len(notas_validas)
    minimo = min(notas_validas)
    maximo = max(notas_validas)
    return {"media": media, "minimo": minimo, "maximo": maximo}

def normalizar_notas(notas, nota_maxima=10):
    """Converte notas para uma escala de 0 a 10."""
    if not notas or nota_maxima <= 0:
        return []
    
    notas_validas = [nota for nota in notas if 0 <= nota <= nota_maxima]
    
    if nota_maxima == 10:
        return notas_validas
    
    fator = 10 / nota_maxima
    return [round(nota * fator, 2) for nota in notas_validas]