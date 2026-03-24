Sovelluksen tarkoitus:

Tarkoitus on luoda peli joka on samankaltainen kuin pelin [puzzle pirates Blacksmithing](https://yppedia.puzzlepirates.com/Blacksmithing) minipeli. Tarkkuutena vain minipeli ensimmäiset tasot joissa on laattoina vain 1-4 eikä erikois liikkeitä.

Pelissä on vain yksipelaaja.

Peli alkaa satunnaisella 6*6 laudalla ja tarkoitus on tyhjentää lauta. Laudalla on laattoja joissa on numero joka kertoo seuraavan liikeen. 

Pelaaja voi valita laudalta ensimmäisen laatan. 
Seuraava liikkuminen tapahtuu laassa olevan arvon mukaisesti. 

Esimerkiksi lauta

```
 1   2   3   3
 1   3   3   2
 1   2   3   4
 1   2   1   1
```


1 -> liiku 1 laatan päähän. 

```
*1* (2)  3   3
(1) (3)  3   2
 1   2   3   4
 1   2   1   1
```

2 -> liikkuu 2 laatan päähän

```
 1  *2*  3  (3)
 1   3   3   2
 1  (2)  3  (4)
 1   2   1   1
```

Peli loppuu jos ei pysty tehdä siirtoa.
Jokaisella laatalla on mahdollista käydä 3 kertaa. Sen jälkeen laatta putoaa pelistä ja kentään syntyy aukkoja.  


Jatkokehityksenä on toeuttaa pelin muut nappulat jotka liikkuvat kuin shakki nappulat. 