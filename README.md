# ks-plan
Wyszukiwarka służb i pociągów z planu

## Schema SQL

Tabela **grafik.holidays** odpowiada za przechowywanie informacji o dniach świątecznych.

|Nazwa|Typ  |
|-----|-----|
|id|serial|
|termin|date|
|opis|varchar(100)|
|wariant|varchar(2)|

Tabela **grafik.pociagi** odpowiada za informację o odcinkach obsługiwanych w ramach przebiegu służby (nr pociągu, obieg, stacja początkowa i końcowa obsługi, godziny odjazdu i przyjazdu oraz tabor).

|Nazwa|Typ  |
|-----|-----|
|id|serial|
|termin|date|
|wariant|varchar(2)|

Tabela **grafik.sluzby** odpowiada za przechowywanie informacji o godzinie rozpoczęcia i zakończenia służby, oraz stacji początkowej. Na podstawie tabel sluzby i pociagi mozna przygotowac wydruk służby zgodny z wydawanym przez firmę.

## Wymagania
* python
* python-psycopg2
* flask
* peewee
* flask-login
* twitter bootstrap
* xhtml2pdf

## Funkcjonalność i obsługa
