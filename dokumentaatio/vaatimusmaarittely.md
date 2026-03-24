# Vaatimusmäärittely
## Sovelluksen perusidea
Sovelluksen tavoitteena on tarjota käyttäjälle vaihtoehto useiden tai liian pitkien todo-listojen tarpeelle. Sovellus perustuu yhteen *viikkotason* sunnitteluun tarkoitetun todo-listan hallintaan kolmen erilaisen *tehtävätyypin* avulla, joka antaa käyttäjälle mahdollisuuden suodattaa näkemiensä tehtävien määrää.

## Sovelluksen tarjoama toiminnallisuus
### Nimimerkin luominen
- Käyttäjä voi määrittää itselleen nimimerkin, jota käytetään sovelluksen käyttöliittymässä

### Tehtävien lisääminen ja poistaminen
- Käyttäjä voi lisätä uusia tehtäviä
- Tehtäville määritetään;
  - nimi
  - tehtävätyyppi
- Tehtävätyypit ovat:
  - ajaton (pysyy viikosta toiseen, kunnes suoritettu)
  - viikottainen (toistuu joka viikko)
  - viikkokohtainen (näkyy vain kyseisen viikon loppuun asti)
- Käyttäjä pystyy poistamaan tehtäviä

 ### Tehtävien tarkastelu ja suodatus
 - Käyttäjä pystyy tarkastelemaan kaikkia tehtäviään yhdessä näkymässä
 - Käyttäjä pystyy suodattamaan näkyviä tehtäviä valitsemalla motivaatiotason
 - Motivaatiotasot ja näkyvät tehtävät:
    - matala: näytetään vain *viikkokohtaiset* tehtävät
    - normaali: näytetään viikkokohtaiset+*viikottaiset*
    - korkea: näytetään kaikki tehtävät

  ### Tehtävien merkitseminen suoritetuksi
  - Käyttäjä voi merkitä tehtävän suoritetuksi
  - Suoritetun tehtävän käsittely riippuu tehtävätyypistä:
     - ajaton ja viikkokohtainen ovat kertaluontoisia suorituksia ja poistuvat listalta kokonaan
     - viikottainen poistuu kyseisen viikon osalta, mutta palautuu automaattisesti viikon vaihtuesssa
   
## Jatkokehitysideoita
Sovellusta voisi tulevaisuudessa kehittää:
- Lisäämällä usean käyttäjän tuen  
- Lisäämällä viikottaisen statistiikan suoritetuista tehtävistä
- Lisäämällä motivaatiotasoksi *vapaapäivä* vaihtoehdon, jolloin näytettäisiin lista mahdollisista kivoista aktiviteeteista
- Luomalla mahdollisuuden siirtää suorittamatta jääneitä viikkokohtaisia tehtäviä seuraavalle viikolle