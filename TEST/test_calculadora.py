import pytest

from calculadora import Calculadora


class TestSumar:
    def test_sumar(self):
        assert Calculadora().sumar(2, 3) == 5


class TestRestar:
    def test_restar(self):
        assert Calculadora().restar(10, 4) == 6


class TestMultiplicar:
    def test_multiplicar(self):
        assert Calculadora().multiplicar(4, 5) == 20


class TestDividir:
    def test_dividir(self):
        assert Calculadora().dividir(10, 2) == 5

    def test_dividir_entre_cero(self):
        with pytest.raises(ZeroDivisionError):
            Calculadora().dividir(5, 0)
