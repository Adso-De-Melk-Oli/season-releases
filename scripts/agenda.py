"""Construit agenda.json pour l'app SEASON.

Sources (open data, sans clé) :
- DATAtourisme, export « fêtes et manifestations » publié chaque nuit sur data.gouv.fr
- Calendrier scolaire de l'Éducation nationale (zone C, académie de Montpellier)

Usage : python3 agenda.py fma.csv vacances.json sortie.json [AAAA-MM-JJ]
"""
import csv, datetime as dt, html, json, re, sys
from zoneinfo import ZoneInfo

PARIS = ZoneInfo("Europe/Paris")
HORIZON = 120          # jours d'événements gardés
MAX_PERIODS = 40

# Les 31 communes de Montpellier Méditerranée Métropole
METROPOLE = {
    "baillargues", "beaulieu", "castelnau-le-lez", "castries", "clapiers", "cournonsec", "cournonterral",
    "fabregues", "grabels", "jacou", "juvignac", "lattes", "laverune", "le cres", "montaud",
    "montferrier-sur-lez", "montpellier", "murviel-les-montpellier", "perols", "pignan", "prades-le-lez",
    "restinclieres", "saint-bres", "saint-drezery", "saint-genies-des-mourgues", "saint-georges-d'orques",
    "saint-jean-de-vedas", "saussan", "sussargues", "vendargues", "villeneuve-les-maguelone",
}

# Catégorie DATAtourisme -> rubrique de l'app (la première trouvée dans cet ordre l'emporte)
CATS = [
    ("concert", {"Concert", "MusicEvent"}),
    ("expo", {"Exhibition", "ExhibitionEvent"}),
    ("spectacle", {"TheaterEvent", "ShowEvent", "ScreeningEvent", "Reading", "DanceEvent", "CircusEvent"}),
    ("sport", {"SportsEvent", "SportsCompetition", "SportsDemonstration"}),
    ("marche", {"SaleEvent", "Market", "Fair", "GarageSale", "FleaMarket", "ChristmasMarket"}),
    ("fete", {"Festival", "SocialEvent", "LocalAnimation", "Carnival", "Parade", "TraditionalCelebration", "Commemoration"}),
    ("atelier", {"Visit", "Practice", "Traineeship", "Product", "Conference", "ChildrensEvent", "Game", "Workshop"}),
]
OUTDOOR_CATS = {"Walk", "SportsEvent", "SportsCompetition", "Market", "SaleEvent", "Fair", "GarageSale", "FleaMarket",
                "ChristmasMarket", "Festival", "Carnival", "Parade", "LocalAnimation", "Visit"}
INDOOR_WORDS = r"arena|zénith|zenith|op[ée]ra|th[ée][âa]tre|salle|mus[ée]e|m[ée]diath[èe]que|parc des expo|parc expo|gymnase|piscine|palais|cin[ée]ma|basket|handball|volley|futsal|halle|atelier|conf[ée]rence|\bvs\b|\bmma\b|boxe|catch|escape"
OUTDOOR_WORDS = r"plein air|balade|randonn[ée]e|march[ée]|brocante|vide[- ]grenier|foul[ée]es|\bcourse\b|trail|feu d'artifice|\bparc\b|jardin|plage|promenade|visite guid[ée]e|dimanches du peyrou|f[êe]te de|carnaval|parade|d[ée]fil[ée]"

SMALL = {"de", "du", "des", "la", "le", "les", "et", "à", "au", "aux", "en", "pour", "sur", "par", "avec", "un", "une", "d'", "l'", "ou"}


def fold(s):
    s = s.lower().strip()
    for a, b in (("é", "e"), ("è", "e"), ("ê", "e"), ("ë", "e"), ("à", "a"), ("â", "a"), ("î", "i"), ("ï", "i"),
                 ("ô", "o"), ("ù", "u"), ("û", "u"), ("ç", "c"), ("’", "'")):
        s = s.replace(a, b)
    return s


def nice_title(t):
    t = re.sub(r"\s+", " ", t).strip()
    letters = [c for c in t if c.isalpha()]
    if not letters or sum(c.isupper() for c in letters) / len(letters) < 0.8:
        return t                                   # déjà en casse normale
    out = []
    for i, w in enumerate(t.lower().split(" ")):
        m = re.match(r"^([dl]['’])(.+)$", w)
        if m and i > 0:
            out.append(m.group(1) + m.group(2)[:1].upper() + m.group(2)[1:]); continue
        if i > 0 and w in SMALL:
            out.append(w); continue
        out.append(w[:1].upper() + w[1:])
    s = " ".join(out)
    return re.sub(r"(?<=[-–(/])([a-zà-ÿ])", lambda m: m.group(1).upper(), s)


def clean_text(s, n=600):
    s = html.unescape(re.sub(r"<[^>]+>", " ", s or ""))
    s = re.sub(r"\s+", " ", s).strip()
    if len(s) > n:
        s = s[:n].rsplit(" ", 1)[0] + "…"
    return s


def first_url(contacts):
    for part in (contacts or "").split("|"):
        for bit in part.split("#"):
            bit = bit.strip()
            if bit.startswith("http"):
                return bit
    return None


def periods(raw, today):
    out = []
    for p in (raw or "").split("|"):
        m = re.match(r"(\d{4}-\d{2}-\d{2})<->(\d{4}-\d{2}-\d{2})", p.strip())
        if not m:
            continue
        a, b = dt.date.fromisoformat(m.group(1)), dt.date.fromisoformat(m.group(2))
        if b < a:
            a, b = b, a
        if b < today or a > today + dt.timedelta(days=HORIZON):
            continue
        out.append((a, b))
    out = sorted(set(out))
    merged = []
    for a, b in out:
        if merged and a <= merged[-1][1] + dt.timedelta(days=1):
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a, b))
    return merged[:MAX_PERIODS]


# Mots du titre qui précisent une catégorie trop générale (« CulturalEvent » seul)
KEYWORDS = [
    ("expo", r"\bexpo(sition)?s?\b|vernissage|galerie"),
    ("concert", r"concert|r[ée]cital|orchestre|\bjazz\b|chorale|op[ée]ra\b|symphoni|musique"),
    ("spectacle", r"spectacle|th[ée][âa]tre|cirque|danse|humour|one[- ]man|com[ée]die|marionnette|cin[ée]|projection|conte"),
    ("marche", r"march[ée]|brocante|vide[- ]grenier|braderie|\bsalon\b|foire|puces|chineu"),
    ("sport", r"\bcourse\b|foul[ée]es|trail|marathon|match|tournoi|\brando"),
    ("atelier", r"atelier|stage|conf[ée]rence|initiation|cours de|jeu(x)? de piste|jeune public|agora|rencontre|lecture"),
    ("visite", r"visite|balade|d[ée]couverte|centre historique|patrimoine|histoire|ch[âa]teau|b[âa]timent historique"),
    ("fete", r"f[êe]te|festival|carnaval|lumi[èe]res|no[ëe]l|soir[ée]e|bal\b"),
]


def category(classes, title=""):
    key = next((k for k, names in CATS if classes & names), None)
    if key in (None, "atelier", "fete"):
        t = fold(title)
        for k, rx in KEYWORDS:
            if re.search(fold(rx), t):
                return k
    if key == "atelier" and "Visit" in classes:
        return "visite"
    return key or "culture"


def outdoor(classes, title, address):
    text = fold(title + " " + address)
    if re.search(fold(INDOOR_WORDS), text):
        return False
    if re.search(fold(OUTDOOR_WORDS), text):
        return True
    return bool(classes & OUTDOOR_CATS)


def build_events(csv_path, today):
    seen, events = set(), []
    with open(csv_path, encoding="utf-8", newline="") as f:
        for r in csv.DictReader(f):
            pc, _, commune = (r.get("Code_postal_et_commune") or "").partition("#")
            if not pc.startswith("34") or fold(commune) not in METROPOLE:
                continue
            per = periods(r.get("Periodes_regroupees"), today)
            if not per:
                continue
            raw_title = (r.get("Nom_du_POI") or "").strip()
            if not raw_title:
                continue
            classes = {c.rsplit("#", 1)[-1].rsplit("/", 1)[-1] for c in (r.get("Categories_de_POI") or "").split("|")}
            cancelled = bool(re.match(r"^\s*(annul[ée]|report[ée])", fold(raw_title)))
            title = re.sub(r"^\s*(annul[ée]e?|report[ée]e?)\s*[-–:]\s*", "", raw_title, flags=re.I)
            title = nice_title(title)
            key = (fold(title), commune, per[0][0])
            if key in seen:
                continue
            seen.add(key)
            address = (r.get("Adresse_postale") or "").strip()
            try:
                lat, lon = round(float(r["Latitude"]), 5), round(float(r["Longitude"]), 5)
            except (TypeError, ValueError, KeyError):
                lat = lon = None
            e = {
                "id": (r.get("URI_ID_du_POI") or "").rsplit("/", 1)[-1],
                "t": title,
                "c": category(classes, title),
                "o": 1 if outdoor(classes, title, address) else 0,
                "p": [[a.isoformat(), b.isoformat()] for a, b in per],
                "a": address,
                "v": commune.strip(),
                "s": clean_text(r.get("Description")),
                "src": (r.get("Createur_de_la_donnee") or "").strip(),
            }
            if lat is not None:
                e["lat"], e["lon"] = lat, lon
            u = first_url(r.get("Contacts_du_POI"))
            if u:
                e["u"] = u
            if cancelled:
                e["x"] = 1
            events.append(e)
    events.sort(key=lambda e: (e["p"][0][0], e["t"]))
    return events


def build_holidays(path, today):
    try:
        d = json.load(open(path, encoding="utf-8"))
    except Exception:
        return []
    out = {}
    for r in d.get("results", []):
        if (r.get("population") or "-") == "Enseignants":
            continue
        try:
            s = dt.datetime.fromisoformat(r["start_date"]).astimezone(PARIS).date()
            e = dt.datetime.fromisoformat(r["end_date"]).astimezone(PARIS).date()
        except Exception:
            continue
        last = e - dt.timedelta(days=1) if e > s else s      # end_date = jour de reprise des cours
        if last < today:
            continue
        name = (r.get("description") or "Vacances").strip()
        name = name[:1].upper() + name[1:].lower().replace("noël", "Noël").replace("ascension", "Ascension").replace("toussaint", "Toussaint")
        out[(s, name)] = {"n": name, "s": s.isoformat(), "e": last.isoformat()}
    return [out[k] for k in sorted(out)]


def main():
    csv_path, vac_path, out_path = sys.argv[1:4]
    today = dt.date.fromisoformat(sys.argv[4]) if len(sys.argv) > 4 else dt.datetime.now(PARIS).date()
    events = build_events(csv_path, today)
    data = {
        "v": 1,
        "updated": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "events": events,
        "vacances": build_holidays(vac_path, today),
        "sources": "DATAtourisme (offices de tourisme) · Éducation nationale",
    }
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, separators=(",", ":"))
    print(f"{len(events)} événements, {len(data['vacances'])} périodes de vacances")


if __name__ == "__main__":
    main()
