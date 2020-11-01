
class BankomatEvent:

    WYPLAC_PIENIADZE = 1
    POKAZ_KOMUNIKAT = 2
    ZARZADAJ_PIN = 3


    def __init__(self, typ, parametr=None):
        self._typ = typ
        self._parametr = parametr

    @property
    def typ(self):
        return self._typ

    @property
    def parametr(self):
        return self._parametr