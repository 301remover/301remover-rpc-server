import unittest
import pytest
from unshortener_rpc.base_converter.base_converter import BaseConverter

DIGITS = '0123456789'
LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
FULL_ALPHABET = DIGITS + LOWERCASE + UPPERCASE + '-_'


def test_int_to_int_conversion():
    converter = BaseConverter(FULL_ALPHABET)
    results = []
    for i in range(0, 10000):
        result = converter.int_to_str(i)
        assert result not in results  # check for uniqueness
        assert converter.str_to_int(result) == i
        results.append(result)


def test_int_to_int_conversion_with_bytes():
    converter = BaseConverter(FULL_ALPHABET)
    for i in range(0, 10000):
        res = converter.str_to_int(
            converter.bytes_to_str(
                converter.str_to_bytes(
                    converter.int_to_str(i)
                )
            )
        )
        assert res == i


def test_int_to_str():
    converter = BaseConverter(FULL_ALPHABET)
    assert converter.int_to_str(1) == '0'
    assert converter.int_to_str(66) == '00'
    assert converter.int_to_str(11) == 'a'
    assert converter.int_to_str(37) == 'A'
    assert converter.int_to_str(129) == '0_'


def test_str_to_int():
    converter = BaseConverter(FULL_ALPHABET)
    assert converter.str_to_int('0') == 1
    assert converter.str_to_int('00') == 66
    assert converter.str_to_int('a') == 11
    assert converter.str_to_int('A') == 37
    assert converter.str_to_int('0_') == 129


def test_str_to_bytes():
    converter = BaseConverter(FULL_ALPHABET)
    with pytest.raises(ValueError):
        converter.int_to_str(-1)
