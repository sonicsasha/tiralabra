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
