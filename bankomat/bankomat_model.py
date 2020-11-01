from typing import Optional

from bankomat.bakomat_event import BankomatEvent


class BankomatModel:

    def __init__(self, prawidlowy_pin="1234", stan_konta=1000):
        self._kolejny_event: Optional[BankomatEvent] = None
        self._czy_podano_prawidlowy_pin: bool = False
        self._prawidlowy_pin = prawidlowy_pin
        self._stan_konta = stan_konta

    def wyplac_pieniadze(self, kwota):
        if not self._czy_podano_prawidlowy_pin:
            self._kolejny_event = BankomatEvent(BankomatEvent.ZARZADAJ_PIN)
        else:
            try:
                kwota = int(kwota)
            except ValueError:
                self._kolejny_event = BankomatEvent(BankomatEvent.POKAZ_KOMUNIKAT, "Podany tekst nie jest liczbą: '{}'".format(kwota))
                return
            if kwota > self._stan_konta:
                self._kolejny_event = BankomatEvent(BankomatEvent.POKAZ_KOMUNIKAT, "Brak środków na koncie")
            else:
                self._stan_konta -= kwota
                self._kolejny_event = BankomatEvent(BankomatEvent.WYPLAC_PIENIADZE, kwota)

    def _kwota_to_int(self, kwota):
        try:
            return int(kwota)
        except ValueError:
            return -1

    def wyswietl_stan_konta(self):
        if not self._czy_podano_prawidlowy_pin:
            self._kolejny_event = BankomatEvent(BankomatEvent.ZARZADAJ_PIN)
        else:
            self._kolejny_event = BankomatEvent(BankomatEvent.POKAZ_KOMUNIKAT, "Obecny stan konta to {} zł".format(self._stan_konta))

    def podano_pin(self, pin: str):
        if pin == self._prawidlowy_pin:
            self._czy_podano_prawidlowy_pin = True
        else:
            self._kolejny_event = BankomatEvent(BankomatEvent.POKAZ_KOMUNIKAT, "Podany PIN jest nieprawidłowy")

    def pobierz_wychodzacy_event(self) -> BankomatEvent:
        wychodzacy_event = self._kolejny_event
        self._kolejny_event = None
        return wychodzacy_event

    def czy_jest_event(self) -> bool:
        return self._kolejny_event is not None
