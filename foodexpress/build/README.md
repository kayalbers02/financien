# Snackavond Deurne — bouwen

`index.html` (één map hoger) wordt gemaakt uit `template.html` + `menu.json`.

- **Stijl:** opbouw en kleuren van Pixmoza (nachtblauw, ivoor, roze, honing, lavendel schaduwen),
  typografie van CreativeByKay (Cabinet Grotesk, Zodiak, Satoshi, als data-URI ingebakken).
- **Links:** elk gerecht linkt naar `https://www.foodexpressdeurne.nl/#product<id>`, elke categorie
  naar `#categorie<id>`. Dat zijn de ankers op de menupagina van Foodexpress (Sitedish-platform).
  Een link die iets direct in de winkelwagen zet bestaat daar niet.

## Menu verversen

1. Sla de homepage van foodexpressdeurne.nl op en haal de gerechten eruit naar `menu.json`
   (per categorie: `c` = categorie-id, `name`, `items` met `id`, `n` naam, `p` prijs, `d` omschrijving).
2. Bouw opnieuw:

```
python3 build.py menu.json ../../../creativebykay-website/assets/fonts \
  ../../../creativebykay-website/assets/images/beeldmerk-teal.svg
```

Pas daarna de datum (`{{DATE}}` in `build.py`) aan.
