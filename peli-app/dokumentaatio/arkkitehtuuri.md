# Arkkitehtuurikuvaus

## Käyttöliittymä

Käyttöliittymässä on kolme näkymää. 

- Aloitus
- Peli
- Pisteytys
- Lopetus

Jokainen on oma luokkansa ja enintään kaksi näkynmää ovat yhtä aikaa käytössä. Käyttöliittymä esitys on eristetty sovelluslogiikasta. Käyttöliittymä kutsuu vain omiaan elementtejään ja päivittää jos elementille on tullut muutos.

Peliin on luotu UI elementtejä käsittelevät arkkitehtuuri. Pygame ei itsestään tarjoa UI elementtejä. Elementtien luomiseen on käytetty avuksi programmingpixels [blogin](https://programmingpixels.com/handling-a-title-screen-game-flow-and-buttons-in-pygame.html) git ohjeita.

UI Elementtejä on

- Tile
- Button
- Txt
- Score

Jokaisella elementillä on elementti kohtainen update funktion riippuen mihin tarkoitukseen elementti on luotu. Elementit käsittelevät itse muutokset. Jolloin jokainen elementti on riippumaton toisista elementeistä, sekä muista samanlaisita elementeistä. 

Elementtien update funktio toimii myös draw funktiona kun käytetään renderöijän kautta. Muuten vain toteuttaa muutokse.

Tile elementin click funktio käsittelee jokaisen painalluksen ja muuttaa elemntiä sen mukaan minkä on numeron Tile saa.

Button elementit sisältävät eriksen actionin joka palauttaa halutun arvon.


## Sovelluslogiikka

Sovelluksen kokonaisuudesta vastaa GameLoop olio. Olio kutsuu event_jonoa, näkymiä, ja renderöijää. Jokaista näistä on vähintään yksi. 

Kun on saatu eventti. GameLoop kysyy näkymää ja tekee muutoksen näkymän 

Renderöijä renderöi jokaisen UI elementin uudelleen vaikkei tullut muutoksia. Renderöijä kutsuu joka kerta update funktiota jossa on elementti kohtainen logiikka.

Pelaajan on vain mahdollista klikata peliä. Pelissä on vain hiiren käyttämistä.

