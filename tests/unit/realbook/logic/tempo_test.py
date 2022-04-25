from decimal import Decimal

from realbook.logic import tempo


def test_calculate_no_last_timestamp():
    actual = tempo.calculate(Decimal('1'), None)

    assert actual == Decimal('60')


def test_calculate_with_last_timestamp():
    actual = tempo.calculate(Decimal('1'), Decimal('0'))

    assert actual == Decimal('60')


def test_calculate_with_expected_tempo():
    actual = tempo.calculate(Decimal('1'), Decimal('0.5'))

    assert actual == Decimal('120')
