from madlib import welcome, trypytest
# import pytest


# def test_welcome(new):
#     """Docstring."""
#     assert welcome(new)


def test_trypytest():
    """Test the pytest setup."""
    assert trypytest


def test_welcome_output_parameter():
    outputType = type(welcome('a string'))
    assert outputType == str













