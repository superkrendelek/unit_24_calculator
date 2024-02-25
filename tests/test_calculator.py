import pytest

from app.calc import *

class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self, 1,1) == 2

    def test_adding_unseccess(self):
        assert self.calc.adding(self,1,1) == 3

    def test_multiply_success(self):
        assert self.calc.multiply(self, 2,4) == 8

    def test_division_success(self):
        assert self.calc.division(self, 9, 3) == 3

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 9, 3) == 6









    def test_zero_divizion(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.divizion(1, 0)

    def teardown_method(self):
        print('выполнение метода Teardown')