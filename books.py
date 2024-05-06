'''
NAME
    books

DESCRIPTION
    Moduł umożliwia dodawanie książek do pliku csv lub ich usuwanie z tego pliku.

FUNCTIONS
    Moduł ten zawiera następujące funkcje:
    * dodaj_ksiazke() - funkcja przyjmuje dane książki, sprawdza czy podana książka nie jest już w bazie
    jeśli nie to jest dodawana.
    * usun_ksiazke() - użytkownik podaje według czego chce usunać książke i podaje te dane, funkcja sprawdza czy podane
    dane są w pliku csv jesli tak to je usuwa.

EXAMPLES
    dodaj_ksiazke(id=7432, autor="Adam Mickiewicz", tytul="Pan Tadeusz", liczba_stron=300, data_dodania="2024-05-06")
    usun_ksiazke(identyfikator=4352, opcja="id")
'''

import csv


def dodaj_ksiazke(id, autor, tytul, liczba_stron, data_dodania):
    """
    Dodaje nową książkę do pliku CSV.

    Args:
        id (int): Identyfikator książki.
        autor (str): Autor książki.
        tytul (str): Tytuł książki.
        liczba_stron (int): Liczba stron książki.
        data_dodania (date): Data dodania ksiązki do bazy.
    """
    try:
        with open('book.csv', 'r') as file1:
            read = list(csv.reader(file1))
        for i in read:
            if i[0] == str(id):
                break
            elif i[1] == autor:
                break
            elif i[2] == tytul:
                break
        with open('book.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([id, autor, tytul, liczba_stron, data_dodania])
        print("Książka dodana pomyślnie do bazy.")
    except ValueError as e:
        print("ValueError exception:", e)
    except TypeError as e:
        print("TypeError exception:", e)
    except IOError as e:
        print("IOError exception:", e)

def usun_ksiazke(identyfikator, opcja):
    """
    Usuwa książkę z bazy na podstawie ID lub tytułu.

    Args:
        identyfikator (str or int): ID lub tytuł książki do usunięcia.
        opcja (str): 'id' lub 'tytuł'.
    """
    with open('book.csv', 'r', newline='', encoding='utf-8') as file:
        rows = list(csv.reader(file))

    if opcja == 'id':
        for row in rows:
            if row[0] == str(identyfikator):
                rows.remove(row)
                break
            else:
                print("Brak podanego id w bazie")
                break
    elif opcja == 'tytuł':
        for row in rows:
            if row[2] == str(identyfikator):
                rows.remove(row)
                break
            else:
                print("Brak podanego tytułu w bazie")
                break
    else:
        print("Nieprawidłowa opcja.")

    with open('book.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)
    print("Książka usunięta pomyślnie z bazy.")

