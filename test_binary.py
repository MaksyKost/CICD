import pytest

import binary_converter


def test_dec_to_bin():
    assert binary_converter.dec_to_bin(10) == "1010"
    assert binary_converter.dec_to_bin(0) == "0"
    assert binary_converter.dec_to_bin(100) == "1100100"


def test_dec_to_bin_out_of_bounds():
    with pytest.raises(ValueError):
        binary_converter.dec_to_bin(-1)
    with pytest.raises(ValueError):
        binary_converter.dec_to_bin(101)


def test_dec_to_bin_not_integer():
    with pytest.raises(TypeError):
        binary_converter.dec_to_bin(10.5)
