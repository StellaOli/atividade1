import re


def _apenas_digitos(cpf: str) -> str:
    """Remove tudo que não for dígito."""
    return re.sub(r"\D", "", cpf)


def _todos_digitos_iguais(cpf: str) -> bool:
    """Verifica se todos os dígitos são iguais."""
    return cpf == cpf[0] * len(cpf)


def _calcular_digito(cpf_parcial: str) -> str:
    """Calcula um dígito verificador."""
    soma = 0
    peso = len(cpf_parcial) + 1

    for digito in cpf_parcial:
        soma += int(digito) * peso
        peso -= 1

    resto = soma % 11
    return "0" if resto < 2 else str(11 - resto)


def validar_cpf(cpf: str) -> bool:
    """
    Regras:
    - Deve conter 11 dígitos
    - Não pode ter todos os dígitos iguais
    - Deve possuir dígitos verificadores corretos
    """

    # Validação básica
    if cpf is None or not isinstance(cpf, str):
        return False

    cpf = _apenas_digitos(cpf)

    if len(cpf) != 11:
        return False

    if _todos_digitos_iguais(cpf):
        return False

    # Cálculo dos dígitos verificadores
    digito1 = _calcular_digito(cpf[:9])
    digito2 = _calcular_digito(cpf[:9] + digito1)

    return cpf[-2:] == digito1 + digito2


def formatar_cpf(cpf: str) -> str:
    """
    Formata CPF válido para XXX.XXX.XXX-XX.

    Levanta ValueError se inválido.
    """

    if not validar_cpf(cpf):
        raise ValueError("CPF inválido")

    cpf = _apenas_digitos(cpf)

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"