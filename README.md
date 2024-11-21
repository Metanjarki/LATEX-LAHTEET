# BibTex -lähdehallintatyökalu 
[![GHA workflow badge](https://github.com/Metanjarki/LATEX-LAHTEET/workflows/CI/badge.svg)](https://github.com/Metanjarki/LATEX-LAHTEET/actions)

Sovelluksen tarkoitus on helpottaa kirjaviitausten keräämistä ja niiden käsittelyä

## Backlog
Nykyisen backlogin voi nähdä [täältä](https://docs.google.com/spreadsheets/d/1M5kKUjORXVepBhWVwGJPqX7DncR86aFn1dlTe7wg358/edit?usp=sharing)

## Asennus
Asenna projektin riippuvuudet ajamalla `poetry install`. Tämän jälkeen laita projektin juureen `.env` -niminen tiedosto, joka sisältää ainakin seuraavat tiedot.

```
DATABASE_URL=Postgres-tietokannan osoite
TEST_ENV=true
SECRET_KEY=jokin satunnainen merkkijono
```

Tämän jälkeen aktivoi python-virtuaaliympäristö komennolla `poetry shell`. Tämän jälkeen projektin ajaminen onnistuu komennolla `python3 src/index.py`.

## Definition of done
TODO
