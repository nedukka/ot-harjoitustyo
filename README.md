# Ohjelmistotekniikka, harjoitustyö

Sovelluksen tarkoituksena on tarjota käyttäjälle työkalu *tehtävien* hallintaan, joka keskittyy **viikkotason** suunnitteluun perinteisen päivätason aikataulutuksen sijaan.

## Dokumentaatio

- [vaatimusmäärittely](https://github.com/nedukka/ot-harjoitustyo/blob/main/dokumentaatio/vaatimusmaarittely.md)
- [työaikakirjanpito](https://github.com/nedukka/ot-harjoitustyo/blob/main/dokumentaatio/tyoaikakirjanpito.md)
- [changelog](https://github.com/nedukka/ot-harjoitustyo/blob/main/dokumentaatio/changelog.md)
- [arkkitehtuurikuvaus](https://github.com/nedukka/ot-harjoitustyo/blob/main/dokumentaatio/arkkitehtuuri.md)

## Sovelluksen asennus

1)

```bash
poetry install
```
2)

```bash
poetry run invoke bild
```

3)

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Testaus

```bash
poetry run invoke test
```

### Testikattavuus

```bash
poetry run invoke coverage-report
```

### Pylint

```bash
poetry run invoke lint
```
