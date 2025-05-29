import pandas as pd

# Dane o albumach z dodatkową kolumną 'Max Poz' (np. pozycja w rankingu)
data = [
    {"Tytuł": "Greatest Hits", "Artysta": "Queen", "Rok": 1981, "Max Poz": 1},
    {"Tytuł": "Gold: Greatest Hits", "Artysta": "ABBA", "Rok": 1992, "Max Poz": 2},
    {"Tytuł": "Sgt. Pepper’s Lonely Hearts Club Band", "Artysta": "The Beatles", "Rok": 1967, "Max Poz": 3},
    {"Tytuł": "21", "Artysta": "Adele", "Rok": 2011, "Max Poz": 4},
    {"Tytuł": "(What’s The Story) Morning Glory?", "Artysta": "Oasis", "Rok": 1995, "Max Poz": 5},
    {"Tytuł": "Thriller", "Artysta": "Michael Jackson", "Rok": 1982, "Max Poz": 6},
    {"Tytuł": "The Dark Side of the Moon", "Artysta": "Pink Floyd", "Rok": 1973, "Max Poz": 7},
    {"Tytuł": "Brothers in Arms", "Artysta": "Dire Straits", "Rok": 1985, "Max Poz": 8},
    {"Tytuł": "Bad", "Artysta": "Michael Jackson", "Rok": 1987, "Max Poz": 9},
    {"Tytuł": "Greatest Hits II", "Artysta": "Queen", "Rok": 1991, "Max Poz": 10}
]

# Tworzymy DataFrame
df = pd.DataFrame(data)

# ZADANIE 1: Zamień nazwy kolumn na ['TYTUŁ','ARTYSTA','ROK','MAX POZ']
df.columns = ['TYTUŁ', 'ARTYSTA', 'ROK', 'MAX POZ']

# ZADANIE 2: Ilu pojedynczych artystów znajduje się na liście?
unikalni_artysci = df['ARTYSTA'].nunique()
print(f"Ilu unikalnych artystów: {unikalni_artysci}")

# ZADANIE 3: Które zespoły pojawiają się najczęściej?
print("\nNajczęściej występujący artyści:")
print(df['ARTYSTA'].value_counts())

# ZADANIE 4: Zmień nagłówki kolumn (pierwsza litera duża, reszta małe)
df.columns = [col.capitalize() for col in df.columns]

# ZADANIE 5: Wyrzuć kolumnę 'Max poz'
df = df.drop(columns=['Max poz'])

# ZADANIE 6: W którym roku wyszło najwięcej albumów?
najpopularniejszy_rok = df['Rok'].value_counts().idxmax()
print(f"\nRok z największą liczbą albumów: {najpopularniejszy_rok}")

# ZADANIE 7: Ile albumów z lat 1960-1990?
albumy_60_90 = df[(df['Rok'] >= 1960) & (df['Rok'] <= 1990)]
print(f"\nLiczba albumów z lat 1960–1990: {len(albumy_60_90)}")

# ZADANIE 8: Najmłodszy album
najmlodszy_rok = df['Rok'].max()
print(f"\nNajmłodszy album pochodzi z roku: {najmlodszy_rok}")

# ZADANIE 9: Najwcześniejszy album każdego artysty
najwczesniejsze_albumy = df.sort_values('Rok').drop_duplicates(subset='Artysta', keep='first')

# ZADANIE 10: Zapisz do pliku CSV
najwczesniejsze_albumy.to_csv("najwczesniejsze_albumy.csv", index=False)
print("\nZapisano plik: najwczesniejsze_albumy.csv")
