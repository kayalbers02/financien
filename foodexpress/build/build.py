"""Bouwt twee versies uit template2.html + menu.json:

  ../index.html  "Werkt nu": tik op een gerecht = dat gerecht openen op foodexpressdeurne.nl
  ../demo.html   "Demo":     tik op een gerecht = in de winkelwagen op deze pagina, met nagespeeld afrekenen

Gebruik:  python3 build.py <menu.json> <cbk-fonts-map> <cbk-beeldmerk.svg> [live-url] [demo-url]
"""
import base64, html, json, pathlib, re, sys

from art import ART

here = pathlib.Path(__file__).parent
menu_path, fonts_dir, mark_path = sys.argv[1], pathlib.Path(sys.argv[2]), sys.argv[3]
live_url = sys.argv[4] if len(sys.argv) > 4 else "index.html"
demo_url = sys.argv[5] if len(sys.argv) > 5 else "demo.html"
menu = json.load(open(menu_path, encoding="utf-8"))
tpl = (here / "template2.html").read_text(encoding="utf-8")
SITE = "https://www.foodexpressdeurne.nl/"
DATE = "8 november 2026"

# Categorieën met een eigen tekening; Friet zit bij Foodexpress onder Extra's (12)
ICON = {6: 6, 1: 1, 4: 4, 11: 11, 12: 12, 21: 21, 13: 13, 25: 25}
NAV_LABEL = {13: "Dranken", 15: "Bier", 9: "Mix grill", 25: "IJs", 12: "Friet & extra's"}


def e(s):
    return html.escape(s, quote=True)


def euro(p):
    return "€ " + f"{p:.2f}".replace(".", ",")


def svg(cid):
    return f'<svg viewBox="0 0 120 120" aria-hidden="true">{ART[cid]}</svg>'


def sections(mode):
    out = []
    for c in menu:
        cid, name = c["c"], c["name"]
        icon = f'<span class="ic">{svg(ICON[cid])}</span>' if cid in ICON else ""
        n = len(c["items"])
        dishes = []
        for it in c["items"]:
            hay = e((it["n"] + " " + it["d"]).lower())
            desc = f'<span class="d">{e(it["d"])}</span>' if it["d"] else ""
            if mode == "live":
                price = f'<span class="price">{euro(it["p"])}<span class="orb">↗</span></span>'
                tag_open = (f'<a class="dish" href="{SITE}#product{it["id"]}" target="_blank" rel="noopener" data-hay="{hay}" '
                            f'aria-label="{e(it["n"])}, {euro(it["p"])}, openen bij Foodexpress">')
                tag_close = "</a>"
            else:
                price = f'<span class="price">+ {euro(it["p"])}<span class="orb">+</span></span>'
                tag_open = (f'<button class="dish" type="button" data-id="{it["id"]}" data-hay="{hay}" '
                            f'aria-label="{e(it["n"])}, {euro(it["p"])}, toevoegen aan winkelwagen">')
                tag_close = "</button>"
            dishes.append(f'<li>{tag_open}<span class="info"><span class="n">{e(it["n"])}</span>{desc}</span>{price}{tag_close}</li>')
        out.append(f'''<section class="cat" id="cat-{cid}" data-name="{e(name)}">
      <div class="cat-kop">{icon}<h2>{e(name)}<small>{n} {"gerecht" if n == 1 else "gerechten"}</small></h2></div>
      <ul class="dishes">
        {"".join(dishes)}
      </ul>
    </section>''')
    return "\n    ".join(out)


def nav():
    return "\n    ".join(f'<li><a href="#cat-{c["c"]}">{e(NAV_LABEL.get(c["c"], c["name"]))}</a></li>' for c in menu)


def b64(name):
    return base64.b64encode((fonts_dir / name).read_bytes()).decode()


mark = pathlib.Path(mark_path).read_text(encoding="utf-8")
mark = re.sub(r"<\?xml[^>]*\?>", "", mark)
mark = re.sub(r"<defs>.*?</defs>", "", mark, flags=re.S)
mark = re.sub(r'\s(id|version|class)="[^"]*"', "", mark)
mark = mark.replace("<path", '<path fill="currentColor"').replace("<svg", '<svg aria-hidden="true"', 1).strip()

DIALOG = '''<dialog class="sheet" id="sheet" aria-labelledby="shTitel">
  <div class="sh-kop"><h3 id="shTitel">Winkelwagen</h3><p id="shSub"></p><button class="sluit" id="sluit" type="button" aria-label="Sluiten">×</button></div>
  <div class="sh-body" id="shBody"></div>
  <div class="sh-foot" id="shFoot"></div>
</dialog>'''

VARIANTS = {
    "live": dict(
        out="index.html", TITLE="Snackavond Deurne", MODE="live", BODY_PAD="96px",
        TAG="Werkt nu · <b>direct naar het gerecht</b>",
        NOTICE_LABEL="Werkt nu",
        NOTICE="Tik op een gerecht en het opent direct bij Foodexpress. Daar zet je het in je winkelwagen en reken je af.",
        H1_LAST="Bestel direct.",
        LEDE="Alle gerechten van Foodexpress Deurne op één pagina. Tik op een gerecht en je staat er meteen bij op hun bestelpagina.",
        OTHER_URL=demo_url, OTHER_LABEL="Bekijk de demo met winkelwagen",
        BAR=f'<div class="txt">Foodexpress Deurne<small>Bestellen en afrekenen gaat via hun eigen site</small></div><a class="btn" href="{SITE}#menu" target="_blank" rel="noopener">Bestellen ↗</a>',
        DIALOG="",
    ),
    "demo": dict(
        out="demo.html", TITLE="Snackavond Demo", MODE="demo", BODY_PAD="96px",
        TAG="Demo · <b>winkelwagen-concept</b>",
        NOTICE_LABEL="Demo",
        NOTICE="Je winkelwagen werkt alleen op deze pagina. Er wordt niets naar Foodexpress gestuurd en niets besteld.",
        H1_LAST="In je wagen.",
        LEDE="Tik op een gerecht en het vliegt in je winkelwagen. Bij afrekenen zie je hoe het zou gaan als je wagen in één keer naar Foodexpress kon.",
        OTHER_URL=live_url, OTHER_LABEL="Naar de versie die nu werkt",
        BAR='<div class="txt">Jouw winkelwagen<small id="barSub">Tik op een gerecht om het toe te voegen</small></div><button class="btn cartbtn" id="cartBtn" type="button">Winkelwagen <span class="count">0</span></button>',
        DIALOG=DIALOG,
    ),
}

common = {
    "FONT_CABINET": b64("CabinetGrotesk-Extrabold.woff2"),
    "FONT_ZODIAK": b64("Zodiak-Regular.woff2"),
    "NAV": nav(),
    "DATE": DATE,
    "CBK_MARK": mark,
    "ART_6": svg(6), "ART_1": svg(1), "ART_12": svg(12),
    "MENU": json.dumps(menu, ensure_ascii=False).replace("</", "<\\/"),
}

for mode, v in VARIANTS.items():
    vals = dict(common, **{k: val for k, val in v.items() if k != "out"}, SECTIONS=sections(mode))
    page = re.sub(r"\{\{(\w+)\}\}", lambda m: vals[m.group(1)], tpl)
    (here.parent / v["out"]).write_text(page, encoding="utf-8")
    print("ok", v["out"], len(page) // 1024, "KB")
