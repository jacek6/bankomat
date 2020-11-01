import tkinter as tk
from tkinter.simpledialog import askstring

from bankomat.bakomat_event import BankomatEvent
from bankomat.bankomat_model import BankomatModel



if __name__ == '__main__':
    bankomat: BankomatModel = BankomatModel()


    def wyplac_pieniadze_clicked():
        kwota = wpisana_kwota.get()
        bankomat.wyplac_pieniadze(kwota)
        process_bankomat_event()


    def wyswietl_stan_konta_clicked():
        bankomat.wyswietl_stan_konta()
        process_bankomat_event()

    def process_bankomat_event():
        while bankomat.czy_jest_event():
            event: BankomatEvent = bankomat.pobierz_wychodzacy_event()
            if event.typ == BankomatEvent.ZARZADAJ_PIN:
                pin = askstring("PIN", "Prosze podac pin:")
                bankomat.podano_pin(pin)
            elif event.typ == BankomatEvent.POKAZ_KOMUNIKAT:
                label.config(text = event.parametr)
            elif event.typ == BankomatEvent.WYPLAC_PIENIADZE:
                label.config(text = "Wypłacam {} zł".format(event.parametr))

    root = tk.Tk()
    root.title("Bankomat")
    label = tk.Label(root)
    label.config(text="Witaj")
    label.grid(row=0, column=0, padx=(30, 30), pady=(30, 20))
    button1 = tk.Button(root, text='Wyświetl stan konta', width=25, command=wyswietl_stan_konta_clicked)
    button2 = tk.Button(root, text='Wypłać pieniądze', width=25, command=wyplac_pieniadze_clicked)
    button1.grid(row=1, column=0, padx=(30, 30), pady=(30, 20))
    button2.grid(row=2, column=0, padx=(30, 30), pady=(30, 20))

    label2 = tk.Label(root)
    label2.config(text="Kwota do wypłaty:")
    label2.grid(row=3, column=0, padx=(30, 30), pady=(30, 8))
    wpisana_kwota = tk.StringVar()
    text_box = tk.Entry(root, width=20, textvariable=wpisana_kwota)
    text_box.grid(row=4, column=0, padx=(30, 30), pady=(8, 20))

    root.mainloop()

