from books import *
from customers import *
import random
from datetime import date


def main1():
    co_robic = input("Co chesz zrobić? \n"
                     "1 Dodać książkę. \n"
                     "2 Usunać książkę. \n"
                     "3 Dodać klienta. \n"
                     "4 Usunąć klienta. \n"
                     "5 Wypożyczenie książki. \n"
                     "6 Zwrot książki. ")
    if co_robic == "1":
        id1 = random.randint(1000, 9999)
        autor = input("Podaj autora. ")
        tytul = input("Podaj tytuł. ")
        liczba_stron = int(input("Podaj liczbe stron. "))
        data_dodania = date.today()
        dodaj_ksiazke(id1, autor, tytul, liczba_stron, data_dodania)
    elif co_robic == "2":
        opcja = input("Według czego usunać książke id lub tytuł? ")
        identyfikator = input("Co wybrałes to to podaj. ")
        usun_ksiazke(identyfikator, opcja)
    elif co_robic == "3":
        dodaj_klienta(dane_klienta())
    elif co_robic == "4":
        opcja1 = input("Według czego usunać klienta id lub imie_nazwisko? ")
        identyfikator1 = input("Co wybrałes to to podaj. ")
        usun_klienta(identyfikator1, opcja1)
    elif co_robic == "5":
        idklienta = input("Podaj id klienta który chce wypożyczyć książke.")
        tytuly = input("Podaj tytuły książek oddzielone przecinkem: ").split(',')
        wypozycz(idklienta, *tytuly)
    elif co_robic == "6":
        idklienta1 = input("Podaj id klienta który chce zwrócić książki.")
        tytuly1 = input("Podaj tytuły książek oddzielone przecinkem: ").split(',')
        zwrot(idklienta1, *tytuly1)


if __name__ == "__main__":
    main1()
