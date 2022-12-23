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

Tarkastellaan aluksi erikseen kaikkia kolmea algoritmia. Kun luodaan satunnaista lyhintä reittiä, niin siinä on kaksi 

Kun luodaan sivuaskelia, niin on vain [yksi tilanne](/src/generators/path_generator.py), jossa käydään läpi listan alkioita. Tässä käydään läpi listan Labyrinth.broken_walls() alkioita, joita ei voi olla enempää kuin labyrintin alkioita. Rajaavin tekijä on kuitenkin vaadittujen askelten määrä, joka ei voi mitenkään olla suurempi kuin wh. Labyrintin koolla ei ole itsessään siis paljon vaikutusta algoritmin suoritusaikaan, se vain antaa ala- sekä ylärajan vaadittujen askelten määrään. Ainoa muuttuja joka vaikuttaa suoritusaikaan on siis n, eli algoritmin aikavaativuus on O(n). Myös suorituskykytestit vahvistavat tämän päätelmän, sillä polunluontialgoritmin suorituskykytestien muodostama kuvaaja on suora.

Tarkastellaan seuraavaksi molempia labyrintin luontialgoritmeja. Syvyyshaku on tunnetusti aikavaativuudeltaan O(|V|+|E|), missä V on verkon solmut ja E on verkon kaaret. Labyrinth-luokassa kuitenkin kaikki tieto tallennetaan yhteen listaan, eli siis sekä solmut että kaaret ovat muuttujassa, jonka tilavaativuus on O(wh). Siispä myös algoritmin aikavaativuus on O(wh). 

Ohjelman käyttämä satunnaisen Primin algoritmi eroaa oikeasta Primin algoritmista niin, että siinä käytetään keon sijaan listaa ja kaikki tieto tallennetaan yhteen matriisiin, eli ei ole erikseen tietoa solmuista ja kaarista. Tarkastelemalla algoritmia kuitenkin käsin huomataan, että ainoa tilanne jossa tietoa "käydään läpi" on while-silmukka, joka käy listan walls_to_break alkiot läpi. Ja koska kyseiseen listaan lisätään alkioita vain, kun jokin alkio on seinä ja samalla seiniä "hajotetaan", niin voidaan päätellä, että algoritmin aikavaativuus on O(wh).

# Työn puutteet ja parannukset
TODO

# Lähteet
[Maze generation algorithm](https://en.wikipedia.org/wiki/Maze_generation_algorithm), Wikipedia

[Random path generation algorithm with defined path size](https://stackoverflow.com/questions/58161102/random-path-generation-algorithm-with-defined-path-size), Stack Overflow