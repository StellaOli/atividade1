import pytest
from cpf import validar_cpf, formatar_cpf


# =========================
# Fixtures
# =========================

@pytest.fixture
def cpfs_validos():
    return [
        "52998224725",   # padrão
        "11144477735",   # válido conhecido
        "00000000191",   # válido com zeros
    ]


@pytest.fixture
def cpfs_invalidos():
    return [
        "12345678900",   # verificadores errados
        "11111111111",   # todos iguais
        "123",           # curto
        "123456789012",  # longo
        "abcdefghijk",   # letras
        "",              # vazio
        None             # None
    ]


# =========================
# validar_cpf — Válidos
# =========================

@pytest.mark.parametrize(
    "cpf",
    ["52998224725", "11144477735", "00000000191"],
    ids=["padrao", "conhecido", "com_zeros"]
)
def test_validar_cpf_valido_retorna_true(cpf):
    # Arrange

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is True


# =========================
# validar_cpf — Inválidos
# =========================

@pytest.mark.parametrize(
    "cpf",
    [
        "12345678900",
        "11111111111",
        "123",
        "123456789012",
        "abcdefghijk",
        "",
        None
    ],
    ids=[
        "verificador_errado",
        "todos_iguais",
        "curto",
        "longo",
        "letras",
        "vazio",
        "none"
    ]
)
def test_validar_cpf_invalido_retorna_false(cpf):
    # Arrange

    # Act
    resultado = validar_cpf(cpf)

    # Assert
    assert resultado is False


# =========================
# Fixtures — Testes
# =========================

def test_fixture_cpfs_validos_sao_aceitos(cpfs_validos):
    # Arrange

    # Act & Assert
    for cpf in cpfs_validos:
        assert validar_cpf(cpf) is True


def test_fixture_cpfs_invalidos_sao_rejeitados(cpfs_invalidos):
    # Arrange

    # Act & Assert
    for cpf in cpfs_invalidos:
        assert validar_cpf(cpf) is False


# =========================
# formatar_cpf — Sucesso
# =========================

def test_formatar_cpf_valido_retorna_formatado():
    # Arrange
    cpf = "52998224725"

    # Act
    resultado = formatar_cpf(cpf)

    # Assert
    assert resultado == "529.982.247-25"


def test_formatar_cpf_valido_com_zeros():
    # Arrange
    cpf = "00000000191"

    # Act
    resultado = formatar_cpf(cpf)

    # Assert
    assert resultado == "000.000.001-91"


# =========================
# formatar_cpf — Exceções
# =========================

@pytest.mark.parametrize(
    "cpf",
    ["12345678900", "11111111111", "", None],
    ids=["verificador_errado", "todos_iguais", "vazio", "none"]
)
def test_formatar_cpf_invalido_levanta_value_error(cpf):
    # Arrange

    # Act & Assert
    with pytest.raises(ValueError):
        formatar_cpf(cpf)