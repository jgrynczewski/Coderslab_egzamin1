![Coders-Lab-1920px-no-background](https://user-images.githubusercontent.com/30623667/104709387-2b7ac180-571f-11eb-9b94-517aa6d501c9.png)

# Kilka ważnych informacji

Przed przystąpieniem do rozwiązywania zadań przeczytaj poniższe wskazówki

## Jak zacząć?

1. Stwórz [*fork*](https://guides.github.com/activities/forking/) repozytorium z zadaniami.
2. Sklonuj fork repozytorium (stworzony w punkcie 1) na swój komputer. Użyj do tego komendy `git clone adres_repozytorium`
Adres możesz znaleźć na stronie forka repozytorium po naciśnięciu w guzik "Clone or download".
3. Rozwiąż zadania i skomituj zmiany do swojego repozytorium. Użyj do tego komend `git add nazwa_pliku`.
Jeżeli chcesz dodać wszystkie zmienione pliki użyj `git add .` 
Pamiętaj że kropka na końcu jest ważna!
Następnie skommituj zmiany komendą `git commit -m "nazwa_commita"`
4. Wypchnij zmiany do swojego repozytorium na GitHubie.  Użyj do tego komendy `git push origin master`
5. Stwórz [*pull request*](https://help.github.com/articles/creating-a-pull-request) do oryginalnego repozytorium, gdy skończysz wszystkie zadania.

Poszczególne zadania rozwiązuj w odpowiednich plikach.

### Poszczególne zadania rozwiązuj w odpowiednich plikach.

**Repozytorium z ćwiczeniami zostanie usunięte 2 tygodnie po zakończeniu kursu. Spowoduje to też usunięcie wszystkich forków, które są zrobione z tego repozytorium.**


## Zadanie 1. (2pkt)

Napisz funkcję `check_character`, która:
* przyjmie napis oraz pojedynczy znak, 
* zwróci liczbę wystąpień znaku w napisie.

Nie korzystaj z metody `count`. Zamiast tego, użyj **pętli**, albo **list comprehension**.

##### Przykład:
```python
print(check_character('Order of the Phoenix', 'o'))
```
##### Wynik
```plaintext
2
```

> Wielkość znaków ma znaczenie `('A' != 'a' etc.)`.

Rozwiązanie wpisz w pliku `answer1.py`.

## Zadanie 2. (4pkt)

Napisz funkcję `get_random`.
Funkcja powinna:
* Przyjąć jeden opcjonalny parametr `number` &ndash; ilość liczb jakie mają zostać wylosowane. 
    **Domyślna wartość to `3`.**
* Losować kolejno liczby z przedziału 1-100. Wylosowane liczby nie mogą się powtarzać.
    Wykorzystaj do tego pętlę `while` i losuj tak długo, aż uzyskasz `number` unikalnych liczb.
    **Nie korzystaj z metod `sample` i `shuffle`.** 
* Jeżeli zostanie do niej przekazany błędny parametr funkcja powinna **wyrzucić** wyjątek `Exception` 
    z komunikatem `"Invalid Data!"`.
* Funkcja powinna zwrócić posortowaną listę wylosowanych liczb (od najmniejszej do największej).

Przykładowe wyniki działania funkcji:

##### Przykład:
```python
print(get_random(5))
```
##### Wynik (przykładowy):
```plaintext
[2, 33, 46, 81, 100]
```

##### Przykład:
```python
print(get_random())
```
##### Wynik (przykładowy):
```plaintext
[58, 66, 99]
```

Rozwiązanie zadania umieść w pliku `answer2.py`.

## Zadanie 3. (5pkt)

W bazie chcemy mieć następujące tabele:
```SQL
* Readers:
    id : serial primary key,
    name : varchar(60),
    email : varchar(60),
    is_active : boolean, nie może być null, standardowa wartość: true
* Books:
    id : serial primary key,
    title : varchar(60),
    price : decimal(5, 2), 
    author : varchar(60),
    publishing_houses_id: int
* PublishingHouses:
    id : serial primary key,
    name : varchar(60),
    city : varchar(20),
    address : varchar(120)
```

W pliku `answers3.py` znajdziesz szereg zmiennych: `query_1 = ""` ... `query_10 = ""`.
Napisz następujące zapytania SQL i umieść je odpowiednio we wskazanych zmiennych:

1. Tworzące tabelę `Readers` (email ma być unikatowy).
2. Tworzące tabelę `PublishingHouses`.
3. Tworzące tabelę `Books` (dodaj odpowiednią relację z tabelą `PublishingHouses`:
    * każda książka może mieć jednego wydawcę,
    * każdy wydawca może mieć wiele książek w ofercie).
4. Tworzące relację wiele do wielu między tabelami `Readers` a `Books`.
5. Wyciągające z bazy wszystkie książki o cenie większej niż 10.
6. Wstawiające do tabeli `PublishingHouses` nowe wydawnictwo o nazwie "Super Książki",
    mieszczące się w miejscowości Kaczy Dół, przy ulicy Batorego 120.
7. Usuniecie książki o `id` 12.
8. Wybierające wszystkich czytelników, którzy kiedykolwiek wypożyczyli jakąś książkę
    (na podstawie relacji wiele do wielu między książką, a czytelnikiem; p. punkt 5).
9. Dezaktywujące użytkownika o id 2 (ustaw wartość `is_active` na false dla tego użytkownika,
    załóż że użytkownik już istnieje w bazie).
10. Dodanie do tabeli `Readers` pola `date_of_birth` przechowującego datę urodzenia czytelnika.
    Pole może przyjmować wartość `null`.

Za każde zapytanie przysługuje pół punktu.


## Zadanie 4. (4 pkt)

Używając frameworka **Flask**, napisz stronę, która spełni następujące założenia:

1. Po wejściu metodą GET wyświetli pusty formularz, który będzie zawierał następujące pola:
    * `name`: imię,
    * `email`: email czytelnika.

2. Po wejściu metodą POST:
    * zweryfikuje poprawność danych 
        (wystarczy sprawdzić, czy imię nie jest puste i w czy w polu `email` znajduje się znak "@"),
    * zapisze te dane do bazy danych do tabeli `Readers` (tabela taka sama jak w zadaniu 3),
    * jeśli którakolwiek dana będzie błędna, zamiast zapisywania do bazy, wyświetli na stronie komunikat o błędzie.

Pamiętaj o poprawnym połączeniu do bazy danych i jego zamknięciu.

Rozwiązanie zapisz w pliku `answer4.py`.

## Zadanie 5. (5pkt)

Napisz w Pythonie klasę `EBook`. Klasa powinna spełniać następujące właściwości:
1. Dziedziczyć po klasie `Book` (zajrzyj do modułu `exam_lib`).
2. Mieć dodatkowe atrybuty: `size` (rozmiar w MB) i `registration_code` (kod do rejestracji).
    Kod rejestracyjny nie powinien być dostępny na zewnątrz (pamiętaj o konwencji nazw).
3. Mieć metodę `__init__`, która przyjmuje następujące dane: tytuł, autor, liczba stron, rozmiar i kod rejestracyjny.
    Tytuł, autor i liczba stron mają być przekazywane do metody `__init__` klasy nadrzędnej.
    Metoda `__init__` ma sprawdzać, czy podany kod rejestracyjny jest prawidłowy. Jeżeli jest  &ndash; to go nastawiać,
    jeżeli nie  &ndash; to kod ma być nastawiony na `None`.
    Kod jest poprawny, jeśli jest ciągiem znaków (`str`) składającym się z 16 cyfr.
4. Mieć metodę statyczną `check_code`. Powinna ona przyjmować jeden parametr (kod rejestracyjny)
    i zwracać wartość logiczną. `True`, jeśli kod jest poprawny, `False`, jeśli nie.
    Kod jest poprawny, jeśli jest ciągiem znaków (`str`) składającym się z 16 cyfr.
5. Mieć getter (`property`) i setter dla atrybutu `registration_code`.
    * getter powinien po prostu zwrócić wartość kodu rejestracyjnego.
    * setter powinien ustawić numer rejestracyjny tylko w przypadku, gdy numer ten jest prawidłowy.

Rozwiązanie zapisz w pliku `answer5.py`.
