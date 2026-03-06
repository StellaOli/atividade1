def calcular_frete(peso: float, destino: str, valor_pedido: float) -> float:

    # ===== Validação de tipos =====
    if not isinstance(peso, (int, float)):
        raise TypeError("Peso deve ser numérico")

    if not isinstance(destino, str):
        raise TypeError("Destino deve ser texto")

    if not isinstance(valor_pedido, (int, float)):
        raise TypeError("Valor do pedido deve ser numérico")

    # ===== Validação do valor do pedido =====
    if valor_pedido < 0:
        raise ValueError("Valor do pedido não pode ser negativo")

    # Frete grátis
    if valor_pedido > 200:
        return 0.0

    # ===== Validação do peso =====
    if peso <= 0:
        raise ValueError("Peso deve ser positivo")

    # ===== Faixas de peso =====
    if peso <= 1:
        frete_base = 10.0
    elif peso <= 5:
        frete_base = 15.0
    elif peso <= 20:
        frete_base = 25.0   
    else:
        raise ValueError("Peso acima do limite permitido")

    # ===== Destino =====
    destino = destino.lower()

    if destino == "mesma_regiao":
        return frete_base
    elif destino == "outra_regiao":
        return frete_base * 1.5
    elif destino == "internacional":
        return frete_base * 2.0
    else:
        raise ValueError("Destino inválido")