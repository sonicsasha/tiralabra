9.11.2022

Tänään pääosin dokumentoin koodia sekä kirjoitin testejä algoritmiä varten. Algoritmeihin liittyen en oppinut niinkään paljon mitään uutta, mutta ainakin Codecovista sekä testien kirjoittamisesta opin jonkin verran uutta, esimerkiksi miten Codecovin saa kunnolla integroitua GitHub Actioneihin. Lisäksi opin jonkin verran yksityiskohtia pytestin sekä coveragen toiminnasta, sillä niitä käsiteltiin aikaisemmin aika pintapuolisesti.

10.11.2022

Tänään aluksi tein koodista siistimpää, lisäsin dokumentaatiota sekä kommentteja. Otin myös käyttöön black:in (koodin siistimistyökalu, joka on vaihtoehto autopep8:lle) sekä pylint:in. Minulla alkaa siis olla toiminnallinen perusta jo aika hyvin kasassa.

Kirjoitin myös uudelleen polunluontialgoritmin, jotta se ei käyttäisi rekursiota. Jouduin jonkin aikaa miettimään, että miten toteuttaisin sen, mutta sain inspiraatiota [täältä](https://stackoverflow.com/questions/58161102/random-path-generation-algorithm-with-defined-path-size). Itse algoritmin kirjoittaminen ei ollut hankalaa, mutta hankaluuksia tuottivat pienet ongelmat, joiden tapahtumisen todennäköisyys oli pieni, mutta silti mahdollinen. Esimerkiksi jos polku vasemmasta alakulmasta oikeaan yläkulmaan on vain yhtä zigzag:ia, niin sivuaskelten luominen on mahdotonta. Sain siihen kuitenkin loppujen lopuksi keksittyä ratkaisun.

Kaiken kaikkiaan olen tyytyväinen tämän projektin nykyiseen vaiheeseen. Kaikki perusasiat olen jo saanut toimimaan, ja algoritmi toimii melko nopeasti (1001x1001 labyrintti noin kahdessa sekunnissa).

Ehkä vielä yksi asia joka mietityttää hieman on se, että mitä labyrintin ominaisuuksia on tärkeä testata? Testaan tällä hetkellä automaattisilla testeillä sen, että labyrintti on yhtenäinen ja että alusta loppuun pääsee halutussa määrässä askelia.

Seuraavaksi alan joko kirjoittamaan toista labyrintin luontialgoritmia tai sitten yritän vain siistiä koodia ja lisätä kommentteja, jotta koodi olisi mahdollisimman ymmärrettävää. Katson fiiliksen mukaan.
