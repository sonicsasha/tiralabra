# Käyttöohje

## Riippuvuuksien asennus

Ohjelman riippuvuudet saa asennettua komennolla
```console
poetry install
```

[Poetry](https://python-poetry.org/) täytyy olla asennettuna

## Ohjelman käynnistäminen

Siirry ensiksi Poetry virtuaaliympäristöön komennolla
```console
poetry shell
```

Tämän jälkeen ohjelman saa käynnistettyä komennolla
```console
invoke start
```

Vaihtoehtoisesti voit käynnistää ohjelman yhdellä komennolla suorittamalla
```console
poetry run invoke start
```

Kun ohjelma on käynnistynyt, sen voi lopettaa jättämällä jonkin syötteen tyhjäksi.

Tämä ohjelma on kehitetty Pythonin versiolla 3.10.3

## Yksikkötestit

Yksikkötestit voi suorittaa komennolla 
```console
poetry run invoke test
```

Kattavuusraportin saa luotua suorittamalla
```console
poetry run invoke coverage
```

## Suorituskykytestit

Suorituskykytestit voi suorittaa komennolla 
```console
poetry run invoke performance-test
```

Koska kyseessä on suorituskykytesti, voi suorituksessa kestää jonkin aikaa. Suorituskykytestien päätyttyä tulokset tallennetaan projektin juuressa olevaan Excel-tiedostoon `performance_report.xlsx`.

## Koodin laadun hallinta

Koodin automaattisen formatoinnin voi suorittaa komennolla
```console
poetry run invoke format
```
Koodin formatoimiseen käytetään [Black-kirjastoa](https://github.com/psf/black)

Koodin automaattisen laaduntarkistuksen voi tehdä komennolla
```console
poetry run invoke lint
```