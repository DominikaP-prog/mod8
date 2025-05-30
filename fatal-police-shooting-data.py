import pandas as pd
import matplotlib.pyplot as plt

# --- KROK 1: Wczytanie danych z Excela ---
interwencje = pd.read_excel('interwencje_policji/fatal-police-shootings-data.xlsx')

# --- KROK 2: Zestawienie liczby ofiar według rasy i oznak choroby psychicznej ---
grouped = interwencje.groupby(['race', 'signs_of_mental_illness']).size().unstack(fill_value=0)

# Dodanie kolumny z odsetkiem przypadków choroby psychicznej
grouped['odsetek_choroby'] = grouped.apply(lambda row: (row[True] / (row[True] + row[False])) * 100 
                                           if (row[True] + row[False]) > 0 else 0, axis=1)

# Posortowanie malejąco według odsetka
grouped = grouped.sort_values(by='odsetek_choroby', ascending=False)

print("\nOdsetek przypadków choroby psychicznej wg rasy:")
print(grouped[['odsetek_choroby']])
print("\nNajwyższy odsetek ma rasa:", grouped[['odsetek_choroby']].idxmax()[0])

# --- KROK 3: Dodanie dnia tygodnia i wykres ---
interwencje['date'] = pd.to_datetime(interwencje['date'], errors='coerce')  # konwersja dat
interwencje = interwencje.dropna(subset=['date'])  # usuń wiersze bez daty
interwencje['day_of_week'] = interwencje['date'].dt.day_name()

# Uporządkowanie dni tygodnia
days_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
interwencje_dni = interwencje['day_of_week'].value_counts().reindex(days_order)

# Wykres kolumnowy
plt.figure(figsize=(10, 6))
interwencje_dni.plot(kind='bar', color='skyblue')
plt.title('Liczba interwencji według dnia tygodnia')
plt.ylabel('Liczba interwencji')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# --- KROK 4: Interwencje na 1000 mieszkańców ---

# Wczytanie danych o populacji i skrótach stanów (tu zakładamy pliki CSV – dostosuj, jeśli masz Excel)
populacja = pd.read_csv('us_states_population.csv')  # kolumny: State, Population
skroty = pd.read_csv('us_state_abbreviations.csv')   # kolumny: State, Abbreviation

# Połączenie populacji ze skrótami stanów
populacja_z_skrotami = pd.merge(populacja, skroty, on='State')

# Zliczenie interwencji na stan
liczba_interwencji = interwencje['state'].value_counts().reset_index()
liczba_interwencji.columns = ['Abbreviation', 'Liczba_interwencji']

# Połączenie danych i obliczenie interwencji na 1000 mieszkańców
dane_polaczone = pd.merge(populacja_z_skrotami, liczba_interwencji, on='Abbreviation', how='left')
dane_polaczone['Liczba_interwencji'] = dane_polaczone['Liczba_interwencji'].fillna(0)
dane_polaczone['Interwencje_na_1000'] = (dane_polaczone['Liczba_interwencji'] / dane_polaczone['Population']) * 1000

# Posortowanie i wykres
dane_sorted = dane_polaczone.sort_values(by='Interwencje_na_1000', ascending=False)

plt.figure(figsize=(12, 8))
plt.barh(dane_sorted['State'], dane_sorted['Interwencje_na_1000'], color='lightcoral')
plt.xlabel('Interwencje na 1000 mieszkańców')
plt.title('Śmiertelne interwencje policyjne na 1000 mieszkańców – USA')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()