from calc import calcular_igv
from calc import aplicar_descuento
from calc import aplicar_recargo


def test_calcular_igv():
    assert calcular_igv(100) == 18


def test_aplicar_descuento():
    assert aplicar_descuento(100, 10) == 90


def test_aplicar_recargo():
    assert aplicar_recargo(100, 10) == 110