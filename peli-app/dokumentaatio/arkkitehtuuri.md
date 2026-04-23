# Arkkitehtuurikuvaus

## Käyttöliittymä

Käyttöliittymässä on kolme näkymää. 

- Aloitus
- Peli
- Pisteytys
- Lopetus

Jokainen on oma luokkansa ja enintään kaksi näkynmää ovat yhtä aikaa käytössä. Käyttöliittymä esitys on eristetty sovelluslogiikasta. Käyttöliittymä kutsuu vain omiaan elementtejään ja päivittää jos elementille on tullut muutos.

Elementtejä on

- Tile
- Button
- Txt
- Score

Jokaisella elementillä on erillainen update funktion riippuen mihin tarkoitukseen elementti on luotu. Elementit käsittelevät itse muutokset. Jolloin jokainen elementti on riippumaton toisista elementeistä. 

Esimerkiksi Tile elementin click funktio käsittelee jokaisen painalluksen ja muuttaa elemntin kuvaa sen mukaan mikä on numero.

## Sovelluslogiikka

Sovelluksen kokonaisuudesta vastaa GameLoop olio. Olio käsittelee 

