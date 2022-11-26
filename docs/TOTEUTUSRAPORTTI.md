# Ohjelman yleisrakenne
Algoritmi toimii Labyrint-luokkana, jolle annetaan parametrit alustuksessa. Labyrintille määritellään korkeus ja leveys. Tämän jälkeen labyrintille suoritetaan operaatioita luokan metodeina. Metodit ovat seuraavat:
- generate_random_shortest_path(), joka luo satunnaisen polun suoraan alusta loppuun.
- generate_sidesteps(), joka luo sivuaskeleet aikaisemmin tehdylle polulle. Nämä kaksi tullaan todennäköisesti yhdistämään yhdeksi funktioksi.
- generate_maze_around_path_dfs(), joka luo satunnaisella syvyyshaulla labyrintin luodun polun ympärille.
- generate_maze_around_path_prim(), joka luo satunnaisella Primin algoritmilla labyrintin luodun polun ympärille.

Nämä vielä refaktoroidaan niin, että yhden komennon suorittaminen riittää kokonaisen labyrintin luomiseen.

# Aika- ja tilavaativuudet
Määritellään, että w on labyrintin leveys, h on labyrintin korkeus ja n on haluttujen askelten määrä.
Kaikki labyrinttiin liittyvät operaatiot tehdään yhteen muuttujaan (tässä tapauksessa Labyrinth.labyrinth_matrix). Lisäksi labyrintin generoimiseen käytetään apumuuttujia Labyrinth.broken_walls ja Labyrinth.walls_to_break, jotka ovat listoja ja joiden pituus ei voi olla suurempi kuin labyrinttimatriisin solujen määrä. Lisäksi tallennetun tiedon määrä on sama riippumatta haluttujen askelten määrästä, joten voidaan päätellä että tilavaativuus on O(wh).

Tarkastellaan aluksi erikseen kaikkia kolmea algoritmia. Kun luodaan sivuaskelia, niin ainoa tilanne jossa käydään läpi listan alkioita on silloin, kun luodaan sivuaskelia. Tässä käydään läpi listan Labyrinth.broken_walls() alkioita, joita ei voi olla enempää kuin labyrintin alkioita. Pahin tilanne on se, jossa generoitava polku on niin pitkä, että sille ei voida muodostaa haarautumia. Tällöin algoritmin aikavaativuus on O(wh). Algoritmissa käytetään kuitenkin valmista funktiota random.shuffle(), jonka aikavaativuutta en tunne. Suorituskykytestien mukaan se ei kuitenkaan ole ainakaan O((wh)^2) luokkaa, joten se on joko O(wh) tai O(wh log(wh)). Suorituskykytesteissä muodostetussa kuvaajassa kulmakerroin kyllä nousee hieman, kun datan määrä nousee, joten arvioisin itse, että algoritmin aikavaativuus on O(wh log(wh)).

Tarkastellaan molempia labyrintin luontialgoritmeja. Syvyyshaku on tunnetusti aikavaativuudeltaan O(|V|+|E|), missä V on verkon solmut ja E on verkon kaaret. Labyrinth-luokassa kuitenkin kaikki tieto tallennetaan yhteen listaan, eli siis sekä solmut että kaaret ovat muuttujassa, jonka tilavaativuus on O(wh). Siispä myös algoritmin aikavaativuus on O(wh). 

Ohjelman käyttämä satunnaisen Primin algoritmi eroaa oikeasta Primin algoritmista niin, että siinä käytetään keon sijaan listaa ja kaikki tieto tallennetaan yhteen matriisiin, eli ei ole erikseen tietoa solmuista ja kaarista. Tarkastelemalla algoritmia kuitenkin käsin huomataan, että ainoa tilanne jossa tietoa "käydään läpi" on while-silmukka, joka käy listan walls_to_break alkiot läpi. Ja koska kyseiseen listaan lisätään alkioita vain, kun jokin alkio on seinä ja samalla seiniä "hajotetaan", niin voidaan päätellä, että algoritmin aikavaativuus on O(wh).

# Työn puutteet ja parannukset
TODO

# Lähteet
TODO