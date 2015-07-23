# coding: utf8
import pytest


def test_true():
    assert 1 == 1


def test_false():
    assert 1 == 2


def test_raise():
    a = {}
    with pytest.raises(KeyError):
        b = a[1]
