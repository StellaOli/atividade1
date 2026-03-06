from caixaBranca import *


# ================================
# Exercício 1
# ================================

def test_par_positivo():
    assert verificar(4) == "Par positivo"

def test_impar_positivo():
    assert verificar(3) == "Impar positivo"

def test_negativo():
    assert verificar(-2) == "Negativo"

def test_zero():
    assert verificar(0) == "Zero"


# ================================
# Exercício 2
# ================================

def test_valor_alto():
    assert classificar(120) == "Alto"

def test_valor_medio():
    assert classificar(70) == "Medio"

def test_valor_baixo():
    assert classificar(30) == "Baixo"


# ================================
# Exercício 3
# ================================

def test_acesso_permitido():
    assert acesso(20, True) == "Permitido"

def test_acesso_negado_nao_membro():
    assert acesso(20, False) == "Negado"

def test_acesso_negado_menor():
    assert acesso(16, True) == "Negado"

def test_acesso_negado_total():
    assert acesso(16, False) == "Negado"


# ================================
# Exercício 4
# ================================

def test_laco_ignorado():
    assert somar_ate(0) == 0

def test_uma_iteracao():
    assert somar_ate(1) == 0

def test_varias_iteracoes():
    assert somar_ate(3) == 3


# ================================
# Exercício 5
# ================================

def test_matriz_vazia():
    assert percorrer_matriz(0, 0) == 0

def test_j_ignorado():
    assert percorrer_matriz(3, 0) == 0

def test_um_loop():
    assert percorrer_matriz(1, 3) == 3

def test_varios_loops():
    assert percorrer_matriz(3, 3) == 9


# ================================
# Exercício 6
# ================================

def test_lista_vazia():
    assert analisar([]) == "Abaixo"

def test_par_positivo_analisar():
    assert analisar([2]) == "Abaixo"

def test_negativo_analisar():
    assert analisar([-1]) == "Abaixo"

def test_continue_analisar():
    assert analisar([3]) == "Abaixo"

def test_acima():
    assert analisar([4, 4, 4]) == "Acima"


# ================================
# Exercício 7
# ================================

def test_cliente_vip():
    assert desconto(100, True) == 80

def test_preco_minimo():
    assert desconto(30, False) == 50