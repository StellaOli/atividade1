import pytest
from calculadora import validar_nota, calcular_media, obter_situacao, calcular_estatisticas, normalizar_notas

def test_validar_nota():
    assert validar_nota(5) == True
    assert validar_nota(0) == True
    assert validar_nota(10) == True
    assert validar_nota(-1) == False
    assert validar_nota(11) == False

def test_calcular_media():
    assert calcular_media(5, 7, 9) == 7.0
    assert calcular_media(10, 10, 10) == 10.0
    assert calcular_media(5, -1, 11) == 5.0
    assert calcular_media() is None
    assert calcular_media(-1, 11) is None

def test_obter_situacao():
    assert obter_situacao(7) == "Aprovado"
    assert obter_situacao(5) == "Recuperacao"
    assert obter_situacao(3) == "Reprovado"

def test_calcular_estatisticas():
    stats = calcular_estatisticas(5, 7, 9)
    assert stats == {"media": 7.0, "minimo": 5, "maximo": 9}
    
    stats = calcular_estatisticas(10, 10, 10)
    assert stats == {"media": 10.0, "minimo": 10, "maximo": 10}
    
    stats = calcular_estatisticas(5, -1, 11)
    assert stats == {"media": 5.0, "minimo": 5, "maximo": 5}
    
    assert calcular_estatisticas() is None
    assert calcular_estatisticas(-1, 11) is None

def test_normalizar_notas():
    assert normalizar_notas([5, 7, 9], 10) == [5.0, 7.0, 9.0]
    assert normalizar_notas([50, 70, 90], 100) == [5.0, 7.0, 9.0]
    assert normalizar_notas([5, -1, 11], 10) == [5.0]
    assert normalizar_notas([], 10) == []
    assert normalizar_notas([5, 7, 9], 0) == []

if __name__ == "__main__":
    pytest.main()   
