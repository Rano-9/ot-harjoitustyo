# Ohjelmistotekniikka, harjoitustyö

Harjoitsustyön tarkoitus on tehdä peli joka mukailee Puzzle Pirates minipeliä.



## Dokumentaatio:
- [Määrittelydokumentti](https://github.com/Rano-9/ot-harjoitustyo/blob/main/peli-app/dokumentaatio/vaatimusm%C3%A4%C3%A4rittely.md)
- [Työaikakirjanpito](https://github.com/Rano-9/ot-harjoitustyo/blob/main/peli-app/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/Rano-9/ot-harjoitustyo/blob/main/peli-app/dokumentaatio/changelog.md)

## Asennus
Sovelluksen saa asennettua suorittamalla seuraavat komennot peli-app hakemistossa
- ``` poetry install ```
- ``` poetry run invoke start ```

## Poetry komennot

Pelin aloittava komento
``` poerty run invoke start ```

Testit suorittava komento
``` poetry run invoke test```

Testikattavuus raportin tuotava komento
``` poetry run invoke coverage```

Pylint komento
``` poetry run invoke lint```