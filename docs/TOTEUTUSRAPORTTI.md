# Ohjelman yleisrakenne
Algoritmit on toteutettu niin, että jokaisella algoritmilla on oma luokka, jolle annetaan Labyrinth-luokan objekti, johon algoritmi sitten tekee muutokset. Labyrintille määritellään korkeus ja leveys. Tämän jälkeen labyrintille suoritetaan operaatioita eri algoritmien luokkien metodeina. Metodit ovat seuraavat:
- PathGenerator.generate_random_shortest_path(), joka luo satunnaisen polun alusta loppuun niin, että se ei tee sivuaskelia mihinkään suuntaan.
- PathGenerator.generate_sidesteps(), joka luo sivuaskeleet aikaisemmin tehdylle polulle.
- MazeGeneratorDFS().generate_maze_around_path(), joka luo satunnaisella syvyyshaulla labyrintin luodun polun ympärille.
- MazeGeneratorPrim().generate_maze_around_path(), joka luo satunnaisella Primin algoritmilla labyrintin luodun polun ympärille.



# Aika- ja tilavaativuudet
Vaikka tässä onkin tarkoitus tarkastella aikavaativuuksia käyttäen pseudokoodia, niin koska oma toteutus eroaa aika paljon oletetusta, niin teen aikavaativuuden analyysin oikealle koodille. Laitan kuitenkin tarvittaessa myös linkit niihin kohtiin koodia, joita käytän perusteluina.

Määritellään, että w on labyrintin leveys, h on labyrintin korkeus ja n on haluttujen askelten määrä.
Kaikki labyrinttiin liittyvät operaatiot tehdään yhteen muuttujaan (tässä tapauksessa Labyrinth.labyrinth_matrix). Lisäksi labyrintin generoimiseen käytetään apumuuttujia Labyrinth.broken_walls ja Labyrinth.walls_to_break, jotka ovat listoja ja joiden pituus ei voi olla suurempi kuin labyrinttimatriisin solujen määrä. Näihin listoihin lisätään matriisin soluja ja sama solu ei voi esiintyä kahdesti. Lisäksi tallennetun tiedon määrä on sama riippumatta haluttujen askelten määrästä, joten voidaan päätellä että tilavaativuus on O(wh).

Tarkastellaan aluksi erikseen kaikkia kolmea algoritmia. Kun luodaan satunnaista lyhintä reittiä, niin siinä ainoa lista on Manhattan-polku alusta loppuun, jonka [pituus on noin (w + h) / 2](/src/generators/path_generator.py#L24). Tätä listaa käydään läpi kolme kertaa: [Kun listaa sekoitetaan satunnaisesti](/src/generators/path_generator.py#L27), [kun katsotaan että kuljetaanko samaan suuntaan kaksi kertaa peräkkäin](/src/generators/path_generator.py#L67) ja [kun polku kirjoitetaan matriisiin](/src/generators/path_generator.py#L53). Listan sekoittaminen on [O(n) operaatio](https://hg.python.org/cpython/file/2e8b28dbc395/Lib/random.py#l276). Siispä nopeimman reitin generoinnin aikavaativuus on O(w + h).

Kun luodaan sivuaskelia, niin siinä käydään läpi listan Labyrinth.broken_walls() alkioita, joita ei voi olla enempää kuin labyrintin alkioita. [While-silmukan](/src/generators/path_generator.py#L82) suorituskertojen määrän määrää kuitenkin sidesteps_to_do, joka ei voi mitenkään olla suurempi kuin wh. Kuitenkin jos esimerkiksi sidesteps_to_do on 0, niin silmukkaa ei suoriteta kertaakaan. Labyrintin koolla ei ole itsessään siis paljon vaikutusta algoritmin suoritusaikaan, se vain antaa ala- sekä ylärajan vaadittujen askelten määrään. Ainoa muuttuja joka vaikuttaa suoritusaikaan on siis n, eli algoritmin aikavaativuus on O(n). Myös suorituskykytestit vahvistavat tämän päätelmän, sillä polunluontialgoritmin suorituskykytestien muodostama kuvaaja on suora, kun w ja h pysyvät vakiona.

Eli tästä voidaan todeta, että polunluontialgoritmin aikavaativuus on yhteensä O(w + h + n).

Tarkastellaan seuraavaksi molempia labyrintin luontialgoritmeja. Syvyyshaku on tunnetusti aikavaativuudeltaan O(|V|+|E|), missä V on verkon solmut ja E on verkon kaaret. Labyrinth-luokassa kuitenkin kaikki tieto tallennetaan yhteen listaan, eli siis sekä solmut että kaaret ovat muuttujassa, jonka tilavaativuus on O(wh). Siispä myös algoritmin aikavaativuus on O(wh). 

Ohjelman käyttämä satunnaisen Primin algoritmi eroaa oikeasta Primin algoritmista niin, että siinä käytetään keon sijaan listaa ja kaikki tieto tallennetaan yhteen matriisiin, eli ei ole erikseen tietoa solmuista ja kaarista. Tarkastelemalla algoritmia kuitenkin käsin huomataan, että ainoa tilanne jossa tietoa "käydään läpi" on while-silmukka, joka käy listan walls_to_break alkiot läpi. Ja koska kyseiseen listaan lisätään alkioita vain, kun jokin alkio on seinä ja samalla seiniä "hajotetaan", niin voidaan päätellä, että algoritmin aikavaativuus on O(wh).

# Algoritmien verailu
Alla esimerkki saaduista labyrinteistä syötteellä leveys 101, korkeus 51 ja vaaditut askeleet 260.
### Primin algoritmi
![Primin algoritmi](/docs/img/prim.png)
### Syvyyshaku
![Syvyyshaku](/docs/img/dfs.png)

Näkyvin ero polkujen pituuksilla. Primin algoritmilla luodussa labyrintissä on paljon enemmän lyhyitä reittejä ja paljon enemmän umpikujia, minkä seurauksena myös reitin haarautuvuus on paljon suurempi. Satunnaisella syvyyshaulla luodussa labyrintissä on kuitenkin paljon enemmän pitkiä polkuja ja vähemmän umpikujia. Haarautuvuus on paljon pienempi. Kun kulkee alusta loppuun oikeaa reittiä pitkin, niin törmää vain kahteen haarautumaan.

Lisäksi mielenkiintoinen ero algoritmien välillä on labyrintin visuaalinen ilme. Koska syvyyshaulla tulee paljon pidemmät ja suoremmat polut, niin se näyttää paljon miellyttävämmältä ja muistuttaa labyrinttiä, kun taas Primin algoritmi luo labyrintin, joka muistuttaa enemmän näkötestiä.

# Työn puutteet ja parannukset
Luulen, että suurin puute tässä työssä on polunluontialgoritmi. Koska se perustuu painottamattomaan satunnaisuuteen, niin on hyvin korkea todennäköisyys, että se kulkee koko ajan halkaisijaviivan ympärillä. Primin algoritmilla tuotetussa labyrintissä melko pienilläkin määrällä askelia pystyy jo selkeästi erottamaan oikean polun muusta labyrintistä. Tämä on kuitenkin aika mielenkiintoinen ero algoritmien välillä. Primin algoritmilla oikean polun voi aika selkeästi erottaa, mutta syvyyshaulla tuotetusta algoritmista sen erottaminen on vaikeampaa, vaikkakin siltikin mahdollista. 

Työtä voisi siis parantaa niin, että polunluontialgoritmin joko tekee kokonaan uudelleen tai sitten lisää siihen sellaisia muutoksia että se voisi myös suosia yläkautta ja alakautta menemistä. Kun aloin tekemään tätä työtä, niin tein polunluontialgoritmin niin, että se valitsi aina satunnaisen suunnan mihin kulkea ja se tekisi sivuaskelia niin, että sivuaskeleet jakautuisivat suurin piirtein tasaisesti koko reitille. Tässä oli kuitenkin sellainen ongelma, että tuli tilanteita, joissa labyrintti kulki vahingossa itseensä ja sen oli pakko tehdä sivuaskel. Jos kuitenkin tehtäviä sivuaskelia ei ollut enää jäljellä, niin tämä tarkoittaisi sitä että polku ei ollut enää validi ja että se oli pidempi kuin mitä sen pitäisi olla. Rekursio auttoi tähän ongelmaan, sillä tuollaisessa tilanteessa pystyi vaan palaamaan takaisin ja kokeilla tehdä jokin toinen reitti. Rekursio rajoitti kuitenkin työtä niin, että se ei toiminut enää suurilla syötteillä. Jos lähtisin jatkokehittämään tätä algoritmia, niin korjaisin tämän ongelman ensiksi. En kuitenkaan keksinyt parempaa keinoa tämän kurssin aikana. :/ 

Lisäksi satunnaisella syvyyshaulla tehdyssä labyrintissä on nyt se ongelma, että kun kulkee oikeaa polkua pitkin alusta loppuun, niin vastaan tulee yleensä vain kaksi haarautumaa, eli syvyyshaulla luodut labyrintit ovat nyt turhankin helppoja. Tämän voisi kokeilla korjata esimerkiksi niin, että yksittäiselle syvyyshaulle määrittelee jonkin rajan syvyydelle, mutta en ehtinyt sitä miettiä tämän kurssin aikana.

# Lähteet
[Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm), Wikipedia

[Random path generation algorithm with defined path size](https://stackoverflow.com/questions/58161102/random-path-generation-algorithm-with-defined-path-size), Stack Overflow