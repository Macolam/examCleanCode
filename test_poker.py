from poker import *
import pytest

def test_isBrelan():
    assert isBrelan([('14', 'coeur'), ('14', 'pique'), ('14', 'trefles'), ('3', 'trefles'), ('6', 'trefles')]) == True
    assert isBrelan([('14', 'coeur'), ('14', 'pique'), ('14', 'trefles'), ('3', 'trefles'), ('6', 'trefles')]) == False