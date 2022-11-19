Tämä viikko on ollut sen verran kiireinen, että en ehtinyt tehdä ihan kaikkea mitä halusin. Ehdin kuitenkin kirjoittaa paremman käyttöliittymän, jotta algoritmien tulosten vertailu olisi helpompaa, ja jotta käyttäjä pystyisi näkemään mistä polusta algoritmi generoi polun.

Tämä on siinä mielessä erittäin hyödyllinen ominaisuus, että näin nyt että polunluontialgoritmini suosii vahvasti labyrintin keskiosaa, mikä tarkoittaa sitä että labyrintin voisi läpäistä melko helposti pyrkimällä aina kulkemaan koilliseen. Ja vaikka labyrinttiin yrittäisikin lisätä sivuaskelia, niin sivuaskeleet yleensä kulkevat lähellä polkua.

Lisäksi huomasin, että polunluontialgoritmini ei oikein toimi yhdessä Primin algoritmin kanssa, sillä varsinkin suurilla syötteillä polku eroaa selvästi muista poluista, jolloin pelaajan on melko helppo päätellä, minne hän haluaa mennä.

Pienemmillä syötteillä nämä eivät ole niinkään vakavia ongelmia, mutta jos halutaan esimerkiksi luoda 1001x1001 labyrintti, niin silloin täytyisi jo jollakin tavalla muokata algoritmia niin, että siinä olisi enemmän satunnaisuutta. Murehdin sitä kuitenkin enemmän sitten, kun minulla on enemmän aikaa.

Opin jonkin verran enemmän pygame:n toiminnasta ja erityisesti siitä, miten napit on järkevä toteuttaa pygame:ssa. 

Lisäksi aloin tällä viikolla kirjoittamaan testausdokumenttia. Sain siihen jo kirjoitettua yksikkötestien tilanteen, yritän seuraavaksi saada kirjoitettua automatisoidut suorituskykytestit ja kirjoittaa siitä testausdokumenttiin. Lisäksi minun olisi hyvä käydä koodia läpi ja optimoida sekä selkeyttää sitä.
