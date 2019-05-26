# Program do analizy danych - zadanie od Profil Software

Program analizuje dane dot. egzaminów maturalnych w Polsce w latach 2010-2018 z podziałem na województwa

## Instalacja

Wystarczy sklonować repo:

```bash
git clone https://github.com/demluk/zadanieProfil.git
```

## Jak używać

Należy z linii poleceń przejść do folderu w którym znajdują się pobrane pliki i użyć komendy 
```bash
python analyser.py 
```
Samo to jednak nie wystarczy, trzeba jeszcze wybrać tryb analizy i podać potrzebne argumenty.
Lista argumentów: 
```bash
-voivodeship/-v
```
(dla trybów median,percentage,comparison) 
```bash
-year/-y, 
```
(dla trybów median, best)
```bash
-voivodeship2/-v2, 
```
(dla trybu comparison) 


### Tryby analizy:

#### Median (średnia)
Tryb używany do wyznaczenia średniej ilości przystępujących do egzaminu z wybranego przez nas województwa w latach od 2010 do podanego przez nas roku.

Przykład użycia:

```bash
python analyser.py mode=median -v Pomorskie -y 2015 
```

#### Percentage (odsetek zdających)
Tryb używany do wyznaczenia procenta przystępujących którzy zaliczyli egzamin dla wybranego przez nas województwa na przestrzeni lat 2010 - 2018.

Przykład użycia:

```bash
python analyser.py mode=percentage -v Lubuskie
```

#### Best (najlepsze województwo)
Tryb używany do wyznaczenia województwa o najwyższym odsetku zaliczonych egzaminów dla podanego przez nas roku.

Przykład użycia:

```bash
python analyser.py mode=best -y 2011
```
#### Regression (pogorszenie wyników)
Tryb używany do wyznaczenia województw, które zanotowały spadek zdawalności w kolejnym roku dla całości zbioru danych.

Przykład użycia:

```bash
python analyser.py mode=regression
```

#### Comparison (porównanie wyników)
Tryb używany do wyznaczenia województwa o wyższej zdawalności spośród dwóch przez nas podanych dla wszystkich dostępnych roczników.

Przykład użycia:

```bash
python analyser.py mode=regression
```

### Podział dla płci

Dla każdego z trybów możemy użyć argumentu

```bash
-f
```
lub
```bash
-m
```
aby zawęzić wyniki do płci żeńskiej (f) lub męskiej (m)

na przykład

```bash
python analyser.py mode=percentage -v Lubuskie -f
```
(wyznaczenie procentowej zdawalności kobiet w województwie Lubuskim)


## Notka końcowa

Niestety nie zdążyłem zrobić testów jednostkowych.

Nie miałem też pomysłu jak zrealizować to w sposób obiektowy, ale bardzo chętnie nauczyłbym się tego na stażu :)