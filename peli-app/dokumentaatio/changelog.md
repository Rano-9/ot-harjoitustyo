# Changelog

## Viikko 3

- Käyttäjä näkee pelikentän
- Käyttäjä pystyy klikkaamaan kentässä olevia laattoja.
- Lisätty pelin logiikaa varten luokkia.

## Viikko 4

- Pelaaja voi nyt nähdä mikä on laatan luku
- Pelaaja voi klikata ainoastaan laatan annetun luvun verran. 
- Peli loppuu kun pelaajalta loppuu sallitut liikkeet.
- Pelin laatat on selkeitä nähdä.

- Lisätty testit jotka edustavat peliä.

## Viikko 5

- Muokattu elementtien toimintaa. Jokainen laittaa joka on valittavissa on korostetu mustalla ja kun sen päällä hoveraa se vaihtaa erikseen väriä.

- Peli todella loppuu kun sallitut liikeet loppuvat.
- Pelin ikkunan voi nytten sulkea.
- Lisätty peliin aloitus näkymä.
- Lisätty peliin lopetus näkymä.

## Viikko 6

 - Artkkitehtuuria dokumentaatiota aloitettu kirjoittaa.
 - Arkkitehtuuria muutettuu loogisemmaksi. Jaettu ruudut näkymiin (Menu, Game, Score). Game ja Score näkymät näkyvät samaan aikaan näytöllä. 
 - Sprites osuudessa luotu Elements luokka. Vain Tiles on erillään. 

 - Lisätty peliin logiikka joka estää häviämisen keski laatoilla. Eli keskimmäiset 4 laattaa eivät saa lukua 4. 
 - Siirretty logiikkaa pois renderöinnistä.

 - Muutettuu elementtien update funktiota. Nytten renderöinti tapahtuu vain jos annetaan surface. Ja vain renderöijä antaa surfacen. Ja renderöijä saa muutokset käsitelyssä olevasta näkymästä.


