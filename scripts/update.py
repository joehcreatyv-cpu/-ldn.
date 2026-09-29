"""Récupère les résultats de la Ligue des Nations via API-Football et écrit data/results.json."""
import json, os, sys, urllib.request, datetime
KEY = os.environ.get("API_FOOTBALL_KEY")
LEAGUE, SEASON = 5, 2026   # à vérifier dans votre compte API-Football
FR = {"Netherlands":"Pays-Bas","Germany":"Allemagne","Serbia":"Serbie","Greece":"Grèce","Norway":"Norvège","Denmark":"Danemark","Wales":"Pays de Galles","Austria":"Autriche","Israel":"Israël","Ireland":"Irlande","Republic of Ireland":"Irlande","Georgia":"Géorgie","Northern Ireland":"Irlande du Nord","Italy":"Italie","Belgium":"Belgique","Turkey":"Turquie","Türkiye":"Turquie","Hungary":"Hongrie","Poland":"Pologne","Bosnia & Herzegovina":"Bosnie","Bosnia and Herzegovina":"Bosnie","Sweden":"Suède","Romania":"Roumanie","Slovenia":"Slovénie","Scotland":"Écosse","Czech Republic":"Tchéquie","Czechia":"Tchéquie","Croatia":"Croatie","England":"Angleterre","Spain":"Espagne","Switzerland":"Suisse","North Macedonia":"Macédoine du Nord"}
MOIS = ["janv.","févr.","mars","avr.","mai","juin","juil.","août","sept.","oct.","nov.","déc."]
def nom(n): return FR.get(n, n)
def jour(iso):
    d = datetime.datetime.fromisoformat(iso.replace("Z", "+00:00"))
    return f"{d.day} {MOIS[d.month-1]}"
if not KEY: sys.exit("Clé API_FOOTBALL_KEY absente")
req = urllib.request.Request(f"https://v3.football.api-sports.io/fixtures?league={LEAGUE}&season={SEASON}", headers={"x-apisports-key": KEY})
j = json.load(urllib.request.urlopen(req, timeout=30))
if j.get("errors"): sys.exit("Erreur API : " + str(j["errors"]))
res, fx = [], []
for m in sorted(j.get("response", []), key=lambda m: m["fixture"]["date"]):
    h, a = nom(m["teams"]["home"]["name"]), nom(m["teams"]["away"]["name"])
    d, st = jour(m["fixture"]["date"]), m["fixture"]["status"]["short"]
    if st in ("FT", "AET", "PEN") and m["goals"]["home"] is not None:
        res.append({"h": h, "a": a, "gh": m["goals"]["home"], "ga": m["goals"]["away"], "d": d})
    elif st in ("NS", "TBD"):
        fx.append({"h": h, "a": a, "d": d})
if not res: sys.exit("Aucun résultat reçu : données existantes conservées")
now = datetime.datetime.now(datetime.timezone.utc).strftime("%d/%m/%Y %H:%M UTC")
json.dump({"updated": now, "results": res, "fixtures": fx[:30]}, open("data/results.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(res), "résultats,", len(fx[:30]), "matchs à venir")
