# Tiralabra labyrinttigeneraattori

## Kielet
Tässä työssä pääkielenä käytetään Pythonia. Vertaisarvioinnin pystyy suorittamaan C#:lla. Dokumentaatiotiedostoissa ja ohjelman käyttöliittymässä käytetään suomea. Ohjelmakoodissa, testauksessa sekä koodin sisäisessä dokumentaatiossa käytetään englantia.

## Projektin tavoite
Tavoitteena on kirjoittaa algoritmi, jolle syötetään jonkin labyrintin leveys, korkeus sekä kuinka monta askelta tarvitaan labyrintin ratkaisemiseen. Ohjelma tulostaa satunnaisen labyrintin, jonka pystyy ratkaisemaan annetussa määrässä askelia.

Koska projektin laajuus on suhteellisen pieni, niin labyrintin generoiminen tehdään kahdella eri algoritmilla, ja näitä tuloksia verrataan.

Projektissa käytetään tietorakenteina listoja sekä mahdollisesti sanakirjaa. Listaa käytetään labyrintin kuvaamiseen matriisina.

## Käytetyt algoritmit
Labyrintti luodaan niin, että aluksi generoidaan halutun mittainen polku alusta loppuun. Tähän käytetään itse tekemää, melko yksinkertaista algoritmia. Labyrintin generoimiseen käytetään satunnaista Kruskalin algoritmia (randomized Kruskal's algorithm) sekä satunnaista syvyyssuuntaista läpikäyntiä (randomized depth-first search). Valitsit nämä algoritmit, sillä ne ovat toteutukseltaan erilaisia ja ne myös tuottavat erilaisia labyrinttejä.
