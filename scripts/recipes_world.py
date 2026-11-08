"""Recettes du monde de SEASON, en trois lots, toujours avec des produits de saison d'ici (pour 2 personnes).
Lot 1 : Asie, Maghreb et Orient, Inde. Lot 2 : Amériques et Afrique. Lot 3 : desserts du monde."""

ALL = list(range(1, 13))


def add_world(r, S):
    # =============== LOT 1 · ASIE ===============
    r("wok-poulet-brocoli", "Wok de poulet, brocoli et carottes", "Plat", 25, "viande", ["Brocoli", "Carotte"], [
        (300, "g", "de blanc de poulet", "poulet_blanc", 300), (1, "", "brocoli|brocolis", "brocoli", 300), (2, "", "carotte|carottes", "carotte", 200),
        (2, "c. à soupe", "de sauce soja", "soja", 30), (1, "c. à café", "de gingembre râpé", "epice", 5), (1, "gousse", "d'ail", "ail", 4),
        (1, "c. à soupe", "d'huile", "huile", 10), (120, "g", "de riz", "riz", 120)],
        ["Cuire le riz.", "Saisir le poulet en lanières 4 min dans l'huile très chaude, réserver.",
         "Faire sauter carottes en bâtonnets et bouquets de brocoli 5 min avec l'ail et le gingembre.",
         "Remettre le poulet, ajouter la sauce soja, servir avec le riz."], meat="volaille", c="asie", o="Chine")
    r("curry-thai-potiron", "Curry rouge thaï au potiron", "Plat", 30, "vege", ["Potimarron"], [
        (500, "g", "de potiron ou de potimarron", "potimarron", 500), (20, "cl", "de lait de coco", "coco", 200), (1, "c. à soupe", "de pâte de curry rouge", "epice", 15),
        (1, "", "oignon|oignons", "oignon", 100), (1, "", "citron vert|citrons verts", "citron", 30), (0.5, "botte", "de coriandre ou de basilic thaï", "herbe", 10),
        (120, "g", "de riz thaï", "riz", 120), (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Cuire le riz.", "Faire revenir l'oignon dans l'huile avec la pâte de curry 2 min.",
         "Ajouter le potiron en dés et le lait de coco, cuire 15 min.", "Ajouter le jus de citron vert et les herbes, assaisonner, servir avec le riz."],
        c="asie", o="Thaïlande", tip="La pâte de curry et le citron vert relèvent bien sans sel.")
    r("soupe-miso", "Soupe miso au tofu et poireau", "Soupe", 15, "vege", ["Poireau"], [
        (2, "c. à soupe", "de pâte miso", "miso", 36), (150, "g", "de tofu ferme", "tofu", 150), (1, "", "poireau|poireaux", "poireau", 150),
        (50, "g", "de champignons", "champignon", 50), (1, "c. à café", "de gingembre râpé", "epice", 5)],
        ["Porter 70 cl d'eau à frémissement avec le gingembre.", "Ajouter le poireau émincé et les champignons, cuire 5 min.",
         "Ajouter le tofu en dés.", "Hors du feu, délayer la pâte miso dans un peu de bouillon et l'ajouter (elle ne doit pas bouillir)."],
        c="asie", o="Japon")
    r("nouilles-chou", "Nouilles sautées au chou et à l'œuf", "Plat", 20, "vege", ["Chou"], [
        (160, "g", "de nouilles de blé", "pates", 160), (0.25, "", "chou|choux", "chou", 300), (2, "", "carotte|carottes", "carotte", 150),
        (2, "", "œuf|œufs", "oeuf", 110), (2, "c. à soupe", "de sauce soja", "soja", 30), (1, "c. à soupe", "d'huile", "huile", 10), (1, "gousse", "d'ail", "ail", 4)],
        ["Cuire les nouilles et les égoutter.", "Faire sauter le chou et les carottes émincés 6 min dans l'huile avec l'ail.",
         "Pousser les légumes, brouiller les œufs dans la poêle.", "Ajouter nouilles et sauce soja, mélanger 2 min."], c="asie", o="Chine")
    r("boeuf-gingembre", "Bœuf sauté au gingembre et poivrons", "Plat", 25, "viande", ["Poivron"], [
        (300, "g", "de rumsteck", "boeuf_maigre", 300), (2, "", "poivron|poivrons", "poivron", 350), (1, "", "oignon|oignons", "oignon", 100),
        (2, "c. à soupe", "de sauce soja", "soja", 30), (1, "c. à soupe", "de gingembre râpé", "epice", 10), (1, "c. à soupe", "d'huile", "huile", 10),
        (120, "g", "de riz", "riz", 120)],
        ["Cuire le riz.", "Saisir le bœuf en lanières 2 min, réserver.", "Sauter poivrons et oignon 6 min avec le gingembre.",
         "Remettre le bœuf, ajouter la sauce soja, servir avec le riz."], meat="boeuf", c="asie", o="Chine")
    r("daurade-vapeur-gingembre", "Daurade vapeur au gingembre et poireau", "Plat", 25, "poisson", ["Poireau"], [
        (2, "", "filet de daurade|filets de daurade", "daurade", 300), (1, "", "poireau|poireaux", "poireau", 150), (1, "c. à soupe", "de gingembre en julienne", "epice", 10),
        (1, "c. à soupe", "de sauce soja", "soja", 15), (1, "c. à soupe", "d'huile de sésame", "huile", 10), (120, "g", "de riz", "riz", 120)],
        ["Cuire le riz.", "Cuire les filets 8 min à la vapeur sur un lit de poireau émincé.",
         "Parsemer de gingembre, arroser de sauce soja.", "Verser l'huile de sésame bien chaude dessus et servir."], f="Daurade", c="asie", o="Chine")
    r("salade-concombre-sesame", "Salade de concombre au sésame", "Entrée", 10, "vege", ["Concombre"], [
        (1, "", "concombre|concombres", "concombre", 300), (1, "c. à soupe", "de vinaigre de riz", "epice", 15), (1, "c. à café", "d'huile de sésame", "huile", 5),
        (1, "c. à soupe", "de graines de sésame", "graines", 10), (1, "c. à café", "de sucre", "sucre", 4)],
        ["Couper le concombre en fines rondelles.", "Mélanger vinaigre, huile et sucre.",
         "Verser sur le concombre, laisser 10 min au frais.", "Parsemer de sésame grillé."], c="asie", o="Japon")
    r("porc-caramel", "Porc au caramel", "Plat", 40, "viande", ["Carotte"], [
        (350, "g", "d'échine de porc", "porc_cote", 350), (2, "c. à soupe", "de sucre", "sucre", 25), (1, "c. à soupe", "de nuoc-mâm", "nuocmam", 15),
        (2, "", "échalote|échalotes", "oignon", 60), (2, "", "carotte|carottes", "carotte", 200), (120, "g", "de riz", "riz", 120)],
        ["Faire un caramel blond avec le sucre et 2 c. à soupe d'eau.", "Ajouter le porc en cubes et les échalotes, bien enrober.",
         "Ajouter le nuoc-mâm, les carottes et un verre d'eau, cuire 30 min.", "Servir avec le riz."], meat="porc", c="asie", o="Viêt Nam")
    r("rouleaux-printemps", "Rouleaux de printemps aux légumes", "Entrée", 25, "vege", ["Laitue", "Radis"], [
        (6, "", "galette de riz|galettes de riz", "galette_riz", 50), (60, "g", "de vermicelles de riz", "pates", 60), (0.5, "", "laitue|laitues", "endive", 100),
        (6, "", "radis|radis", "radis", 60), (1, "", "carotte|carottes", "carotte", 100), (1, "brin", "de menthe", "herbe", 5),
        (2, "c. à soupe", "de sauce soja", "soja", 30)],
        ["Cuire les vermicelles et les rincer à l'eau froide.", "Râper la carotte, émincer radis et laitue.",
         "Ramollir chaque galette 5 s dans l'eau tiède, garnir et rouler serré.", "Servir avec la sauce soja."], c="asie", o="Viêt Nam")
    r("maquereau-teriyaki", "Maquereau teriyaki et riz", "Plat", 20, "poisson", [], [
        (2, "", "maquereau en filets|maquereaux en filets", "maquereau", 300), (2, "c. à soupe", "de sauce soja", "soja", 30), (1, "c. à soupe", "de miel", "miel", 20),
        (1, "c. à café", "de gingembre râpé", "epice", 5), (120, "g", "de riz", "riz", 120), (1, "c. à soupe", "de sésame", "graines", 10)],
        ["Cuire le riz.", "Mélanger soja, miel et gingembre.", "Cuire les filets 3 min côté peau, retourner, verser la sauce et laisser réduire 1 min.",
         "Servir sur le riz, parsemer de sésame."], f="Maquereau", c="asie", o="Japon")
    r("bibimbap", "Bibimbap aux épinards et carottes", "Plat", 30, "vege", ["Épinard", "Carotte"], [
        (150, "g", "de riz", "riz", 150), (200, "g", "d'épinards", "epinard", 200), (2, "", "carotte|carottes", "carotte", 200),
        (150, "g", "de champignons", "champignon", 150), (2, "", "œuf|œufs", "oeuf", 110), (1, "c. à soupe", "de sauce soja", "soja", 15),
        (1, "c. à café", "de piment coréen ou de paprika", "epice", 2), (1, "c. à soupe", "d'huile de sésame", "huile", 10)],
        ["Cuire le riz.", "Faire sauter séparément épinards, carottes râpées et champignons 3 min chacun.",
         "Cuire les œufs au plat.", "Répartir le riz, disposer les légumes et l'œuf, assaisonner de soja et de piment."], c="asie", o="Corée")

    # =============== LOT 1 · MAGHREB ET ORIENT ===============
    r("chakchouka", "Chakchouka", "Plat", 30, "vege", ["Poivron", "Tomate"], [
        (2, "", "poivron|poivrons", "poivron", 350), (4, "", "tomate|tomates", "tomate", 450), (1, "", "oignon|oignons", "oignon", 100),
        (4, "", "œuf|œufs", "oeuf", 220), (1, "c. à café", "de cumin", "epice", 2), (1, "c. à café", "de paprika", "epice", 2),
        (2, "c. à soupe", "d'huile d'olive", "huile", 20), S],
        ["Faire revenir oignon et poivrons émincés 8 min dans l'huile avec les épices.", "Ajouter les tomates en dés, cuire 10 min.",
         "Creuser 4 puits, casser les œufs, couvrir et cuire 6 min.", "Assaisonner et servir avec du pain."], c="orient", o="Tunisie")
    r("couscous-hiver", "Couscous de légumes d'hiver", "Plat", 45, "vege", ["Navet", "Carotte"], [
        (150, "g", "de semoule", "semoule", 150), (2, "", "carotte|carottes", "carotte", 200), (2, "", "navet|navets", "navet", 200),
        (200, "g", "de potiron", "potimarron", 200), (200, "g", "de pois chiches cuits", "poischiche", 200), (1, "", "oignon|oignons", "oignon", 100),
        (1, "c. à soupe", "de ras-el-hanout", "epice", 6), (2, "c. à soupe", "d'huile d'olive", "huile", 20), S],
        ["Faire revenir l'oignon dans l'huile avec les épices.", "Ajouter carottes, navets et 1 l d'eau, cuire 20 min.",
         "Ajouter potiron et pois chiches, cuire 10 min.", "Préparer la semoule avec un peu de bouillon, servir avec les légumes, assaisonner."],
        c="orient", o="Maroc")
    r("taboule", "Taboulé libanais", "Entrée", 20, "vege", ["Tomate", "Concombre"], [
        (2, "botte", "de persil plat", "herbe", 60), (1, "brin", "de menthe", "herbe", 10), (40, "g", "de boulgour fin", "boulgour", 40),
        (3, "", "tomate|tomates", "tomate", 350), (0.5, "", "concombre|concombres", "concombre", 150), (1, "", "citron|citrons", "citron", 60),
        (3, "c. à soupe", "d'huile d'olive", "huile", 30), S],
        ["Faire gonfler le boulgour 10 min dans l'eau froide, égoutter.", "Hacher finement persil et menthe.",
         "Couper tomates et concombre en petits dés.", "Mélanger avec le jus de citron et l'huile, assaisonner."], c="orient", o="Liban")
    r("houmous-crudites", "Houmous et bâtonnets de carottes", "Entrée", 10, "vege", ["Carotte"], [
        (250, "g", "de pois chiches cuits", "poischiche", 250), (1, "c. à soupe", "de tahini", "tahini", 15), (1, "", "citron|citrons", "citron", 60),
        (1, "gousse", "d'ail", "ail", 4), (2, "c. à soupe", "d'huile d'olive", "huile", 20), (3, "", "carotte|carottes", "carotte", 300),
        (1, "c. à café", "de cumin", "epice", 2), S],
        ["Mixer pois chiches, tahini, jus de citron, ail et cumin avec 3 c. à soupe d'eau.", "Ajouter l'huile, mixer jusqu'à ce que ce soit lisse.",
         "Assaisonner.", "Servir avec les carottes en bâtonnets."], c="orient", o="Liban")
    r("tajine-agneau-pruneaux", "Tajine d'agneau aux pruneaux et amandes", "Plat", 45, "viande", [], [
        (400, "g", "d'épaule d'agneau en morceaux", "agneau", 400), (100, "g", "de pruneaux", "pruneau", 100), (20, "g", "d'amandes", "amande", 20),
        (1, "", "oignon|oignons", "oignon", 100), (1, "c. à café", "de cannelle", "epice", 2), (1, "c. à café", "de gingembre", "epice", 2),
        (1, "c. à soupe", "d'huile d'olive", "huile", 10), S],
        ["Faire dorer l'agneau avec l'oignon et les épices.", "Couvrir d'eau à hauteur, cuire 30 min à couvert.",
         "Ajouter les pruneaux et cuire 10 min.", "Assaisonner, parsemer d'amandes grillées."], meat="agneau", c="orient", o="Maroc", m=[10, 11, 12, 1, 2, 3])
    r("harira", "Harira aux lentilles et pois chiches", "Soupe", 40, "vege", ["Céleri-rave"], [
        (80, "g", "de lentilles", "lentille", 80), (150, "g", "de pois chiches cuits", "poischiche", 150), (200, "g", "de tomates concassées", "tomate", 200),
        (100, "g", "de céleri", "celeri", 100), (1, "", "oignon|oignons", "oignon", 100), (0.5, "botte", "de coriandre et persil", "herbe", 20),
        (1, "c. à café", "de curcuma et gingembre", "epice", 3), (1, "", "citron|citrons", "citron", 60), S],
        ["Faire revenir oignon et céleri hachés avec les épices.", "Ajouter lentilles, tomates et 1 l d'eau, cuire 25 min.",
         "Ajouter pois chiches et herbes, cuire 5 min.", "Assaisonner, servir avec un filet de citron."], c="orient", o="Maroc")
    r("fattouch", "Fattouch", "Entrée", 15, "vege", ["Concombre", "Tomate"], [
        (2, "", "tomate|tomates", "tomate", 250), (0.5, "", "concombre|concombres", "concombre", 150), (6, "", "radis|radis", "radis", 60),
        (1, "", "pain pita|pains pita", "pain", 70), (1, "c. à café", "de sumac", "epice", 2), (1, "", "citron|citrons", "citron", 60),
        (2, "c. à soupe", "d'huile d'olive", "huile", 20), (1, "brin", "de menthe", "herbe", 5), S],
        ["Griller le pain pita et le casser en morceaux.", "Couper tomates, concombre et radis.",
         "Mélanger jus de citron, huile et sumac, assaisonner.", "Mélanger le tout juste avant de servir."], c="orient", o="Liban")
    r("imam-bayildi", "Aubergines imam bayildi", "Plat", 45, "vege", ["Aubergine", "Tomate"], [
        (2, "", "aubergine|aubergines", "aubergine", 600), (2, "", "oignon|oignons", "oignon", 200), (3, "", "tomate|tomates", "tomate", 350),
        (2, "gousse", "d'ail", "ail", 8), (3, "c. à soupe", "d'huile d'olive", "huile", 30), (0.5, "botte", "de persil", "herbe", 15), S],
        ["Fendre les aubergines et les précuire 15 min au four.", "Faire fondre oignons et ail dans l'huile, ajouter tomates et persil.",
         "Garnir les aubergines de cette farce.", "Cuire 25 min à 180 °C, servir tiède, assaisonner."], c="orient", o="Turquie")
    r("falafels-four", "Falafels au four, sauce tahini", "Plat", 35, "vege", [], [
        (250, "g", "de pois chiches cuits", "poischiche", 250), (1, "", "oignon|oignons", "oignon", 100), (0.5, "botte", "de persil et coriandre", "herbe", 20),
        (1, "c. à café", "de cumin", "epice", 2), (2, "c. à soupe", "de farine", "farine", 20), (2, "c. à soupe", "de tahini", "tahini", 30),
        (1, "", "citron|citrons", "citron", 60), (2, "c. à soupe", "d'huile d'olive", "huile", 20), S],
        ["Mixer pois chiches, oignon, herbes, cumin et farine.", "Former des boulettes, les huiler et cuire 20 min à 200 °C en les retournant.",
         "Mélanger tahini, jus de citron et un peu d'eau.", "Assaisonner et servir avec une salade de saison."], c="orient", o="Liban", m=ALL)
    r("chich-taouk", "Brochettes de poulet chich taouk", "Plat", 30, "viande", ["Poivron"], [
        (300, "g", "de blanc de poulet", "poulet_blanc", 300), (1, "", "yaourt|yaourts", "yaourt", 125), (1, "", "citron|citrons", "citron", 60),
        (2, "gousse", "d'ail", "ail", 8), (1, "c. à café", "de paprika", "epice", 2), (1, "", "poivron|poivrons", "poivron", 200), S],
        ["Mariner le poulet en cubes 1 h avec yaourt, citron, ail et paprika.", "Monter les brochettes avec le poivron.",
         "Griller 12 min en retournant.", "Assaisonner et servir avec du pain pita."], meat="volaille", c="orient", o="Liban")
    r("sardines-chermoula", "Sardines à la chermoula", "Plat", 25, "poisson", ["Tomate"], [
        (8, "", "sardine|sardines", "sardine", 400), (0.5, "botte", "de coriandre et persil", "herbe", 20), (2, "gousse", "d'ail", "ail", 8),
        (1, "c. à café", "de cumin et paprika", "epice", 3), (1, "", "citron|citrons", "citron", 60), (2, "c. à soupe", "d'huile d'olive", "huile", 20),
        (3, "", "tomate|tomates", "tomate", 350), S],
        ["Mixer herbes, ail, épices, jus de citron et huile : c'est la chermoula.", "Badigeonner les sardines vidées de chermoula.",
         "Les cuire 10 min à 220 °C sur les tomates en rondelles.", "Assaisonner et servir."], f="Sardine", c="orient", o="Maroc")

    # =============== LOT 1 · INDE ===============
    r("dal-epinards", "Dal de lentilles corail aux épinards", "Plat", 30, "vege", ["Épinard"], [
        (150, "g", "de lentilles corail", "lentille", 150), (150, "g", "d'épinards", "epinard", 150), (20, "cl", "de lait de coco", "coco", 200),
        (1, "", "oignon|oignons", "oignon", 100), (1, "c. à soupe", "de curry", "epice", 6), (1, "c. à café", "de gingembre", "epice", 3),
        (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Faire revenir l'oignon avec le curry et le gingembre.", "Ajouter lentilles, lait de coco et 40 cl d'eau, cuire 15 min.",
         "Ajouter les épinards 3 min.", "Assaisonner, servir avec du riz ou un pain naan."], c="inde", o="Inde")
    r("aloo-gobi", "Aloo gobi (chou-fleur et pommes de terre)", "Plat", 35, "vege", ["Chou-fleur"], [
        (0.5, "", "chou-fleur|chou-fleurs", "choufleur", 400), (2, "", "pomme de terre|pommes de terre", "pdt", 300), (1, "", "oignon|oignons", "oignon", 100),
        (2, "", "tomate|tomates", "tomate", 200), (1, "c. à café", "de curcuma", "epice", 2), (1, "c. à café", "de garam masala", "epice", 2),
        (2, "c. à soupe", "d'huile", "huile", 20), (0.5, "botte", "de coriandre", "herbe", 10), S],
        ["Faire revenir l'oignon dans l'huile avec les épices.", "Ajouter pommes de terre en dés et bouquets de chou-fleur, enrober.",
         "Ajouter les tomates et un demi-verre d'eau, cuire 20 min à couvert.", "Assaisonner et parsemer de coriandre."], c="inde", o="Inde")
    r("poulet-saag", "Poulet aux épinards (saag)", "Plat", 35, "viande", ["Épinard"], [
        (300, "g", "de blanc de poulet", "poulet_blanc", 300), (300, "g", "d'épinards", "epinard", 300), (1, "", "yaourt|yaourts", "yaourt", 125),
        (1, "", "oignon|oignons", "oignon", 100), (1, "c. à café", "de garam masala", "epice", 2), (1, "c. à café", "de gingembre", "epice", 3),
        (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Faire dorer le poulet en dés dans l'huile avec l'oignon et les épices.", "Ajouter les épinards hachés et un peu d'eau, cuire 10 min.",
         "Hors du feu, ajouter le yaourt.", "Assaisonner et servir avec du riz."], meat="volaille", c="inde", o="Inde")
    r("curry-poisson-coco", "Curry de poisson au coco et épinards", "Plat", 25, "poisson", ["Épinard"], [
        (2, "", "pavé de cabillaud|pavés de cabillaud", "cabillaud", 300), (20, "cl", "de lait de coco", "coco", 200), (150, "g", "d'épinards", "epinard", 150),
        (1, "", "oignon|oignons", "oignon", 100), (1, "c. à soupe", "de curry", "epice", 6), (1, "", "citron vert|citrons verts", "citron", 30),
        (120, "g", "de riz basmati", "riz", 120), S],
        ["Cuire le riz.", "Faire revenir l'oignon avec le curry, ajouter le lait de coco.",
         "Poser le poisson en morceaux et les épinards, cuire 8 min à couvert.", "Ajouter le citron vert, assaisonner."], f="Cabillaud", c="inde", o="Inde (Kerala)")
    r("raita", "Raïta de concombre", "Entrée", 10, "vege", ["Concombre"], [
        (1, "", "concombre|concombres", "concombre", 300), (2, "", "yaourt|yaourts", "yaourt", 250), (1, "c. à café", "de cumin grillé", "epice", 2),
        (1, "brin", "de menthe", "herbe", 5), S],
        ["Râper le concombre et le presser.", "Mélanger au yaourt avec le cumin et la menthe.", "Assaisonner.", "Servir frais."], c="inde", o="Inde")
    r("biryani-legumes", "Biryani de légumes", "Plat", 40, "vege", ["Chou-fleur", "Carotte"], [
        (150, "g", "de riz basmati", "riz", 150), (200, "g", "de chou-fleur", "choufleur", 200), (2, "", "carotte|carottes", "carotte", 200),
        (1, "", "oignon|oignons", "oignon", 100), (1, "c. à soupe", "d'épices biryani ou de garam masala", "epice", 6), (1, "", "yaourt|yaourts", "yaourt", 125),
        (20, "g", "de raisins secs", "raisin_sec", 20), (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Faire dorer l'oignon émincé dans l'huile, en garder la moitié.", "Ajouter légumes et épices, puis le yaourt, cuire 10 min.",
         "Ajouter le riz rincé, les raisins et 30 cl d'eau, cuire 15 min à couvert.", "Assaisonner, garnir d'oignon doré."], c="inde", o="Inde")

    # =============== LOT 2 · AMÉRIQUES ===============
    r("chili-sin-carne", "Chili sin carne", "Plat", 35, "vege", ["Poivron", "Tomate"], [
        (250, "g", "de haricots rouges cuits", "haricotblanc", 250), (1, "", "poivron|poivrons", "poivron", 200), (3, "", "tomate|tomates", "tomate", 350),
        (100, "g", "de maïs", "mais", 100), (1, "", "oignon|oignons", "oignon", 100), (1, "c. à café", "de cumin et piment", "epice", 3),
        (100, "g", "de riz", "riz", 100), (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Cuire le riz.", "Faire revenir oignon et poivron avec les épices.", "Ajouter tomates, haricots et maïs, cuire 20 min.",
         "Assaisonner et servir avec le riz."], c="ameriques", o="Mexique")
    r("chili-con-carne", "Chili con carne", "Plat", 40, "viande", [], [
        (250, "g", "de bœuf haché", "boeuf_maigre", 250), (250, "g", "de haricots rouges cuits", "haricotblanc", 250), (400, "g", "de tomates concassées", "tomate", 400),
        (1, "", "oignon|oignons", "oignon", 100), (1, "c. à café", "de cumin et piment", "epice", 3), (100, "g", "de riz", "riz", 100),
        (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Cuire le riz.", "Faire dorer l'oignon puis le bœuf avec les épices.", "Ajouter tomates et haricots, cuire 25 min.",
         "Assaisonner et servir avec le riz."], meat="boeuf", c="ameriques", o="Tex-Mex", m=[10, 11, 12, 1, 2, 3])
    r("tacos-poisson", "Tacos de poisson et chou croquant", "Plat", 25, "poisson", ["Chou"], [
        (2, "", "filet de cabillaud|filets de cabillaud", "cabillaud", 300), (4, "", "tortilla de maïs|tortillas de maïs", "tortilla", 120),
        (150, "g", "de chou finement émincé", "chou", 150), (1, "", "citron vert|citrons verts", "citron", 30), (2, "c. à soupe", "de yaourt", "yaourt", 40),
        (1, "c. à café", "de paprika fumé", "epice", 2), (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Saupoudrer le poisson de paprika et le cuire 3 min de chaque côté.", "Mélanger le chou avec le jus de citron vert.",
         "Chauffer les tortillas.", "Garnir de poisson émietté, de chou et de yaourt, assaisonner."], f="Cabillaud", c="ameriques", o="Mexique")
    r("ceviche", "Ceviche de daurade", "Entrée", 20, "poisson", [], [
        (250, "g", "de filet de daurade très frais", "daurade", 250), (3, "", "citron vert|citrons verts", "citron", 90), (0.5, "", "oignon rouge|oignons rouges", "oignon", 50),
        (0.5, "botte", "de coriandre", "herbe", 10), (1, "pincée", "de piment", "epice", 0), S],
        ["Couper le poisson en petits dés.", "Le couvrir de jus de citron vert avec l'oignon émincé, 15 min au frais.",
         "Égoutter un peu, ajouter coriandre et piment.", "Assaisonner et servir aussitôt."], f="Daurade", c="ameriques", o="Pérou")
    r("salade-mais-haricots", "Salade de maïs, tomates et haricots noirs", "Entrée", 15, "vege", ["Maïs", "Tomate"], [
        (1, "", "épi de maïs|épis de maïs", "mais", 200), (2, "", "tomate|tomates", "tomate", 250), (150, "g", "de haricots noirs cuits", "haricotblanc", 150),
        (1, "", "citron vert|citrons verts", "citron", 30), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (0.5, "botte", "de coriandre", "herbe", 10), S],
        ["Cuire l'épi 10 min et égrener.", "Couper les tomates en dés.", "Mélanger avec les haricots, le jus de citron et l'huile.",
         "Assaisonner et parsemer de coriandre."], c="ameriques", o="Mexique")
    r("soupe-coco-potiron", "Soupe de potiron et patate douce au coco", "Soupe", 30, "vege", ["Potimarron"], [
        (400, "g", "de potiron", "potimarron", 400), (1, "", "patate douce|patates douces", "patatedouce", 250), (20, "cl", "de lait de coco", "coco", 200),
        (1, "", "oignon|oignons", "oignon", 100), (1, "c. à café", "de gingembre", "epice", 3), (1, "pincée", "de piment", "epice", 0), S],
        ["Faire revenir l'oignon avec le gingembre.", "Ajouter potiron et patate douce en dés et 60 cl d'eau, cuire 20 min.",
         "Mixer avec le lait de coco.", "Assaisonner et relever d'une pincée de piment."], c="ameriques", o="Antilles")
    r("poulet-mais-grille", "Poulet grillé, épis de maïs et salsa", "Plat", 35, "viande", ["Maïs", "Tomate"], [
        (2, "", "cuisse de poulet|cuisses de poulet", "poulet_cuisse", 450), (2, "", "épi de maïs|épis de maïs", "mais", 400), (2, "", "tomate|tomates", "tomate", 250),
        (0.5, "", "oignon rouge|oignons rouges", "oignon", 50), (1, "c. à café", "de paprika fumé", "epice", 2), (1, "", "citron vert|citrons verts", "citron", 30), S],
        ["Frotter le poulet de paprika, le griller 25 min en le retournant.", "Griller les épis 10 min.",
         "Couper tomates et oignon en petits dés avec le jus de citron vert : c'est la salsa.", "Assaisonner et servir."],
        meat="volaille", c="ameriques", o="États-Unis")
    r("moqueca", "Moqueca de poisson au coco", "Plat", 30, "poisson", [], [
        (2, "", "pavé de cabillaud|pavés de cabillaud", "cabillaud", 300), (20, "cl", "de lait de coco", "coco", 200), (400, "g", "de tomates concassées", "tomate", 400),
        (1, "", "oignon|oignons", "oignon", 100), (1, "", "citron vert|citrons verts", "citron", 30), (0.5, "botte", "de coriandre", "herbe", 10),
        (120, "g", "de riz", "riz", 120), S],
        ["Cuire le riz.", "Faire fondre l'oignon, ajouter tomates et lait de coco, cuire 10 min.",
         "Poser le poisson, couvrir et cuire 8 min.", "Ajouter citron vert et coriandre, assaisonner."], f="Cabillaud", c="ameriques", o="Brésil")
    r("quesadillas-courgettes", "Quesadillas aux courgettes", "Plat", 20, "vege", ["Courgette"], [
        (4, "", "tortilla de blé|tortillas de blé", "tortilla", 160), (2, "", "courgette|courgettes", "courgette", 400), (80, "g", "de cheddar ou de tomme râpés", "tomme", 80),
        (1, "c. à café", "de cumin", "epice", 2), (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Râper les courgettes et les poêler 6 min avec le cumin.", "Garnir deux tortillas de courgettes et de fromage, couvrir avec les deux autres.",
         "Dorer 3 min de chaque côté à la poêle.", "Couper en parts et servir."], c="ameriques", o="Mexique")

    # =============== LOT 2 · AFRIQUE ===============
    r("mafe", "Mafé de poulet à la patate douce", "Plat", 45, "viande", [], [
        (2, "", "haut de cuisse de poulet|hauts de cuisse de poulet", "poulet_cuisse", 400), (2, "c. à soupe", "de beurre de cacahuète", "arachide", 40),
        (200, "g", "de tomates concassées", "tomate", 200), (1, "", "patate douce|patates douces", "patatedouce", 300), (1, "", "oignon|oignons", "oignon", 100),
        (2, "", "carotte|carottes", "carotte", 150), (100, "g", "de riz", "riz", 100), (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Faire dorer le poulet et l'oignon dans l'huile.", "Ajouter tomates, beurre de cacahuète délayé et 50 cl d'eau.",
         "Ajouter patate douce et carottes, cuire 30 min.", "Assaisonner, servir avec le riz."], meat="volaille", c="afrique", o="Mali · Sénégal",
        m=[10, 11, 12, 1, 2, 3])
    r("yassa", "Poulet yassa", "Plat", 45, "viande", ["Citron"], [
        (2, "", "cuisse de poulet|cuisses de poulet", "poulet_cuisse", 450), (3, "", "oignon|oignons", "oignon", 350), (2, "", "citron|citrons", "citron", 120),
        (1, "c. à soupe", "de moutarde", "moutarde", 15), (1, "c. à soupe", "d'huile", "huile", 10), (100, "g", "de riz", "riz", 100), S],
        ["Mariner le poulet avec les oignons émincés, le jus de citron et la moutarde (1 h si possible).", "Dorer le poulet, réserver.",
         "Faire fondre longuement les oignons de la marinade, remettre le poulet et un peu d'eau, cuire 25 min.", "Assaisonner, servir avec le riz."],
        meat="volaille", c="afrique", o="Sénégal")
    r("riz-poisson-legumes", "Riz au poisson et légumes", "Plat", 45, "poisson", ["Carotte", "Chou"], [
        (2, "", "filet de merlan|filets de merlan", "merlan", 300), (150, "g", "de riz", "riz", 150), (2, "", "carotte|carottes", "carotte", 200),
        (200, "g", "de chou", "chou", 200), (1, "", "oignon|oignons", "oignon", 100), (2, "c. à soupe", "de concentré de tomate", "tomate", 30),
        (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Faire revenir l'oignon et le concentré de tomate.", "Ajouter carottes, chou et 60 cl d'eau, cuire 15 min.",
         "Ajouter le riz, cuire 15 min, poser le poisson les 8 dernières minutes.", "Assaisonner et servir."],
        f="Merlan", c="afrique", o="Sénégal (thiéboudienne)")
    r("attieke-poisson", "Attiéké et poisson grillé", "Plat", 30, "poisson", ["Tomate"], [
        (2, "", "maquereau|maquereaux", "maquereau", 400), (200, "g", "d'attiéké (ou de semoule)", "semoule", 200), (2, "", "tomate|tomates", "tomate", 250),
        (1, "", "oignon|oignons", "oignon", 100), (1, "", "citron vert|citrons verts", "citron", 30), (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Griller les maquereaux 6 min de chaque côté.", "Réchauffer l'attiéké à la vapeur.",
         "Couper tomates et oignon en dés avec le jus de citron vert.", "Assaisonner, servir le poisson sur l'attiéké avec la salade."],
        f="Maquereau", c="afrique", o="Côte d'Ivoire")
    r("misir-wot", "Lentilles épicées (misir wot)", "Plat", 35, "vege", ["Carotte"], [
        (150, "g", "de lentilles corail", "lentille", 150), (1, "", "oignon|oignons", "oignon", 100), (1, "", "carotte|carottes", "carotte", 100),
        (1, "c. à soupe", "de berbéré ou de paprika épicé", "epice", 6), (200, "g", "de tomates concassées", "tomate", 200), (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Faire fondre longuement l'oignon haché dans l'huile.", "Ajouter les épices, la carotte râpée et les tomates.",
         "Ajouter lentilles et 50 cl d'eau, cuire 20 min.", "Assaisonner, servir avec du riz ou du pain."], c="afrique", o="Éthiopie")
    r("salade-haricots-cacahuetes", "Salade de haricots verts aux cacahuètes", "Entrée", 20, "vege", ["Haricot vert", "Tomate"], [
        (300, "g", "de haricots verts", "haricotvert", 300), (2, "", "tomate|tomates", "tomate", 250), (30, "g", "de cacahuètes grillées", "arachide", 30),
        (1, "", "citron vert|citrons verts", "citron", 30), (1, "c. à soupe", "d'huile", "huile", 10), (1, "pincée", "de piment", "epice", 0), S],
        ["Cuire les haricots 8 min et les refroidir.", "Couper les tomates.", "Mélanger avec le jus de citron vert, l'huile et le piment.",
         "Assaisonner et parsemer de cacahuètes concassées."], c="afrique", o="Afrique de l'Ouest")

    # =============== LOT 3 · DESSERTS DU MONDE ===============
    r("kheer", "Kheer, riz au lait à la cardamome", "Dessert", 35, "vege", [], [
        (50, "g", "de riz", "riz", 50), (50, "cl", "de lait", "lait", 500), (30, "g", "de sucre", "sucre", 30), (3, "", "gousse de cardamome|gousses de cardamome", "epice", 1),
        (15, "g", "de pistaches", "amande", 15)],
        ["Cuire le riz dans le lait avec la cardamome écrasée, 30 min à feu doux en remuant.", "Ajouter le sucre.",
         "Laisser tiédir.", "Servir parsemé de pistaches concassées."], sweet=True, c="inde", o="Inde", m=ALL)
    r("mouhalabieh", "Mouhalabieh à la fleur d'oranger", "Dessert", 15, "vege", [], [
        (40, "cl", "de lait", "lait", 400), (30, "g", "de maïzena", "farine", 30), (30, "g", "de sucre", "sucre", 30),
        (1, "c. à soupe", "d'eau de fleur d'oranger", "epice", 15), (15, "g", "de pistaches", "amande", 15)],
        ["Délayer la maïzena dans un peu de lait froid.", "Chauffer le reste du lait avec le sucre, ajouter la maïzena et épaissir en fouettant.",
         "Ajouter la fleur d'oranger, verser dans des coupes.", "Réserver 2 h au frais, parsemer de pistaches."], sweet=True, c="orient", o="Liban", m=ALL)
    r("riz-coco-poires", "Riz au lait de coco et poires", "Dessert", 30, "vege", ["Poire"], [
        (60, "g", "de riz rond", "riz", 60), (20, "cl", "de lait de coco", "coco", 200), (20, "cl", "de lait", "lait", 200), (25, "g", "de sucre", "sucre", 25),
        (2, "", "poire|poires", "poire", 300)],
        ["Cuire le riz dans le lait et le lait de coco 25 min à feu doux.", "Ajouter le sucre.",
         "Poêler les poires en dés 5 min.", "Servir le riz tiède avec les poires."], sweet=True, c="asie", o="Thaïlande")
    r("tarta-santiago", "Gâteau aux amandes (tarta de Santiago)", "Dessert", 45, "vege", [], [
        (125, "g", "de poudre d'amande", "amande", 125), (100, "g", "de sucre", "sucre", 100), (3, "", "œuf|œufs", "oeuf", 165),
        (1, "", "citron (zeste)|citrons (zeste)", "citron", 10), (1, "c. à soupe", "de sucre glace", "sucre", 10)],
        ["Fouetter les œufs et le sucre.", "Ajouter la poudre d'amande et le zeste.", "Verser dans un moule de 18 cm et cuire 30 min à 180 °C.",
         "Saupoudrer de sucre glace."], sweet=True, c="med", o="Espagne", m=ALL, parts=6)
    r("tiramisu-fraises", "Tiramisu aux fraises", "Dessert", 25, "vege", ["Fraise"], [
        (250, "g", "de fraises", "fraise", 250), (125, "g", "de mascarpone", "mascarpone", 125), (1, "", "œuf|œufs", "oeuf", 55),
        (30, "g", "de sucre", "sucre", 30), (6, "", "biscuit cuillère|biscuits cuillère", "biscuit", 50)],
        ["Fouetter le jaune avec le sucre, ajouter le mascarpone, puis le blanc monté en neige.", "Mixer la moitié des fraises en coulis.",
         "Tremper les biscuits dans le coulis, alterner avec la crème et les fraises en morceaux.", "Réserver 3 h au frais."], sweet=True, c="med", o="Italie")
    r("panna-cotta-framboises", "Panna cotta aux framboises", "Dessert", 20, "vege", ["Framboise"], [
        (20, "cl", "de crème liquide", "creme", 200), (10, "cl", "de lait", "lait", 100), (25, "g", "de sucre", "sucre", 25),
        (1, "g", "d'agar-agar", "epice", 1), (150, "g", "de framboises", "framboise", 150)],
        ["Porter crème, lait, sucre et agar-agar à ébullition 1 min.", "Verser dans des verrines, laisser prendre 2 h au frais.",
         "Écraser la moitié des framboises en coulis.", "Servir avec le coulis et les framboises entières."], sweet=True, c="med", o="Italie")
    r("pommes-four", "Pommes au four à la cannelle", "Dessert", 35, "vege", ["Pomme"], [
        (2, "", "pomme|pommes", "pomme", 360), (20, "g", "de noix", "noix", 20), (1, "c. à soupe", "de miel", "miel", 20),
        (1, "c. à café", "de cannelle", "epice", 2), (10, "g", "de beurre", "beurre", 10)],
        ["Évider les pommes.", "Les garnir de noix, miel, cannelle et beurre.", "Cuire 30 min à 180 °C.", "Servir tièdes avec leur jus."],
        sweet=True, c="ameriques", o="États-Unis")
    r("crumble-prunes", "Crumble aux prunes", "Dessert", 40, "vege", ["Prune"], [
        (400, "g", "de prunes", "prune", 400), (50, "g", "de farine", "farine", 50), (40, "g", "de beurre", "beurre", 40), (40, "g", "de sucre", "sucre", 40),
        (20, "g", "de flocons d'avoine", "farine", 20)],
        ["Dénoyauter les prunes et les mettre dans un plat.", "Sabler farine, beurre, sucre et flocons.", "Couvrir les fruits.", "Cuire 30 min à 180 °C."],
        sweet=True, c="med", o="Royaume-Uni")
    r("kakis-gingembre", "Kakis au sirop de gingembre", "Dessert", 15, "vege", ["Kaki"], [
        (2, "", "kaki|kakis", "kaki", 350), (20, "g", "de sucre", "sucre", 20), (1, "c. à café", "de gingembre râpé", "epice", 5),
        (1, "", "citron vert|citrons verts", "citron", 30)],
        ["Faire un sirop avec 10 cl d'eau, le sucre et le gingembre (3 min).", "Ajouter le jus de citron vert, laisser refroidir.",
         "Couper les kakis en quartiers.", "Arroser de sirop et servir frais."], sweet=True, c="asie", o="Japon")
    r("basbousa-orange", "Gâteau de semoule à l'orange (basboussa)", "Dessert", 45, "vege", ["Orange"], [
        (120, "g", "de semoule fine", "semoule", 120), (1, "", "yaourt|yaourts", "yaourt", 125), (60, "g", "de sucre", "sucre", 60),
        (40, "g", "de beurre fondu", "beurre", 40), (2, "", "orange|oranges", "orange", 300), (20, "g", "d'amandes", "amande", 20)],
        ["Mélanger semoule, yaourt, 30 g de sucre, beurre et zeste d'une orange.", "Verser dans un petit moule, poser les amandes, cuire 30 min à 180 °C.",
         "Chauffer le jus des oranges avec le reste du sucre.", "Arroser le gâteau chaud de ce sirop."], sweet=True, c="orient", o="Égypte", parts=6)
    r("tarte-potiron", "Tarte au potiron épicée (pumpkin pie)", "Dessert", 55, "vege", ["Potimarron"], [
        (1, "", "pâte brisée|pâtes brisées", "pate", 230), (400, "g", "de potiron cuit en purée", "potimarron", 400), (2, "", "œuf|œufs", "oeuf", 110),
        (60, "g", "de sucre roux", "sucre", 60), (10, "cl", "de crème", "creme", 100), (1, "c. à café", "de cannelle et gingembre", "epice", 3)],
        ["Foncer un moule avec la pâte.", "Mélanger la purée de potiron, les œufs, le sucre, la crème et les épices.",
         "Verser sur la pâte.", "Cuire 40 min à 180 °C, servir tiède ou froid."], sweet=True, c="ameriques", o="États-Unis", parts=6)
    r("lassi-fraises", "Lassi aux fraises", "Dessert", 5, "vege", ["Fraise"], [
        (200, "g", "de fraises", "fraise", 200), (2, "", "yaourt|yaourts", "yaourt", 250), (10, "cl", "de lait", "lait", 100),
        (1, "c. à soupe", "de miel", "miel", 20), (1, "pincée", "de cardamome", "epice", 0)],
        ["Laver les fraises.", "Mixer avec le yaourt, le lait, le miel et la cardamome.", "Ajouter des glaçons si on le souhaite.", "Servir aussitôt."],
        sweet=True, c="inde", o="Inde")
