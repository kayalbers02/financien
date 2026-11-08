# Snackavond Deurne — bouwen

`build.py` maakt twee pagina's (één map hoger) uit `template2.html` + `menu.json` + `art.py`:

| Bestand | Versie | Tik op een gerecht |
|---|---|---|
| `index.html` | Werkt nu | opent dat gerecht op foodexpressdeurne.nl (`#product<id>`) |
| `demo.html` | Demo | gaat in een winkelwagen op de pagina zelf; afrekenen is nagespeeld, er wordt niets besteld |

- **Stijl:** opbouw van de Foodexpress-site (witte gerechtkaarten, turquoise prijsknoppen,
  categoriebalk, alle categorieën onder elkaar) met CreativeByKay-typografie en -kleuren
  (Cabinet Grotesk + Zodiak, als data-URI ingebakken). Beweging van CreativeByKay
  (paginawissel, openschuivende regels, veeg op knoppen) en Pixmoza (zwevende blokjes, harde schaduw).
- **Winkelwagen doorzetten** naar Foodexpress kan niet van buitenaf: hun winkelwagen leeft op de
  server van Sitedish. Daarvoor is een koppeling van Foodexpress/Sitedish nodig.

## Opnieuw bouwen

```
python3 build.py menu.json ../../../creativebykay-website/assets/fonts \
  ../../../creativebykay-website/assets/images/beeldmerk-teal.svg \
  https://claude.ai/artifact/6C9qisuF9cATN2FxZP4FZr https://claude.ai/artifact/5KuG8aPwDuYKZFcwhy5TTf
```

`menu.json` komt van de homepage van foodexpressdeurne.nl (per categorie `c`, `name`, `items`
met `id`, `n`, `p`, `d`). Pas na verversen ook `DATE` in `build.py` aan.
