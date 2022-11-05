Tällä viikolla olen suunnitellut ohjelmaa, miettinyt mitä algoritmeja käytän sekä yleisestikin alustanut projektin. Kaiken kaikkiaan arvioisin, että näihin meni noin 6 tuntia, vaikkakin suunnitteluun ja ideointiin meni enemmänkin.

Ohjelma on edistynyt toistaiseksi hyvin. Tein jo yksinkertaisen pygame:lla toimivan labyrintin visualisoijan. Muuten olen jo saanut yleisesti hyvän käsityksen siitä, mitä tulen projektissani tekemään.

Tällä viikolla opin paljon uusia juttuja labyrintin luomiseen liittyvistä algoritmeista, varsinkin sen, minkälaisia menetelmiä labyrinttien luomiseen on ja miten ne eroavat toisistaan. Opin myös menetelmiä satunnaisten polkujen generoimiseen.

Seuraavaksi aion kirjoittaa algoritmin, joka generoi satunnaisen riittävän pituisen reitin vasemmasta alakulmasta oikeaan yläkulmaan, ja toivottavasti jos aika riittää niin voin soveltaa jo ainakin yhtä labyrintin generoimiseen tarkoitettua algoritmia.

UPDATE 4.11

Sain kirjoitettua ohjelman, joka luo satunnaisen pyydetyn mittaisen polun vasemmasta alakulmasta oikeaan yläkulmaan. Se toimii muuten hyvin, mutta ensinnäkin se toimii rekursiolla, joten sille ei voi antaa erityisen suuria syötteitä. Mietin että onko olemassa mitään helppoa tapaa toteuttaa kyseinen algoritmi ilman rekursiota. Se siis toimii tällä hetkellä käytännössä satunnaisella syvyyshaulla.

Lisäksi jäin jumiin sellaiseen pieneen kohtaan, että miten voidaan laskea pisimmän mahdollisen reitin pituus vasemmasta alakulmasta oikeaan yläkulmaan. En nimittäin oikein keksi, miten sen voisi tehdä ilman että kokeilee eri arvoja ja katsoo, luodaanko reitti.

Lisäksi jäi mietityttämään, että saako/kannattaako käyttää Pythonin random-kirjaston satunnaislukugeneraattoreita vai pitääkö ne kehittää itse?

Algoritmin kirjoittamiseen meni noin 4-5 tuntia.

UPDATE 5.11

Sain tänään kirjoitettua algoritmin, joka luo labyrintin luodun polun ympärille satunnaisella syvyyshaulla. Siihen meni noin puolitoista tuntia. 

Minun suurimmat huolenaiheet tällä hetkellä ovat seuraavat:
* Miten saisin kirjoitettua polun generoinnin niin, että se ei käyttäisi rekursiota. Koska tällä hetkellä siinä tarvitaan peruutusta.

* Onko aiheeni tällä hetkellä riittävän laaja arvosanaa 5 varten vai kannattaako minun tehdä vielä jotain muutakin? Tiedän, että en ole vielä kirjoittanut testejä tai muuta dokumentaatiota, mutta olen jo vähän huolissani siitä kuinka nopeasti olen edennyt :DDD

Seuraavaksi voisin jo alkaa kirjoittamaan testejä, jotta en vahingossa kirjoittaisi valmista koodia ja vasta loppypäädyssä tajua, että olen tehnyt jonkun pahan virheen.