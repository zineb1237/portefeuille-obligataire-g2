import pytest
from bond import prix, ytm_bissection, duration_macaulay

N = 100  


def test_prix_au_pair():
 
    assert prix(0.03, 0.03, N, 5) == pytest.approx(100)


def test_prix_zero_coupon():
   
    assert prix(0.05, 0.0, N, 1) == pytest.approx(100 / 1.05)


def test_ytm_obligation_1_an():
   
    y = ytm_bissection(99.5, 0.02, N, 1)
    assert y == pytest.approx(102 / 99.5 - 1, abs=1e-6)


def test_ytm_redonne_le_prix():

    y = ytm_bissection(98.0, 0.04, N, 5)
    assert prix(y, 0.04, N, 5) == pytest.approx(98.0, abs=1e-6)


def test_duration_zero_coupon():
  
    assert duration_macaulay(0.03, 0.0, N, 5) == pytest.approx(5)


def test_duration_inferieure_maturite():
  
    assert duration_macaulay(0.03, 0.04, N, 5) < 5