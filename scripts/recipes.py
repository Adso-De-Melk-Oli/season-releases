"""Construit data/recipes.json pour l'app SEASON à partir de recipes_data.py.
- mois de saison calculés avec le calendrier des fruits et légumes (et des poissons) ;
- kcal par personne calculées avec une table de valeurs moyennes (approximation, base Ciqual) ;
- indicateurs : porc, bœuf, sans sel possible."""
import json, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from recipes_data import R

# kcal pour 100 g (valeurs moyennes arrondies)
KCAL = dict(
    potimarron=30, oignon=40, carotte=36, epice=0, bouillon=5, creme=290, huile=900, graines=560, sel=0, choufleur=25, lait=47, beurre=745,
    farine=350, tomme=360, riz=350, champignon=25, vin=70, parmesan=400, herbe=0, poischiche=140, patatedouce=86, epinard=23, coco=190,
    poireau=30, pdt=80, endive=17, poire=55, noix=700, roquefort=360, lentille=330, pate=430, chevre=210, oeuf=140, pates=360, brocoli=34,
    ail=130, citron=30, panais=70, pomme=54, betterave=45, orange=47, asperge=25, petitspois=80, feve=70, ricotta=150, radis=15, concombre=13,
    yaourt=100, aubergine=25, courgette=17, poivron=30, tomate=18, peche=45, mozzarella=250, haricotvert=30, haricotblanc=110, artichaut=45,
    chataigne=200, fenouil=30, olive=150, blette=20, poulet_cuisse=190, poulet_blanc=120, agneau=230, veau=150, boeuf_braise=170, boeuf_maigre=130,
    porc_filet=140, porc_cote=200, saucisse=300, lapin=130, canard=200, confit=300, dinde=110, moutarde=150, miel=320, coing=60, figue=75,
    daurade=100, moule=85, seiche=80, sardine=140, maquereau=200, merlan=80, cabillaud=80, celeri=30, encornet=90, thon=130, stjacques=90,
    rouget=110, bar=100, anchois=130, sucre=400, amande=600, cerise=60, fraise=33, abricot=48, melon=34, noisette=640, feuilletee=400,
    chocolat=550, rhubarbe=20, pasteque=30, raisin=70, fromageblanc=75, kiwi=60,
)
# Aliments salés et leur remplacement en mode « sans sel ajouté » (None = la recette n'est pas proposée)
SALTY = {"bouillon": "de bouillon de légumes sans sel ajouté", "olive": None, "saucisse": None, "confit": None, "roquefort": "de chèvre frais",
         "parmesan": "de parmesan (facultatif, à doser)", "anchois": "d'anchois frais (ils ne sont pas salés)", "moutarde": "de moutarde à l'ancienne, peu salée"}
PORK = {"porc_filet", "porc_cote", "saucisse"}
BEEF = {"boeuf_braise", "boeuf_maigre"}

FISH = {"Sardine": [5, 6, 7, 8, 9, 10], "Anchois": [4, 5, 6, 7, 8, 9], "Maquereau": [3, 4, 5, 6], "Daurade": [4, 5, 6, 7, 8, 9, 10, 11, 12],
        "Merlan": [10, 11, 12, 1, 2, 3], "Cabillaud": [10, 11, 12, 1, 2, 3, 4], "Seiche": [2, 3, 4, 5, 6, 9, 10, 11],
        "Encornet": [6, 7, 8, 9, 10], "Moules": [9, 10, 11, 12, 1, 2, 3, 4], "Saint-Jacques": [10, 11, 12, 1, 2, 3, 4, 5],
        "Thon": [6, 7, 8, 9], "Rouget": [5, 6, 7, 8, 9, 10], "Bar": [10, 11, 12, 1, 2, 3]}
FISH_LABEL = {"Sardine": "sardine", "Anchois": "anchois", "Maquereau": "maquereau", "Daurade": "daurade", "Merlan": "merlan", "Cabillaud": "cabillaud",
              "Seiche": "seiche", "Encornet": "encornet", "Moules": "moules de Bouzigues", "Saint-Jacques": "coquilles Saint-Jacques",
              "Thon": "thon", "Rouget": "rouget", "Bar": "bar"}
# Équivalences avec le calendrier des produits de l'app
ALIAS = {"Potimarron": ["Potimarron", "Potiron", "Courge", "Courge butternut"], "Carotte": ["Carotte", "Carotte nouvelle"],
         "Champignons": ["Champignons"], "Oignon nouveau": ["Oignon nouveau"], "Céleri-rave": ["Céleri-rave", "Céleri"]}

def produce(season_json):
    d = json.load(open(season_json, encoding="utf-8"))["produce"]
    return {int(m): set(p["f"].split(",")) | set(p["l"].split(",")) for m, p in d.items()}

def months_for(rec, prod):
    if rec["m"]:
        return sorted(rec["m"])
    ms = set(range(1, 13))
    for u in rec["u"]:
        names = ALIAS.get(u, [u])
        ok = {m for m in range(1, 13) if any(n in prod[m] for n in names)}
        assert ok, f"{rec['id']} : produit inconnu {u}"
        ms &= ok
    if rec["f"]:
        ms &= set(FISH[rec["f"]])
    assert ms, f"{rec['id']} : aucun mois"
    return sorted(ms)

def build(season_json, out):
    prod = produce(season_json)
    recipes = []
    for x in R:
        ing, kcal, salty_block, pork, beef, has_salt = [], 0, False, False, False, False
        for q, unit, name, food, grams in x["i"]:
            assert food in KCAL, f"{x['id']} : aliment inconnu {food}"
            kcal += KCAL[food] * grams / 100
            e = {"q": q, "u": unit, "n": name}
            if food == "sel":
                e["salt"] = 1; has_salt = True
            elif food in SALTY:
                has_salt = True
                if SALTY[food] is None: salty_block = True
                else: e["ns"] = SALTY[food]
            pork |= food in PORK; beef |= food in BEEF
            ing.append(e)
        months = months_for(x, prod)
        recipes.append({
            "id": x["id"], "n": x["n"], "k": x["k"], "t": x["t"], "m": months, "r": x["reg"], "v": x["meat"],
            "pork": int(pork), "beef": int(beef), "sw": int(x["sweet"]), "ns": int(not salty_block), "salt": int(has_salt),
            "u": x["u"] + ([FISH_LABEL[x["f"]].capitalize()] if x["f"] else []), "kcal": round(kcal / x["parts"] / 10) * 10, "p": 2, "parts": x["parts"],
            "i": ing, "s": x["s"], **({"tip": x["tip"]} if x["tip"] else {}),
        })
    ids = [r["id"] for r in recipes]; assert len(ids) == len(set(ids)), "identifiants en double"
    fish = {str(m): [FISH_LABEL[k] for k, ms in FISH.items() if m in ms] for m in range(1, 13)}
    data = {"v": 1, "recipes": recipes, "fish": fish}
    json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    return recipes

if __name__ == "__main__":
    rec = build(sys.argv[1], sys.argv[2])
    print(len(rec), "recettes")
    import collections
    for m in range(1, 13):
        c = collections.Counter()
        for x in rec:
            if m in x["m"]:
                c["dessert" if x["sw"] else x["r"]] += 1
        print(m, dict(c))
