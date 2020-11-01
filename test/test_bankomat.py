import pytest

from bankomat.bakomat_event import BankomatEvent


def test_wyswietl_stan_konta_prawidlowy_pin(bankomat, prawidlowy_pin):
    bankomat.wyswietl_stan_konta()
    assert bankomat.czy_jest_event()
    assert bankomat.pobierz_wychodzacy_event().typ == BankomatEvent.ZARZADAJ_PIN
    bankomat.podano_pin(prawidlowy_pin)
    bankomat.wyswietl_stan_konta()
    assert bankomat.czy_jest_event()
    event = bankomat.pobierz_wychodzacy_event()
    assert event.typ == BankomatEvent.POKAZ_KOMUNIKAT
    assert event.parametr == "Obecny stan konta to 2000 zł"

def test_wyswietl_stan_konta_nieprawidlowy_pin(bankomat, nieprawidlowy_pin):
    bankomat.wyswietl_stan_konta()
    assert bankomat.czy_jest_event()
    assert bankomat.pobierz_wychodzacy_event().typ == BankomatEvent.ZARZADAJ_PIN
    bankomat.podano_pin(nieprawidlowy_pin)
    assert bankomat.czy_jest_event()
    event = bankomat.pobierz_wychodzacy_event()
    assert event.typ == BankomatEvent.POKAZ_KOMUNIKAT
    assert event.parametr == "Podany PIN jest nieprawidłowy"

    bankomat.wyswietl_stan_konta()
    assert bankomat.czy_jest_event()
    assert bankomat.pobierz_wychodzacy_event().typ == BankomatEvent.ZARZADAJ_PIN



@pytest.fixture
def prawidlowy_pin():
    return "1111"

@pytest.fixture
def nieprawidlowy_pin():
    return "2222"


@pytest.fixture
def poczatkowy_stan_konta():
    return 2000


@pytest.fixture
def bankomat(prawidlowy_pin, poczatkowy_stan_konta):
    from bankomat.bankomat_model import BankomatModel
    return BankomatModel(prawidlowy_pin=prawidlowy_pin, stan_konta=poczatkowy_stan_konta)
