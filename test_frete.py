import pytest
from hypothesis import given, strategies as st
from frete import calcular_frete


# =========================================================
# CLASSES DE EQUIVALÊNCIA 
# =========================================================

@pytest.mark.parametrize("peso,destino,valor,esperado", [
    (0.5, "mesma_regiao", 167, 10.0),
    (3, "mesma_regiao", 167, 15.0),
    (11, "mesma_regiao", 167, 25.0),
    (3, "outra_regiao", 167, 22.5),
    (3, "internacional", 167, 30.0),
])
def test_classes_equivalencia(peso, destino, valor, esperado):
    assert calcular_frete(peso, destino, valor) == esperado


# =========================================================
# VALORES LIMITE 
# =========================================================

@pytest.mark.parametrize("peso", [0.5, 3, 11])
def test_valores_limite_validos(peso):
    assert calcular_frete(peso, "mesma_regiao", 167) >= 0


# =========================================================
# TABELA DE DECISÃO
# =========================================================

@pytest.mark.parametrize("destino,esperado", [
    ("mesma_regiao", 15.0),
    ("outra_regiao", 22.5),
    ("internacional", 30.0),
])
def test_tabela_decisao(destino, esperado):
    assert calcular_frete(3, destino, 167) == esperado


# =========================================================
# ENTRADAS INVÁLIDAS 
# =========================================================

def test_peso_negativo():
    with pytest.raises(ValueError):
        calcular_frete(-1, "mesma_regiao", 167)


def test_peso_nao_numerico():
    with pytest.raises(TypeError):
        calcular_frete("a", "mesma_regiao", 167)


def test_destino_nao_textual():
    with pytest.raises(TypeError):
        calcular_frete(3, 987, 167)


def test_destino_invalido():
    with pytest.raises(ValueError):
        calcular_frete(3, "minha_casa", 167)


def test_valor_nao_numerico():
    with pytest.raises(TypeError):
        calcular_frete(3, "mesma_regiao", "dez")


def test_valor_negativo():
    with pytest.raises(ValueError):
        calcular_frete(3, "mesma_regiao", -100)


# =========================================================
# FRETE GRÁTIS
# =========================================================

def test_frete_gratis():
    assert calcular_frete(3, "mesma_regiao", 205) == 0.0


# =========================================================
# PROPERTY-BASED TESTING 
# =========================================================

@given(
    peso=st.floats(min_value=0.0001, max_value=20),
    destino=st.sampled_from(["mesma_regiao", "outra_regiao", "internacional"]),
    valor=st.floats(min_value=0, max_value=200),
)
def test_frete_nunca_negativo(peso, destino, valor):
    frete = calcular_frete(peso, destino, valor)
    assert frete >= 0


@given(
    peso=st.floats(min_value=0.0001, max_value=20),
    destino=st.sampled_from(["mesma_regiao", "outra_regiao", "internacional"]),
    valor=st.floats(min_value=200.01, max_value=10000),
)
def test_frete_gratis_propriedade(peso, destino, valor):
    assert calcular_frete(peso, destino, valor) == 0.0


@given(
    peso=st.floats(min_value=0.0001, max_value=20),
    valor=st.floats(min_value=0, max_value=200),
)
def test_outra_regiao_maior(peso, valor):
    mesma = calcular_frete(peso, "mesma_regiao", valor)
    outra = calcular_frete(peso, "outra_regiao", valor)
    assert outra >= mesma