# Yksikkötestauksen kattavuusraportti

Kattavuusraportin voi löytää [Codecov](https://app.codecov.io/gh/sonicsasha/tiralabra):ista.

# Yksikkötestit
## Mitä testataan ja miten

Testit suoritetaan pytest:illä.

Aluksi testit katsovat, että käyttäjä ei pysty antamaan labyrintille parametreja, joilla labyrintin generointi olisi mahdotonta. Esimerkiksi testataan, että käyttäjä ei pysty luomaan labyrinttiä, jonka pituus tai leveys ovat parittomia lukuja, ja että käyttäjä ei syötä sellaista määrää askelia, joilla labyrintin läpäisy on mahdotonta.

Yksi puute testauksessa ja ohjelmassa on se, että se ei katso, onko vaadittujen askelten määrä liian suuri. Jos käyttäjä syöttää niin suuren määrän askelia, että labyrintin läpäiseminen on mahdotonta, se havaitaan vasta labyrintin generoinnin aikana.

Lisäksi testataan, että luotavat labyrintit ovat yhtenäisiä (eli että labyrintin alkuruudusta päästään jokaiseen labyrintin soluun) ja että alusta pääsee maaliin halutussa määrässä askelia. Nämä testit suoritetaan sekä syvyyshaulla että Primin algoritmilla luoduille algoritmeille. Labyrintit ovat kooltaan 11x11, ja haluttujen askelten määrä on 36.

Lisäksi testataan, että algoritmi generoi oikein 5x5 labyrintin, joka halutaan läpäistä 16 askeleessa. Tämä testataan sen takia, että se on hyvä ääritapaus algoritmille, sillä tällaisia labyrinttejä on vain kaksi.

## Testien suoritus

Testit voi suorittaa omalla koneella syöttämällä komentokehotteeseen komento 
`poetry run invoke test`

# Suorituskykytestit
## Yksikkötestauksen kattavuusraportti
Kattavuusraportin näkee alta:

[![codecov](https://codecov.io/gh/sonicsasha/tiralabra/branch/main/graph/badge.svg?token=KDR8Z7R8I1)](https://codecov.io/gh/sonicsasha/tiralabra)

## Mitä testataan
Koska ohjelman toiminta perustuu kahteen peräkkäin toimivaan algoritmiin (ensiksi polun luonti ja sen jälkeen itse labyrintti), joten testasin näiden toimintaa erikseen.
Suorituskykyä testataan niin, että ensiksi yritetään luoda satunnaista polkua 10001x10001-labyrinttiin eri määrällä haluttuja askelia. Tämän jälkeen luodaan erikokoisia labyrinttejä, missä polku lähdöstä maaliin on lyhin mahdollinen, jotta polunluontialgoritmilla olisi mahdollisimman pieni ja ennustettava vaikutus suoritusaikaan. Nämä testit suoritetaan sekä syvyyshaulla että Primin algoritmilla samoilla syötteillä.
Nämä testit voi suorittaa omalla koneella komennolla

`poetry run invoke performance-test`

## Syötteet (3.12.2022)
### Polunluontialgoritmi
| Leveys | Korkeus | Vaaditut askeleet |
|-------|--------|----------------|
| 10001 | 10001  | 20000          |
| 10001 | 10001  | 24000          |
| 10001 | 10001  | 28000          |
| 10001 | 10001  | 38000          |
| 10001 | 10001  | 48000          |
| 10001 | 10001  | 55000          |
| 10001 | 10001  | 60000          |
| 10001 | 10001  | 68000          |
| 10001 | 10001  | 76000          |
| 10001 | 10001  | 84000          |
| 10001 | 10001  | 92000          |
| 10001 | 10001  | 100000         |
| 10001 | 10001  | 140000         |
| 10001 | 10001  | 180000         |
| 10001 | 10001  | 220000         |
| 10001 | 10001  | 260000         |
| 10001 | 10001  | 300000         |
| 10001 | 10001  | 340000         |
| 10001 | 10001  | 380000         |
| 10001 | 10001  | 420000         |
| 10001 | 10001  | 460000         |
| 10001 | 10001  | 500000         |
| 10001 | 10001  | 620000         |
| 10001 | 10001  | 760000         |
| 10001 | 10001  | 880000         |

### Labyrintin luontialgoritmit
| Leveys | Korkeus | Vaaditut askeleet |
|-------|--------|----------------|
| 5     | 5      | 8              |
| 11    | 11     | 20             |
| 51    | 51     | 100            |
| 101   | 101    | 200            |
| 301   | 301    | 600            |
| 501   | 501    | 1000           |
| 1001  | 1001   | 2000           |
| 2001  | 2001   | 4000           |
| 5001  | 5001   | 10000          |
| 8001  | 8001   | 16000          |
| 10001 | 10001  | 20000          |

__HUOM! Tässä vaadittujen askelten määrä on aina leveys + korkeus - 2__

## Suorituskyktestien tulokset
Suorituskykytestien raportin voi lukea suoraan [täältä](/performance_report.xlsx)
### Polunluonti
| Leveys | Korkeus | Vaaditut askeleet | Suoritusaika (s)    |
|-------|--------|----------------|-------------------|
| 10001 | 10001  | 20000          | 0.253889799118042 |
| 10001 | 10001  | 24000          | 0.10419511795044  |
| 10001 | 10001  | 28000          | 0.184114933013916 |
| 10001 | 10001  | 38000          | 0.690302848815918 |
| 10001 | 10001  | 48000          | 0.269785881042481 |
| 10001 | 10001  | 55000          | 0.327528953552246 |
| 10001 | 10001  | 60000          | 0.503434419631958 |
| 10001 | 10001  | 68000          | 0.297757387161255 |
| 10001 | 10001  | 76000          | 0.237871170043945 |
| 10001 | 10001  | 84000          | 0.827225208282471 |
| 10001 | 10001  | 92000          | 0.48801326751709  |
| 10001 | 10001  | 100000         | 0.551369905471802 |
| 10001 | 10001  | 140000         | 0.790416240692139 |
| 10001 | 10001  | 180000         | 0.760104894638062 |
| 10001 | 10001  | 220000         | 1.23835277557373  |
| 10001 | 10001  | 260000         | 1.09469056129456  |
| 10001 | 10001  | 300000         | 1.66305494308472  |
| 10001 | 10001  | 340000         | 1.5538444519043   |
| 10001 | 10001  | 380000         | 1.87185740470886  |
| 10001 | 10001  | 420000         | 1.72506046295166  |
| 10001 | 10001  | 460000         | 1.99029111862183  |
| 10001 | 10001  | 500000         | 2.23190021514893  |
| 10001 | 10001  | 620000         | 2.56474208831787  |
| 10001 | 10001  | 760000         | 3.28734374046326  |
| 10001 | 10001  | 880000         | 3.87917375564575  |

![Polunluontialgoritmin suorituskykytestien kuvaaja](/docs/img/path.png)

### Syvyyshaku
| Leveys | Korkeus | Vaaditut askeleet | Suoritusaika (s)       |
|-------|--------|----------------|----------------------|
| 5     | 5      | 8              | 7.46250152587891E-05 |
| 11    | 11     | 20             | 0.000230550765991211 |
| 51    | 51     | 100            | 0.00431370735168457  |
| 101   | 101    | 200            | 0.017122745513916    |
| 301   | 301    | 600            | 0.156205654144287    |
| 501   | 501    | 1000           | 0.446015119552612    |
| 1001  | 1001   | 2000           | 1.77980017662048     |
| 2001  | 2001   | 4000           | 7.26179957389832     |
| 5001  | 5001   | 10000          | 51.7462909221649     |
| 8001  | 8001   | 16000          | 156.648549556732     |
| 10001 | 10001  | 20000          | 278.019733428955     |

![Syvyyshaulla toimivan labyrintin luontialgoritmin suorituskykytestien kuvaaja](/docs/img/dfs.png)

### Primin algoritmi
| Leveys | Korkeus | Vaaditut askeleet | Suoritusaika (s)       |
|-------|--------|----------------|----------------------|
| 5     | 5      | 8              | 7.51018524169922E-05 |
| 11    | 11     | 20             | 0.000236034393310547 |
| 51    | 51     | 100            | 0.00507545471191406  |
| 101   | 101    | 200            | 0.0175867080688477   |
| 301   | 301    | 600            | 0.160141706466675    |
| 501   | 501    | 1000           | 0.478475570678711    |
| 1001  | 1001   | 2000           | 1.95156097412109     |
| 2001  | 2001   | 4000           | 7.93495011329651     |
| 5001  | 5001   | 10000          | 56.1203625202179     |
| 8001  | 8001   | 16000          | 147.457976341248     |
| 10001 | 10001  | 20000          | 239.375643491745     |

![Primin algoritmilla toimivan labyrintin luontialgoritmin suorituskykytestien kuvaaja](/docs/img/prim.png)