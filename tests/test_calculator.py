import pytest
from calculator import (
    calculate_simple_interest,
    calculate_compound_interest,
    calculate_tax,
)

class TestSimpleInterest:
    def test_typical_cases(self):
        assert calculate_simple_interest(1000, 5, 3) == 150.0
        assert calculate_simple_interest(2000, 3.5, 2) == 140.0

    def test_zero_values(self):
        assert calculate_simple_interest(0, 5, 3) == 0.0
        assert calculate_simple_interest(1000, 0, 3) == 0.0
        assert calculate_simple_interest(1000, 5, 0) == 0.0

    def test_negative_values(self):
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(-100, 5, 3)
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(100, -5, 3)
        with pytest.raises(ValueError, match="Аргументы должны быть неотрицательными"):
            calculate_simple_interest(100, 5, -3)

class TestCompoundInterest:
    def test_typical_cases(self):
        result1 = calculate_compound_interest(1000, 5, 3, 1)
        assert round(result1, 3) == 1157.625
        result2 = calculate_compound_interest(1500, 4, 2, 4)
        assert round(result2, 3) == 1624.285

    def test_zero_values(self):
        assert calculate_compound_interest(0, 5, 3) == 0.0
        assert calculate_compound_interest(1000, 0, 3) == 1000.0
        assert calculate_compound_interest(1000, 5, 0) == 1000.0

    def test_negative_or_invalid_arguments(self):
        with pytest.raises(ValueError, match="principal, rate, time должны быть неотрицательными"):
            calculate_compound_interest(-1000, 5, 3)
        with pytest.raises(ValueError, match="principal, rate, time должны быть неотрицательными"):
            calculate_compound_interest(1000, -5, 3)
        with pytest.raises(ValueError, match="principal, rate, time должны быть неотрицательными"):
            calculate_compound_interest(1000, 5, -3)
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 3, n=2.5)
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 3, n=0)
        with pytest.raises(ValueError, match="n должно быть целым положительным числом"):
            calculate_compound_interest(1000, 5, 3, n=-1)

class TestTax:
    def test_typical_cases(self):
        assert calculate_tax(1000, 20) == 200.0
        assert calculate_tax(5000, 13) == 650.0

    def test_zero_values(self):
        assert calculate_tax(0, 20) == 0.0
        assert calculate_tax(1000, 0) == 0.0

    def test_boundary_tax_rates(self):
        assert calculate_tax(1000, 0) == 0.0
        assert calculate_tax(1000, 100) == 1000.0

    def test_invalid_tax_rate(self):
        with pytest.raises(ValueError, match="tax_rate должна быть между 0 и 100"):
            calculate_tax(1000, -1)
        with pytest.raises(ValueError, match="tax_rate должна быть между 0 и 100"):
            calculate_tax(1000, 101)

    def test_negative_amount(self):
        with pytest.raises(ValueError, match="amount не может быть отрицательным"):
            calculate_tax(-500, 20)
