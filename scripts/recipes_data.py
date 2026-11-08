"""Base de recettes de SEASON (pour 2 personnes). Chaque ingrédient :
(quantité, unité, nom « sing|plur », aliment pour les kcal, grammes pour 2 personnes).
Les mois sont calculés à partir des produits de saison (champ u) et des poissons (champ f)."""

S = (None, "", "Sel, poivre", "sel", 0)   # retiré en mode « sans sel ajouté »

R = []
def r(id, n, k, t, reg, u, i, s, meat=None, f=None, sweet=False, tip=None, m=None, parts=2):
    """parts : nombre de parts obtenues (pour les kcal par part) ; les quantités restent prévues pour 2 personnes."""
    R.append(dict(id=id, n=n, k=k, t=t, reg=reg, u=u, i=i, s=s, meat=meat, f=f, sweet=sweet, tip=tip, m=m, parts=parts))

# ---------------- Végétarien : plats, soupes, entrées ----------------
r("veloute-potimarron", "Velouté de potimarron au cumin", "Soupe", 25, "vege", ["Potimarron"], [
    (600, "g", "de potimarron, avec la peau", "potimarron", 600), (1, "", "oignon|oignons", "oignon", 100),
    (1, "", "carotte|carottes", "carotte", 100), (1, "c. à café", "de cumin", "epice", 2),
    (50, "cl", "de bouillon de légumes", "bouillon", 500), (2, "c. à soupe", "de crème fraîche", "creme", 30),
    (1, "c. à soupe", "d'huile d'olive", "huile", 10), (20, "g", "de graines de courge", "graines", 20), S],
    ["Couper le potimarron, l'oignon et la carotte en morceaux.", "Faire revenir l'oignon 3 min dans l'huile avec le cumin.",
     "Ajouter les légumes et le bouillon, cuire 18 min à couvert.", "Mixer avec la crème, assaisonner, parsemer de graines de courge."],
    tip="Le cumin et les graines grillées donnent du goût sans sel.")
r("gratin-choufleur", "Gratin de chou-fleur à la tomme", "Plat", 40, "vege", ["Chou-fleur"], [
    (1, "", "petit chou-fleur|petits chou-fleurs", "choufleur", 600), (30, "cl", "de lait", "lait", 300),
    (20, "g", "de beurre", "beurre", 20), (20, "g", "de farine", "farine", 20), (60, "g", "de tomme râpée", "tomme", 60),
    (1, "pincée", "de muscade", "epice", 0), S],
    ["Cuire les bouquets de chou-fleur 8 min à la vapeur.", "Faire fondre le beurre, ajouter la farine puis le lait en fouettant jusqu'à épaississement.",
     "Assaisonner la sauce avec la muscade.", "Mettre le chou-fleur dans un plat, napper, couvrir de tomme et gratiner 20 min à 200 °C."])
r("risotto-champignons", "Risotto aux champignons et persil", "Plat", 35, "vege", ["Champignons"], [
    (150, "g", "de riz arborio", "riz", 150), (250, "g", "de champignons de Paris", "champignon", 250), (1, "", "échalote|échalotes", "oignon", 40),
    (70, "cl", "de bouillon de légumes chaud", "bouillon", 700), (10, "cl", "de vin blanc", "vin", 100), (30, "g", "de parmesan râpé", "parmesan", 30),
    (1, "c. à soupe", "d'huile d'olive", "huile", 10), (0.5, "botte", "de persil", "herbe", 15), S],
    ["Faire revenir l'échalote dans l'huile, ajouter le riz et le nacrer 2 min.", "Verser le vin, laisser absorber.",
     "Ajouter le bouillon louche par louche pendant 18 min en remuant.", "Poêler les champignons à part, les mélanger au riz avec le parmesan et le persil, assaisonner."])
r("curry-poischiches", "Curry de pois chiches, patate douce et épinards", "Plat", 30, "vege", ["Épinard"], [
    (250, "g", "de pois chiches cuits", "poischiche", 250), (1, "", "patate douce|patates douces", "patatedouce", 300),
    (100, "g", "de pousses d'épinards", "epinard", 100), (20, "cl", "de lait de coco", "coco", 200), (1, "", "oignon|oignons", "oignon", 100),
    (1, "c. à soupe", "de curry", "epice", 6), (1, "c. à soupe", "d'huile d'olive", "huile", 10), S],
    ["Faire revenir l'oignon émincé dans l'huile avec le curry.", "Ajouter la patate douce en dés et le lait de coco, cuire 15 min.",
     "Ajouter les pois chiches et les épinards, cuire 3 min.", "Assaisonner et servir avec un peu de riz si on le souhaite."],
    tip="Le curry et un trait de citron suffisent à relever le plat.")
r("soupe-poireaux", "Soupe de poireaux et pommes de terre", "Soupe", 30, "vege", ["Poireau"], [
    (2, "", "poireau|poireaux", "poireau", 300), (2, "", "pomme de terre|pommes de terre", "pdt", 300),
    (70, "cl", "de bouillon de légumes", "bouillon", 700), (1, "c. à soupe", "d'huile d'olive", "huile", 10),
    (2, "c. à soupe", "de crème fraîche", "creme", 30), S],
    ["Émincer les poireaux et couper les pommes de terre en dés.", "Faire suer les poireaux 5 min dans l'huile.",
     "Ajouter les pommes de terre et le bouillon, cuire 20 min.", "Mixer avec la crème et assaisonner."])
r("salade-endives-poire", "Salade d'endives, poire et noix", "Entrée", 10, "vege", ["Endive", "Poire"], [
    (2, "", "endive|endives", "endive", 200), (1, "", "poire|poires", "poire", 150), (30, "g", "de cerneaux de noix", "noix", 30),
    (40, "g", "de bleu des Causses", "roquefort", 40), (1, "c. à soupe", "d'huile de noix", "huile", 10), (1, "c. à café", "de vinaigre de cidre", "epice", 5), S],
    ["Couper les endives en rondelles et la poire en lamelles.", "Émietter le fromage et concasser les noix.",
     "Mélanger l'huile et le vinaigre, assaisonner.", "Mélanger le tout au moment de servir."])
r("lentilles-carottes", "Lentilles vertes aux carottes et cumin", "Plat", 35, "vege", ["Carotte"], [
    (150, "g", "de lentilles vertes du Puy", "lentille", 150), (2, "", "carotte|carottes", "carotte", 200), (1, "", "oignon|oignons", "oignon", 100),
    (1, "c. à café", "de cumin", "epice", 2), (1, "", "feuille de laurier|feuilles de laurier", "herbe", 1), (1, "c. à soupe", "d'huile d'olive", "huile", 10),
    (0.5, "botte", "de persil", "herbe", 15), S],
    ["Rincer les lentilles.", "Faire revenir l'oignon et les carottes en rondelles dans l'huile avec le cumin.",
     "Ajouter les lentilles, le laurier et 3 fois leur volume d'eau, cuire 25 min.", "Égoutter si besoin, assaisonner, parsemer de persil."],
    tip="Ne pas saler l'eau de cuisson : les lentilles restent plus tendres.")
r("tarte-poireaux-chevre", "Tarte fine aux poireaux et chèvre", "Plat", 40, "vege", ["Poireau"], [
    (1, "", "pâte brisée|pâtes brisées", "pate", 230), (3, "", "poireau|poireaux", "poireau", 450), (100, "g", "de chèvre frais", "chevre", 100),
    (2, "", "œuf|œufs", "oeuf", 110), (10, "cl", "de crème fraîche", "creme", 100), (1, "c. à soupe", "d'huile d'olive", "huile", 10), S],
    ["Émincer les poireaux et les faire fondre 10 min dans l'huile.", "Étaler la pâte dans un moule.",
     "Battre les œufs et la crème, assaisonner, ajouter les poireaux.", "Verser sur la pâte, émietter le chèvre et cuire 25 min à 190 °C."], parts=4)
r("orecchiette-brocoli", "Orecchiette au brocoli, ail et citron", "Plat", 20, "vege", ["Brocoli"], [
    (180, "g", "d'orecchiette", "pates", 180), (1, "", "brocoli|brocolis", "brocoli", 350), (2, "gousse", "d'ail", "ail", 8),
    (1, "", "citron (zeste et jus)|citrons (zeste et jus)", "citron", 60), (2, "c. à soupe", "d'huile d'olive", "huile", 20),
    (25, "g", "de parmesan râpé", "parmesan", 25), (1, "pincée", "de piment", "epice", 0), S],
    ["Cuire les pâtes avec les bouquets de brocoli les 5 dernières minutes.", "Faire dorer l'ail émincé dans l'huile avec le piment.",
     "Égoutter, mélanger avec l'huile à l'ail, le zeste et le jus de citron.", "Assaisonner et servir avec le parmesan."])
r("veloute-panais-pomme", "Velouté de panais et pomme", "Soupe", 30, "vege", ["Panais", "Pomme"], [
    (400, "g", "de panais", "panais", 400), (1, "", "pomme|pommes", "pomme", 150), (1, "", "oignon|oignons", "oignon", 100),
    (60, "cl", "de bouillon de légumes", "bouillon", 600), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "pincée", "de muscade", "epice", 0), S],
    ["Éplucher et couper panais, pomme et oignon.", "Faire revenir l'oignon dans l'huile.",
     "Ajouter panais, pomme et bouillon, cuire 20 min.", "Mixer, assaisonner et râper un peu de muscade."])
r("salade-betterave-orange", "Salade de betteraves, orange et chèvre", "Entrée", 10, "vege", ["Betterave", "Orange"], [
    (2, "", "betterave cuite|betteraves cuites", "betterave", 250), (1, "", "orange|oranges", "orange", 150), (60, "g", "de chèvre frais", "chevre", 60),
    (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "brin", "de menthe", "herbe", 3), S],
    ["Couper les betteraves en dés.", "Peler l'orange à vif et la couper en quartiers en gardant le jus.",
     "Mélanger le jus et l'huile, assaisonner.", "Disposer betteraves et orange, émietter le chèvre, ajouter la menthe."])
r("omelette-asperges", "Omelette aux asperges et parmesan", "Plat", 20, "vege", ["Asperge"], [
    (8, "", "asperge verte|asperges vertes", "asperge", 250), (4, "", "œuf|œufs", "oeuf", 220), (20, "g", "de parmesan râpé", "parmesan", 20),
    (1, "c. à soupe", "d'huile d'olive", "huile", 10), (0.5, "botte", "de ciboulette", "herbe", 10), S],
    ["Couper les asperges en tronçons et les poêler 6 min dans l'huile.", "Battre les œufs avec le parmesan et la ciboulette, assaisonner.",
     "Verser sur les asperges et cuire 4 min à feu doux.", "Plier l'omelette et servir aussitôt."])
r("pates-printanieres", "Pâtes printanières aux petits pois, fèves et menthe", "Plat", 25, "vege", ["Petits pois", "Fèves"], [
    (180, "g", "de linguine", "pates", 180), (150, "g", "de petits pois écossés", "petitspois", 150), (150, "g", "de fèves écossées", "feve", 150),
    (60, "g", "de ricotta", "ricotta", 60), (1, "", "citron (zeste)|citrons (zeste)", "citron", 20), (2, "c. à soupe", "d'huile d'olive", "huile", 20),
    (1, "brin", "de menthe", "herbe", 5), S],
    ["Cuire les pâtes ; ajouter petits pois et fèves 3 min avant la fin.", "Égoutter en gardant un peu d'eau de cuisson.",
     "Mélanger avec l'huile, la ricotta, le zeste et un peu d'eau de cuisson.", "Assaisonner et parsemer de menthe ciselée."])
r("salade-radis-concombre", "Salade de radis et concombre au yaourt", "Entrée", 10, "vege", ["Radis", "Concombre"], [
    (1, "botte", "de radis", "radis", 200), (1, "", "concombre|concombres", "concombre", 300), (1, "", "yaourt grec|yaourts grecs", "yaourt", 150),
    (1, "gousse", "d'ail", "ail", 4), (1, "brin", "d'aneth ou de menthe", "herbe", 5), S],
    ["Couper radis et concombre en fines rondelles.", "Mélanger le yaourt avec l'ail râpé et les herbes.",
     "Assaisonner la sauce.", "Mélanger avec les légumes juste avant de servir."])
r("ratatouille", "Ratatouille", "Plat", 45, "vege", ["Aubergine", "Courgette", "Poivron", "Tomate"], [
    (1, "", "aubergine|aubergines", "aubergine", 300), (1, "", "courgette|courgettes", "courgette", 250), (1, "", "poivron|poivrons", "poivron", 200),
    (3, "", "tomate|tomates", "tomate", 400), (1, "", "oignon|oignons", "oignon", 100), (2, "gousse", "d'ail", "ail", 8),
    (3, "c. à soupe", "d'huile d'olive", "huile", 30), (1, "brin", "de thym", "herbe", 2), S],
    ["Couper tous les légumes en dés.", "Faire revenir l'oignon et le poivron 5 min dans l'huile, puis l'aubergine 5 min.",
     "Ajouter courgette, tomates, ail et thym.", "Cuire 30 min à feu doux à couvert et assaisonner."],
    tip="Le thym, l'ail et une cuisson lente donnent tout le goût.")
r("tian-provencal", "Tian de courgettes et tomates au thym", "Plat", 50, "vege", ["Courgette", "Tomate"], [
    (2, "", "courgette|courgettes", "courgette", 400), (4, "", "tomate|tomates", "tomate", 450), (1, "", "oignon|oignons", "oignon", 100),
    (2, "c. à soupe", "d'huile d'olive", "huile", 20), (1, "brin", "de thym", "herbe", 2), (1, "gousse", "d'ail", "ail", 4), S],
    ["Émincer l'oignon et le répartir au fond d'un plat avec l'ail.", "Couper courgettes et tomates en rondelles et les ranger en alternance.",
     "Arroser d'huile, parsemer de thym, assaisonner.", "Cuire 40 min à 180 °C."])
r("gaspacho", "Gaspacho de tomates et poivron", "Soupe", 15, "vege", ["Tomate", "Poivron", "Concombre"], [
    (600, "g", "de tomates bien mûres", "tomate", 600), (0.5, "", "poivron rouge|poivrons rouges", "poivron", 100), (0.5, "", "concombre|concombres", "concombre", 150),
    (1, "gousse", "d'ail", "ail", 4), (2, "c. à soupe", "d'huile d'olive", "huile", 20), (1, "c. à soupe", "de vinaigre de Xérès", "epice", 10), S],
    ["Couper tous les légumes en morceaux.", "Mixer finement avec l'ail, l'huile et le vinaigre.",
     "Assaisonner, ajouter un peu d'eau froide si c'est trop épais.", "Réserver 1 h au frais avant de servir."])
r("salade-tomate-peche", "Salade de tomates, pêches et mozzarella", "Entrée", 10, "vege", ["Tomate", "Pêche"], [
    (2, "", "tomate|tomates", "tomate", 300), (1, "", "pêche|pêches", "peche", 150), (125, "g", "de mozzarella", "mozzarella", 125),
    (1, "c. à soupe", "d'huile d'olive", "huile", 10), (4, "", "feuille de basilic|feuilles de basilic", "herbe", 2), S],
    ["Couper tomates et pêche en quartiers.", "Déchirer la mozzarella.",
     "Disposer le tout, arroser d'huile, assaisonner.", "Parsemer de basilic."])
r("aubergines-yaourt", "Aubergines rôties, yaourt à l'ail et menthe", "Plat", 35, "vege", ["Aubergine"], [
    (2, "", "aubergine|aubergines", "aubergine", 600), (1, "", "yaourt grec|yaourts grecs", "yaourt", 150), (1, "gousse", "d'ail", "ail", 4),
    (2, "c. à soupe", "d'huile d'olive", "huile", 20), (20, "g", "de pignons", "graines", 20), (1, "brin", "de menthe", "herbe", 5), S],
    ["Couper les aubergines en deux, quadriller la chair, badigeonner d'huile.", "Rôtir 30 min à 200 °C.",
     "Mélanger le yaourt et l'ail râpé, assaisonner.", "Napper les aubergines, parsemer de pignons grillés et de menthe."])
r("courgettes-farcies", "Courgettes farcies au riz et chèvre", "Plat", 45, "vege", ["Courgette", "Tomate"], [
    (2, "", "courgette ronde|courgettes rondes", "courgette", 500), (60, "g", "de riz", "riz", 60), (1, "", "tomate|tomates", "tomate", 150),
    (80, "g", "de chèvre frais", "chevre", 80), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "brin", "de basilic", "herbe", 2), S],
    ["Cuire le riz.", "Couper un chapeau aux courgettes, les évider et hacher la chair.",
     "Mélanger riz, chair, tomate en dés, chèvre et basilic, assaisonner.", "Farcir, arroser d'huile et cuire 30 min à 180 °C."])
r("soupe-pistou", "Soupe au pistou", "Soupe", 40, "vege", ["Courgette", "Haricot vert", "Tomate"], [
    (1, "", "courgette|courgettes", "courgette", 200), (100, "g", "de haricots verts", "haricotvert", 100), (1, "", "tomate|tomates", "tomate", 150),
    (1, "", "pomme de terre|pommes de terre", "pdt", 150), (100, "g", "de haricots blancs cuits", "haricotblanc", 100), (50, "g", "de petites pâtes", "pates", 50),
    (1, "botte", "de basilic", "herbe", 20), (2, "gousse", "d'ail", "ail", 8), (2, "c. à soupe", "d'huile d'olive", "huile", 20), S],
    ["Couper les légumes en dés et les cuire 20 min dans 1 litre d'eau.", "Ajouter les haricots blancs et les pâtes, cuire 10 min.",
     "Piler le basilic avec l'ail et l'huile pour faire le pistou.", "Assaisonner la soupe et servir avec le pistou."])
r("artichauts-barigoule", "Artichauts à la barigoule", "Plat", 40, "vege", ["Artichaut", "Carotte nouvelle"], [
    (6, "", "petit artichaut violet|petits artichauts violets", "artichaut", 500), (2, "", "carotte nouvelle|carottes nouvelles", "carotte", 150),
    (1, "", "oignon nouveau|oignons nouveaux", "oignon", 80), (10, "cl", "de vin blanc", "vin", 100), (2, "c. à soupe", "d'huile d'olive", "huile", 20),
    (1, "brin", "de thym", "herbe", 2), S],
    ["Parer les artichauts et les couper en quatre.", "Faire revenir oignon et carottes dans l'huile.",
     "Ajouter artichauts, thym, vin et un verre d'eau.", "Cuire 25 min à couvert et assaisonner."])
r("poelee-champignons-chataignes", "Poêlée de champignons et châtaignes", "Plat", 25, "vege", ["Champignons", "Châtaigne"], [
    (300, "g", "de champignons", "champignon", 300), (200, "g", "de châtaignes cuites", "chataigne", 200), (1, "", "échalote|échalotes", "oignon", 40),
    (15, "g", "de beurre", "beurre", 15), (0.5, "botte", "de persil", "herbe", 15), (1, "gousse", "d'ail", "ail", 4), S],
    ["Faire fondre l'échalote dans le beurre.", "Ajouter les champignons et les faire dorer 8 min.",
     "Ajouter les châtaignes et l'ail, réchauffer 5 min.", "Assaisonner et parsemer de persil."])
r("salade-fenouil-pomme", "Salade de fenouil, pomme et olives", "Entrée", 10, "vege", ["Fenouil", "Pomme"], [
    (1, "", "bulbe de fenouil|bulbes de fenouil", "fenouil", 250), (1, "", "pomme|pommes", "pomme", 150), (10, "", "olive noire|olives noires", "olive", 30),
    (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "", "citron (jus)|citrons (jus)", "citron", 40), S],
    ["Émincer finement le fenouil.", "Couper la pomme en fines lamelles et l'arroser de jus de citron.",
     "Ajouter les olives, l'huile, assaisonner.", "Laisser reposer 10 min avant de servir."])
r("pdt-sautees-blettes", "Blettes et pommes de terre à l'ail", "Plat", 30, "vege", ["Blette"], [
    (1, "botte", "de blettes", "blette", 500), (3, "", "pomme de terre|pommes de terre", "pdt", 400), (2, "gousse", "d'ail", "ail", 8),
    (2, "c. à soupe", "d'huile d'olive", "huile", 20), (2, "", "œuf|œufs", "oeuf", 110), S],
    ["Cuire les pommes de terre en dés 12 min à l'eau.", "Émincer les côtes et les feuilles de blettes.",
     "Faire revenir côtes puis feuilles dans l'huile avec l'ail, ajouter les pommes de terre.", "Assaisonner et servir avec un œuf au plat."])

# ---------------- Viandes ----------------
r("poulet-potimarron", "Poulet rôti au thym, potimarron et châtaignes", "Plat", 45, "viande", ["Potimarron", "Châtaigne"], [
    (2, "", "cuisse de poulet|cuisses de poulet", "poulet_cuisse", 450), (400, "g", "de potimarron", "potimarron", 400), (150, "g", "de châtaignes cuites", "chataigne", 150),
    (1, "", "oignon rouge|oignons rouges", "oignon", 100), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (2, "brin", "de thym", "herbe", 3), S],
    ["Couper le potimarron en quartiers et l'oignon en quatre.", "Disposer avec les cuisses dans un plat, arroser d'huile, ajouter le thym, assaisonner.",
     "Cuire 35 min à 200 °C.", "Ajouter les châtaignes 10 min avant la fin."], meat="volaille")
r("tajine-poulet-citron", "Tajine de poulet au citron et carottes", "Plat", 45, "viande", ["Carotte", "Citron"], [
    (2, "", "haut de cuisse de poulet|hauts de cuisse de poulet", "poulet_cuisse", 400), (3, "", "carotte|carottes", "carotte", 300), (1, "", "oignon|oignons", "oignon", 100),
    (1, "", "citron|citrons", "citron", 100), (1, "c. à café", "de ras-el-hanout", "epice", 3), (1, "c. à soupe", "d'huile d'olive", "huile", 10),
    (0.5, "botte", "de coriandre ou de persil", "herbe", 15), S],
    ["Faire dorer le poulet dans l'huile avec l'oignon et les épices.", "Ajouter les carottes en bâtonnets, le citron en quartiers et un verre d'eau.",
     "Cuire 35 min à couvert à feu doux.", "Assaisonner et parsemer d'herbes."], meat="volaille", tip="Le citron et le ras-el-hanout remplacent le sel.")
r("agneau-coings", "Agneau confit aux coings", "Plat", 45, "viande", ["Coing"], [
    (400, "g", "d'épaule d'agneau en morceaux", "agneau", 400), (2, "", "coing|coings", "coing", 300), (1, "", "oignon|oignons", "oignon", 100),
    (1, "c. à café", "de cannelle", "epice", 2), (1, "c. à soupe", "de miel", "miel", 20), (1, "c. à soupe", "d'huile d'olive", "huile", 10), S],
    ["Faire dorer l'agneau dans l'huile avec l'oignon et la cannelle.", "Couvrir d'eau à hauteur et cuire 25 min à couvert.",
     "Ajouter les coings en quartiers et le miel, cuire 15 min.", "Assaisonner et servir."], meat="agneau")
r("navarin-printanier", "Navarin d'agneau aux légumes nouveaux", "Plat", 45, "viande", ["Carotte nouvelle", "Petits pois"], [
    (400, "g", "d'épaule d'agneau en morceaux", "agneau", 400), (4, "", "carotte nouvelle|carottes nouvelles", "carotte", 250), (150, "g", "de petits pois", "petitspois", 150),
    (6, "", "pomme de terre grenaille|pommes de terre grenaille", "pdt", 250), (1, "c. à soupe", "de concentré de tomate", "tomate", 15),
    (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "brin", "de thym", "herbe", 2), S],
    ["Faire dorer l'agneau dans l'huile, ajouter le concentré de tomate.", "Couvrir d'eau, ajouter le thym et cuire 20 min.",
     "Ajouter carottes et pommes de terre, cuire 15 min.", "Ajouter les petits pois 8 min, assaisonner."], meat="agneau")
r("blanquette-veau", "Blanquette de veau aux champignons", "Plat", 45, "viande", ["Carotte", "Champignons"], [
    (400, "g", "d'épaule de veau en morceaux", "veau", 400), (2, "", "carotte|carottes", "carotte", 200), (150, "g", "de champignons", "champignon", 150),
    (1, "", "oignon|oignons", "oignon", 100), (10, "cl", "de crème fraîche", "creme", 100), (1, "", "jaune d'œuf|jaunes d'œufs", "oeuf", 20), S],
    ["Couvrir le veau d'eau froide avec l'oignon et les carottes, cuire 35 min à frémissement.", "Ajouter les champignons 10 min avant la fin.",
     "Mélanger la crème, le jaune et une louche de bouillon.", "Lier la sauce hors du feu, assaisonner."], meat="veau")
r("daube-boeuf", "Daube de bœuf à la provençale", "Plat", 45, "viande", ["Carotte"], [
    (400, "g", "de bœuf à braiser", "boeuf_braise", 400), (2, "", "carotte|carottes", "carotte", 200), (1, "", "oignon|oignons", "oignon", 100),
    (20, "cl", "de vin rouge", "vin", 200), (1, "", "zeste d'orange|zestes d'orange", "orange", 5), (1, "c. à soupe", "d'huile d'olive", "huile", 10),
    (1, "brin", "de thym", "herbe", 2), S],
    ["Faire dorer le bœuf dans l'huile.", "Ajouter oignon, carottes, zeste d'orange, thym et vin.",
     "Cuire 40 min en autocuiseur (ou 2 h en cocotte).", "Assaisonner avant de servir."], meat="boeuf")
r("filet-mignon-pommes", "Filet mignon de porc aux pommes", "Plat", 35, "viande", ["Pomme"], [
    (350, "g", "de filet mignon de porc", "porc_filet", 350), (2, "", "pomme|pommes", "pomme", 300), (1, "", "oignon|oignons", "oignon", 100),
    (10, "cl", "de cidre", "vin", 100), (10, "g", "de beurre", "beurre", 10), S],
    ["Faire dorer le filet mignon dans le beurre.", "Ajouter l'oignon et les pommes en quartiers.",
     "Verser le cidre, couvrir et cuire 20 min.", "Assaisonner, trancher et servir."], meat="porc")
r("lentilles-saucisse", "Lentilles et saucisse de Toulouse", "Plat", 40, "viande", ["Carotte"], [
    (150, "g", "de lentilles vertes", "lentille", 150), (2, "", "saucisse de Toulouse|saucisses de Toulouse", "saucisse", 250), (2, "", "carotte|carottes", "carotte", 200),
    (1, "", "oignon|oignons", "oignon", 100), (1, "", "feuille de laurier|feuilles de laurier", "herbe", 1), S],
    ["Faire dorer les saucisses à sec, réserver.", "Faire revenir oignon et carottes dans la même cocotte.",
     "Ajouter les lentilles, le laurier, 3 fois leur volume d'eau et les saucisses.", "Cuire 25 min et assaisonner."], meat="porc")
r("lapin-moutarde", "Lapin à la moutarde et carottes", "Plat", 45, "viande", ["Carotte"], [
    (4, "", "morceau de lapin|morceaux de lapin", "lapin", 450), (2, "c. à soupe", "de moutarde", "moutarde", 30), (3, "", "carotte|carottes", "carotte", 300),
    (10, "cl", "de crème fraîche", "creme", 100), (10, "cl", "de vin blanc", "vin", 100), (1, "c. à soupe", "d'huile d'olive", "huile", 10), S],
    ["Badigeonner le lapin de moutarde et le faire dorer dans l'huile.", "Ajouter les carottes en rondelles et le vin.",
     "Cuire 35 min à couvert.", "Ajouter la crème, assaisonner."], meat="lapin")
r("magret-figues", "Magret de canard aux figues", "Plat", 30, "viande", ["Figue"], [
    (1, "", "magret de canard|magrets de canard", "canard", 350), (6, "", "figue|figues", "figue", 300), (1, "c. à soupe", "de miel", "miel", 20),
    (1, "c. à soupe", "de vinaigre balsamique", "epice", 15), S],
    ["Quadriller la peau du magret et le cuire 8 min côté peau, 4 min côté chair.", "Laisser reposer sous une feuille d'aluminium.",
     "Rôtir les figues coupées en deux dans la poêle avec le miel et le vinaigre.", "Trancher le magret, assaisonner, servir avec les figues."], meat="canard")
r("brochettes-poulet", "Brochettes de poulet, courgettes et poivrons", "Plat", 30, "viande", ["Courgette", "Poivron"], [
    (300, "g", "de blanc de poulet", "poulet_blanc", 300), (1, "", "courgette|courgettes", "courgette", 200), (1, "", "poivron|poivrons", "poivron", 200),
    (1, "", "citron|citrons", "citron", 60), (2, "c. à soupe", "d'huile d'olive", "huile", 20), (1, "c. à café", "d'herbes de Provence", "herbe", 2), S],
    ["Couper poulet et légumes en morceaux.", "Mariner 10 min avec l'huile, le jus de citron et les herbes.",
     "Monter les brochettes.", "Griller 12 min en les retournant, assaisonner."], meat="volaille")
r("boulettes-agneau", "Boulettes d'agneau, tomates et menthe", "Plat", 35, "viande", ["Tomate"], [
    (300, "g", "d'agneau haché", "agneau", 300), (4, "", "tomate|tomates", "tomate", 450), (1, "", "oignon|oignons", "oignon", 100),
    (1, "c. à café", "de cumin", "epice", 2), (1, "brin", "de menthe", "herbe", 5), (1, "c. à soupe", "d'huile d'olive", "huile", 10), S],
    ["Mélanger l'agneau, la moitié de l'oignon haché, le cumin et la menthe, former des boulettes.", "Les faire dorer dans l'huile.",
     "Ajouter le reste de l'oignon et les tomates en dés.", "Cuire 15 min, assaisonner."], meat="agneau")
r("poulet-asperges", "Poulet aux asperges et citron", "Plat", 30, "viande", ["Asperge"], [
    (300, "g", "de blanc de poulet", "poulet_blanc", 300), (10, "", "asperge verte|asperges vertes", "asperge", 300), (1, "", "citron|citrons", "citron", 60),
    (10, "cl", "de crème légère", "creme", 100), (1, "c. à soupe", "d'huile d'olive", "huile", 10), S],
    ["Couper le poulet en lanières et les asperges en tronçons.", "Faire dorer le poulet dans l'huile, réserver.",
     "Cuire les asperges 6 min dans la même poêle.", "Remettre le poulet avec la crème et le zeste de citron, assaisonner."], meat="volaille")
r("dinde-epinards", "Escalopes de dinde aux épinards", "Plat", 25, "viande", ["Épinard"], [
    (2, "", "escalope de dinde|escalopes de dinde", "dinde", 300), (300, "g", "d'épinards frais", "epinard", 300), (1, "gousse", "d'ail", "ail", 4),
    (10, "cl", "de crème légère", "creme", 100), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "pincée", "de muscade", "epice", 0), S],
    ["Cuire les escalopes 4 min de chaque côté dans l'huile, réserver.", "Faire tomber les épinards avec l'ail dans la poêle.",
     "Ajouter la crème et la muscade.", "Assaisonner et servir avec les escalopes."], meat="volaille")
r("boeuf-poivrons", "Bœuf sauté aux poivrons", "Plat", 25, "viande", ["Poivron"], [
    (300, "g", "de rumsteck", "boeuf_maigre", 300), (2, "", "poivron|poivrons", "poivron", 350), (1, "", "oignon|oignons", "oignon", 100),
    (1, "gousse", "d'ail", "ail", 4), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "c. à café", "de paprika", "epice", 2), S],
    ["Couper le bœuf en lanières et les légumes en bandes.", "Saisir le bœuf 2 min à feu vif, réserver.",
     "Faire sauter les légumes 8 min avec l'ail et le paprika.", "Remettre le bœuf, assaisonner."], meat="boeuf")
r("cotes-porc-haricots", "Côtes de porc et haricots verts à l'ail", "Plat", 25, "viande", ["Haricot vert"], [
    (2, "", "côte de porc|côtes de porc", "porc_cote", 350), (300, "g", "de haricots verts", "haricotvert", 300), (2, "gousse", "d'ail", "ail", 8),
    (1, "c. à soupe", "d'huile d'olive", "huile", 10), (0.5, "botte", "de persil", "herbe", 15), S],
    ["Cuire les haricots 8 min à l'eau bouillante.", "Cuire les côtes 5 min de chaque côté dans l'huile.",
     "Faire sauter les haricots avec l'ail et le persil.", "Assaisonner et servir."], meat="porc")
r("parmentier-canard", "Parmentier de canard et panais", "Plat", 45, "viande", ["Panais"], [
    (2, "", "cuisse de canard confite|cuisses de canard confites", "confit", 400), (300, "g", "de pommes de terre", "pdt", 300), (300, "g", "de panais", "panais", 300),
    (10, "cl", "de lait", "lait", 100), (1, "", "échalote|échalotes", "oignon", 40), S],
    ["Cuire pommes de terre et panais 20 min, les écraser avec le lait.", "Effilocher le canard sans la peau, le faire revenir avec l'échalote.",
     "Mettre le canard au fond d'un plat, couvrir de purée.", "Gratiner 15 min à 200 °C."], meat="canard")
r("poulet-poireaux", "Poulet aux poireaux et moutarde", "Plat", 30, "viande", ["Poireau"], [
    (300, "g", "de blanc de poulet", "poulet_blanc", 300), (2, "", "poireau|poireaux", "poireau", 300), (1, "c. à soupe", "de moutarde", "moutarde", 15),
    (10, "cl", "de crème légère", "creme", 100), (1, "c. à soupe", "d'huile d'olive", "huile", 10), S],
    ["Émincer les poireaux et les faire fondre 10 min dans l'huile.", "Ajouter le poulet en dés et le faire dorer.",
     "Ajouter la crème et la moutarde, cuire 5 min.", "Assaisonner et servir."], meat="volaille")
r("boeuf-carottes", "Bœuf carottes", "Plat", 45, "viande", ["Carotte"], [
    (400, "g", "de paleron de bœuf", "boeuf_braise", 400), (4, "", "carotte|carottes", "carotte", 400), (1, "", "oignon|oignons", "oignon", 100),
    (20, "cl", "de vin blanc", "vin", 200), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "brin", "de thym", "herbe", 2), S],
    ["Faire dorer le bœuf en morceaux dans l'huile.", "Ajouter l'oignon, les carottes en rondelles, le thym et le vin.",
     "Cuire 40 min en autocuiseur (ou 2 h en cocotte).", "Assaisonner avant de servir."], meat="boeuf")

# ---------------- Poissons ----------------
r("daurade-fenouil", "Daurade au four, fenouil et citron", "Plat", 35, "poisson", ["Fenouil"], [
    (2, "", "filet de daurade|filets de daurade", "daurade", 300), (2, "", "bulbe de fenouil|bulbes de fenouil", "fenouil", 400), (1, "", "citron|citrons", "citron", 60),
    (2, "c. à soupe", "d'huile d'olive", "huile", 20), (1, "brin", "de thym", "herbe", 2), S],
    ["Émincer le fenouil et le rôtir 15 min à 200 °C avec l'huile.", "Poser les filets dessus avec des rondelles de citron et le thym.",
     "Cuire 12 min.", "Assaisonner et servir."], f="Daurade")
r("moules-vin-blanc", "Moules de Bouzigues au vin blanc", "Plat", 20, "poisson", [], [
    (1, "kg", "de moules de Bouzigues", "moule", 1000), (2, "", "échalote|échalotes", "oignon", 80), (15, "cl", "de vin blanc", "vin", 150),
    (0.5, "botte", "de persil", "herbe", 15), (10, "g", "de beurre", "beurre", 10)],
    ["Gratter et rincer les moules.", "Faire fondre les échalotes dans le beurre.",
     "Ajouter le vin et les moules, couvrir et cuire 6 min en remuant.", "Parsemer de persil et servir aussitôt (pas besoin de sel)."], f="Moules")
r("seiches-tomate", "Seiches à la tomate et persillade", "Plat", 35, "poisson", ["Tomate"], [
    (400, "g", "de seiches nettoyées", "seiche", 400), (3, "", "tomate|tomates", "tomate", 400), (2, "gousse", "d'ail", "ail", 8),
    (0.5, "botte", "de persil", "herbe", 15), (2, "c. à soupe", "d'huile d'olive", "huile", 20), (1, "pincée", "de piment", "epice", 0), S],
    ["Couper les seiches en lanières et les saisir 3 min dans l'huile.", "Ajouter les tomates en dés et le piment.",
     "Cuire 25 min à feu doux.", "Ajouter l'ail et le persil hachés, assaisonner."], f="Seiche", m=[5, 6, 9, 10])
r("sardines-grillees", "Sardines grillées, tomates aux herbes", "Plat", 20, "poisson", ["Tomate"], [
    (8, "", "sardine fraîche|sardines fraîches", "sardine", 400), (3, "", "tomate|tomates", "tomate", 400), (1, "", "citron|citrons", "citron", 60),
    (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "c. à café", "d'herbes de Provence", "herbe", 2), S],
    ["Vider et rincer les sardines.", "Les griller 3 min de chaque côté.",
     "Couper les tomates, arroser d'huile, parsemer d'herbes.", "Assaisonner et servir avec le citron."], f="Sardine")
r("maquereaux-pdt", "Maquereaux rôtis, salade de pommes de terre", "Plat", 30, "poisson", ["Oignon nouveau"], [
    (2, "", "maquereau|maquereaux", "maquereau", 400), (400, "g", "de pommes de terre", "pdt", 400), (1, "", "oignon nouveau|oignons nouveaux", "oignon", 60),
    (1, "c. à soupe", "de moutarde", "moutarde", 15), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "", "citron|citrons", "citron", 60), S],
    ["Cuire les pommes de terre 15 min à l'eau.", "Rôtir les maquereaux 15 min à 200 °C avec des rondelles de citron.",
     "Mélanger moutarde, huile et oignon émincé avec les pommes de terre tièdes.", "Assaisonner et servir avec le poisson."], f="Maquereau")
r("merlan-papillote", "Merlan en papillote, poireaux et citron", "Plat", 25, "poisson", ["Poireau"], [
    (2, "", "filet de merlan|filets de merlan", "merlan", 300), (2, "", "poireau|poireaux", "poireau", 300), (1, "", "citron|citrons", "citron", 60),
    (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "brin", "d'aneth", "herbe", 3), S],
    ["Émincer les poireaux et les faire fondre 8 min dans l'huile.", "Répartir sur deux feuilles de papier cuisson, poser les filets, l'aneth et le citron.",
     "Fermer les papillotes.", "Cuire 12 min à 200 °C, assaisonner à table."], f="Merlan")
r("cabillaud-celeri", "Cabillaud, purée de céleri-rave", "Plat", 30, "poisson", ["Céleri-rave"], [
    (2, "", "pavé de cabillaud|pavés de cabillaud", "cabillaud", 300), (500, "g", "de céleri-rave", "celeri", 500), (10, "cl", "de lait", "lait", 100),
    (10, "g", "de beurre", "beurre", 10), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (0.5, "botte", "de ciboulette", "herbe", 10), S],
    ["Cuire le céleri en dés 20 min à l'eau, le mixer avec le lait et le beurre.", "Cuire le cabillaud 4 min de chaque côté dans l'huile.",
     "Assaisonner.", "Servir sur la purée avec la ciboulette."], f="Cabillaud")
r("encornets-ail", "Encornets sautés à l'ail et persil", "Plat", 20, "poisson", ["Tomate"], [
    (400, "g", "d'encornets nettoyés", "encornet", 400), (3, "gousse", "d'ail", "ail", 12), (0.5, "botte", "de persil", "herbe", 15),
    (2, "c. à soupe", "d'huile d'olive", "huile", 20), (1, "", "citron|citrons", "citron", 60), (2, "", "tomate|tomates", "tomate", 300), S],
    ["Couper les encornets en anneaux.", "Les saisir 3 min à feu vif dans l'huile.",
     "Ajouter l'ail et le persil hachés, cuire 1 min.", "Assaisonner, servir avec le citron et une salade de tomates."], f="Encornet")
r("thon-poivrons", "Thon snacké, poivrons confits", "Plat", 30, "poisson", ["Poivron", "Tomate"], [
    (2, "", "steak de thon|steaks de thon", "thon", 300), (2, "", "poivron|poivrons", "poivron", 350), (2, "", "tomate|tomates", "tomate", 250),
    (2, "c. à soupe", "d'huile d'olive", "huile", 20), (1, "gousse", "d'ail", "ail", 4), (1, "brin", "de basilic", "herbe", 2), S],
    ["Faire confire poivrons et tomates en lanières 20 min dans l'huile avec l'ail.", "Saisir le thon 1 min 30 de chaque côté.",
     "Assaisonner.", "Servir avec les poivrons et le basilic."], f="Thon")
r("saint-jacques-poireaux", "Saint-Jacques poêlées, fondue de poireaux", "Plat", 25, "poisson", ["Poireau"], [
    (8, "", "noix de Saint-Jacques|noix de Saint-Jacques", "stjacques", 240), (2, "", "poireau|poireaux", "poireau", 300), (10, "cl", "de crème légère", "creme", 100),
    (10, "g", "de beurre", "beurre", 10), S],
    ["Émincer les poireaux et les faire fondre 12 min dans le beurre.", "Ajouter la crème et assaisonner.",
     "Saisir les Saint-Jacques 1 min de chaque côté dans une poêle très chaude.", "Servir sur la fondue de poireaux."], f="Saint-Jacques")
r("rougets-courgettes", "Rougets et courgettes au basilic", "Plat", 25, "poisson", ["Courgette"], [
    (4, "", "filet de rouget|filets de rouget", "rouget", 250), (2, "", "courgette|courgettes", "courgette", 400), (2, "c. à soupe", "d'huile d'olive", "huile", 20),
    (1, "brin", "de basilic", "herbe", 3), (1, "", "citron|citrons", "citron", 60), S],
    ["Couper les courgettes en rondelles et les poêler 10 min dans l'huile.", "Cuire les filets 2 min côté peau, 1 min de l'autre.",
     "Assaisonner.", "Servir avec le basilic et un filet de citron."], f="Rouget")
r("bar-endives", "Bar rôti, endives braisées à l'orange", "Plat", 35, "poisson", ["Endive", "Orange"], [
    (2, "", "filet de bar|filets de bar", "bar", 300), (4, "", "endive|endives", "endive", 400), (1, "", "orange|oranges", "orange", 150),
    (10, "g", "de beurre", "beurre", 10), (1, "c. à soupe", "d'huile d'olive", "huile", 10), S],
    ["Couper les endives en deux et les dorer dans le beurre.", "Ajouter le jus d'orange, couvrir et braiser 20 min.",
     "Cuire le bar 3 min côté peau dans l'huile.", "Assaisonner et servir avec les endives."], f="Bar")
r("anchois-marines", "Anchois frais marinés au citron", "Entrée", 20, "poisson", [], [
    (300, "g", "d'anchois frais", "anchois", 300), (2, "", "citron|citrons", "citron", 120), (1, "gousse", "d'ail", "ail", 4),
    (2, "c. à soupe", "d'huile d'olive", "huile", 20), (0.5, "botte", "de persil", "herbe", 15), S],
    ["Lever les filets d'anchois et les rincer.", "Les couvrir de jus de citron 2 h au frais (ils blanchissent).",
     "Égoutter, arroser d'huile, ajouter ail et persil hachés.", "Assaisonner et servir bien frais."], f="Anchois")
r("salade-thon-haricots", "Salade de haricots verts et thon", "Entrée", 20, "poisson", ["Haricot vert", "Tomate"], [
    (250, "g", "de haricots verts", "haricotvert", 250), (1, "", "steak de thon|steaks de thon", "thon", 150), (2, "", "tomate|tomates", "tomate", 250),
    (1, "", "œuf dur|œufs durs", "oeuf", 55), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "c. à café", "de moutarde", "moutarde", 5), S],
    ["Cuire les haricots 8 min et les refroidir.", "Saisir le thon 1 min par face et le couper en dés.",
     "Mélanger huile et moutarde, assaisonner.", "Assembler haricots, tomates, thon et œuf."], f="Thon")

# ---------------- Desserts ----------------
r("poires-pochees", "Poires pochées aux épices et noix", "Dessert", 25, "vege", ["Poire"], [
    (2, "", "poire|poires", "poire", 300), (40, "g", "de sucre", "sucre", 40), (1, "", "bâton de cannelle|bâtons de cannelle", "epice", 3),
    (1, "", "étoile de badiane|étoiles de badiane", "epice", 1), (20, "g", "de cerneaux de noix", "noix", 20)],
    ["Éplucher les poires en gardant la queue.", "Porter 50 cl d'eau à ébullition avec le sucre et les épices.",
     "Pocher les poires 20 min à frémissement.", "Servir tièdes avec un peu de sirop et les noix concassées."], sweet=True)
r("crumble-pomme-coing", "Crumble pomme-coing", "Dessert", 35, "vege", ["Pomme", "Coing"], [
    (2, "", "pomme|pommes", "pomme", 300), (1, "", "coing|coings", "coing", 200), (50, "g", "de farine", "farine", 50),
    (40, "g", "de beurre", "beurre", 40), (40, "g", "de sucre", "sucre", 40), (20, "g", "de poudre d'amande", "amande", 20)],
    ["Couper pommes et coing en dés, les cuire 10 min à la poêle avec un peu d'eau.", "Sabler du bout des doigts farine, beurre, sucre et amande.",
     "Mettre les fruits dans un plat et couvrir de crumble.", "Cuire 25 min à 180 °C."], sweet=True)
r("salade-oranges", "Salade d'oranges à la cannelle", "Dessert", 10, "vege", ["Orange"], [
    (3, "", "orange|oranges", "orange", 450), (1, "c. à café", "de cannelle", "epice", 2), (1, "c. à soupe", "de miel", "miel", 20),
    (1, "brin", "de menthe", "herbe", 3)],
    ["Peler les oranges à vif et les couper en rondelles.", "Les disposer dans un plat.",
     "Arroser de miel, saupoudrer de cannelle.", "Parsemer de menthe et servir frais."], sweet=True)
r("clafoutis-cerises", "Clafoutis aux cerises", "Dessert", 45, "vege", ["Cerise"], [
    (300, "g", "de cerises", "cerise", 300), (2, "", "œuf|œufs", "oeuf", 110), (40, "g", "de farine", "farine", 40), (40, "g", "de sucre", "sucre", 40),
    (20, "cl", "de lait", "lait", 200), (10, "g", "de beurre", "beurre", 10)],
    ["Beurrer un plat et y répartir les cerises.", "Fouetter œufs et sucre, ajouter la farine puis le lait.",
     "Verser sur les cerises.", "Cuire 35 min à 180 °C et servir tiède."], sweet=True)
r("fraises-yaourt-menthe", "Fraises, yaourt et menthe", "Dessert", 10, "vege", ["Fraise"], [
    (300, "g", "de fraises", "fraise", 300), (2, "", "yaourt grec|yaourts grecs", "yaourt", 250), (1, "c. à soupe", "de miel", "miel", 20),
    (1, "brin", "de menthe", "herbe", 3)],
    ["Laver et couper les fraises.", "Mélanger avec le miel et la menthe ciselée.",
     "Répartir le yaourt dans deux coupes.", "Ajouter les fraises au moment de servir."], sweet=True)
r("abricots-rotis", "Abricots rôtis au miel et amandes", "Dessert", 25, "vege", ["Abricot"], [
    (8, "", "abricot|abricots", "abricot", 350), (1, "c. à soupe", "de miel", "miel", 20), (20, "g", "d'amandes effilées", "amande", 20),
    (1, "brin", "de romarin ou de thym", "herbe", 1)],
    ["Couper les abricots en deux et les dénoyauter.", "Les disposer dans un plat, arroser de miel, ajouter le romarin.",
     "Rôtir 15 min à 200 °C.", "Parsemer d'amandes grillées et servir tiède."], sweet=True)
r("peches-melon-menthe", "Salade de pêches et melon à la menthe", "Dessert", 10, "vege", ["Pêche", "Melon"], [
    (2, "", "pêche|pêches", "peche", 300), (0.5, "", "melon|melons", "melon", 400), (1, "", "citron vert|citrons verts", "citron", 30),
    (1, "brin", "de menthe", "herbe", 3)],
    ["Couper pêches et melon en dés.", "Arroser de jus de citron vert.",
     "Ajouter la menthe ciselée.", "Servir très frais."], sweet=True)
r("figues-roties", "Figues rôties au miel", "Dessert", 20, "vege", ["Figue"], [
    (6, "", "figue|figues", "figue", 300), (1, "c. à soupe", "de miel", "miel", 20), (2, "", "yaourt grec|yaourts grecs", "yaourt", 250),
    (20, "g", "de noisettes", "noisette", 20)],
    ["Inciser les figues en croix.", "Les arroser de miel et les rôtir 12 min à 200 °C.",
     "Servir sur le yaourt.", "Parsemer de noisettes concassées."], sweet=True)
r("tarte-fine-pommes", "Tarte fine aux pommes", "Dessert", 35, "vege", ["Pomme"], [
    (1, "", "pâte feuilletée|pâtes feuilletées", "feuilletee", 230), (3, "", "pomme|pommes", "pomme", 450), (20, "g", "de beurre", "beurre", 20),
    (30, "g", "de sucre", "sucre", 30), (1, "c. à café", "de cannelle", "epice", 2)],
    ["Étaler la pâte sur une plaque.", "Couper les pommes en fines lamelles et les ranger sur la pâte.",
     "Parsemer de beurre en noisettes, de sucre et de cannelle.", "Cuire 25 min à 200 °C."], sweet=True, m=[9, 10, 11, 12, 1, 2, 3], parts=4)
r("mousse-chocolat", "Mousse au chocolat légère", "Dessert", 20, "vege", [], [
    (100, "g", "de chocolat noir", "chocolat", 100), (3, "", "œuf|œufs", "oeuf", 165), (1, "pincée", "de cannelle (facultatif)", "epice", 0)],
    ["Faire fondre le chocolat au bain-marie.", "Séparer les blancs des jaunes, mélanger les jaunes au chocolat tiède.",
     "Monter les blancs en neige ferme et les incorporer délicatement.", "Réserver 3 h au frais."], sweet=True, m=list(range(1, 13)))
r("compote-pommes-poires", "Compote pommes-poires sans sucre ajouté", "Dessert", 25, "vege", ["Pomme", "Poire"], [
    (2, "", "pomme|pommes", "pomme", 300), (2, "", "poire|poires", "poire", 300), (1, "c. à café", "de vanille liquide", "epice", 5),
    (1, "pincée", "de cannelle", "epice", 0)],
    ["Éplucher et couper les fruits.", "Les cuire 20 min à couvert avec 5 cl d'eau, la vanille et la cannelle.",
     "Écraser à la fourchette ou mixer.", "Servir tiède ou froide."], sweet=True)
r("gateau-noix", "Gâteau moelleux aux noix", "Dessert", 40, "vege", ["Noix"], [
    (80, "g", "de cerneaux de noix", "noix", 80), (2, "", "œuf|œufs", "oeuf", 110), (60, "g", "de sucre", "sucre", 60), (50, "g", "de farine", "farine", 50),
    (50, "g", "de beurre fondu", "beurre", 50)],
    ["Mixer grossièrement les noix.", "Fouetter œufs et sucre, ajouter le beurre fondu, la farine et les noix.",
     "Verser dans un petit moule beurré.", "Cuire 25 min à 180 °C (il en restera pour le lendemain)."], sweet=True, parts=4)
r("crumble-rhubarbe-fraise", "Crumble rhubarbe et fraises", "Dessert", 40, "vege", ["Rhubarbe", "Fraise"], [
    (250, "g", "de rhubarbe", "rhubarbe", 250), (200, "g", "de fraises", "fraise", 200), (50, "g", "de farine", "farine", 50),
    (40, "g", "de beurre", "beurre", 40), (50, "g", "de sucre", "sucre", 50)],
    ["Couper rhubarbe et fraises en morceaux, les mettre dans un plat avec 10 g de sucre.", "Sabler farine, beurre et le reste du sucre.",
     "Couvrir les fruits de crumble.", "Cuire 30 min à 180 °C."], sweet=True)
r("granite-pasteque", "Granité de pastèque au citron vert", "Dessert", 15, "vege", ["Pastèque"], [
    (600, "g", "de chair de pastèque", "pasteque", 600), (1, "", "citron vert|citrons verts", "citron", 30), (20, "g", "de sucre", "sucre", 20)],
    ["Mixer la pastèque sans pépins avec le jus de citron vert et le sucre.", "Verser dans un plat et mettre au congélateur.",
     "Gratter à la fourchette toutes les 30 min pendant 3 h.", "Servir dans des verres bien froids."], sweet=True)
r("raisins-fromage-blanc", "Raisins frais, fromage blanc et miel", "Dessert", 5, "vege", ["Raisin"], [
    (250, "g", "de raisin", "raisin", 250), (200, "g", "de fromage blanc", "fromageblanc", 200), (1, "c. à soupe", "de miel", "miel", 20),
    (20, "g", "de noisettes", "noisette", 20)],
    ["Laver et égrainer le raisin.", "Répartir le fromage blanc dans deux bols.",
     "Ajouter le raisin, le miel et les noisettes concassées.", "Servir aussitôt."], sweet=True)
r("kiwi-clementines", "Salade de kiwis et clémentines", "Dessert", 10, "vege", ["Kiwi", "Clémentine"], [
    (3, "", "kiwi|kiwis", "kiwi", 250), (3, "", "clémentine|clémentines", "orange", 200), (1, "c. à café", "de miel", "miel", 7),
    (1, "brin", "de menthe", "herbe", 3)],
    ["Peler et couper les kiwis en rondelles.", "Peler les clémentines et séparer les quartiers.",
     "Mélanger avec le miel.", "Parsemer de menthe et servir frais."], sweet=True)

# ---------------- Ajouts printemps-été (viandes) ----------------
r("poulet-petits-pois", "Poulet aux petits pois et oignons nouveaux", "Plat", 35, "viande", ["Petits pois", "Oignon nouveau"], [
    (2, "", "haut de cuisse de poulet|hauts de cuisse de poulet", "poulet_cuisse", 400), (250, "g", "de petits pois", "petitspois", 250),
    (4, "", "oignon nouveau|oignons nouveaux", "oignon", 150), (1, "", "laitue|laitues", "endive", 150), (1, "c. à soupe", "d'huile d'olive", "huile", 10),
    (1, "brin", "de thym", "herbe", 2), S],
    ["Faire dorer le poulet dans l'huile.", "Ajouter les oignons nouveaux, le thym et un demi-verre d'eau, cuire 15 min à couvert.",
     "Ajouter les petits pois et la laitue émincée, cuire 10 min.", "Assaisonner et servir."], meat="volaille")
r("agneau-feves-artichauts", "Sauté d'agneau aux fèves et artichauts", "Plat", 40, "viande", ["Fèves", "Artichaut"], [
    (350, "g", "d'épaule d'agneau en morceaux", "agneau", 350), (200, "g", "de fèves écossées", "feve", 200), (4, "", "petit artichaut violet|petits artichauts violets", "artichaut", 300),
    (1, "", "citron|citrons", "citron", 60), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "brin", "de menthe", "herbe", 3), S],
    ["Faire dorer l'agneau dans l'huile.", "Ajouter les artichauts en quartiers, le jus de citron et un verre d'eau, cuire 20 min.",
     "Ajouter les fèves, cuire 8 min.", "Assaisonner et parsemer de menthe."], meat="agneau")
r("poulet-tzatziki", "Poulet grillé et salade de concombre au yaourt", "Plat", 25, "viande", ["Concombre"], [
    (300, "g", "de blanc de poulet", "poulet_blanc", 300), (1, "", "concombre|concombres", "concombre", 300), (1, "", "yaourt grec|yaourts grecs", "yaourt", 150),
    (1, "gousse", "d'ail", "ail", 4), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (1, "c. à café", "de paprika", "epice", 2), (1, "brin", "de menthe", "herbe", 3), S],
    ["Frotter le poulet d'huile et de paprika, le griller 6 min de chaque côté.", "Râper le concombre et le presser.",
     "Mélanger concombre, yaourt, ail et menthe, assaisonner.", "Trancher le poulet et servir avec la salade."], meat="volaille")
r("veau-printanier", "Escalopes de veau aux asperges", "Plat", 25, "viande", ["Asperge"], [
    (2, "", "escalope de veau|escalopes de veau", "veau", 280), (10, "", "asperge verte|asperges vertes", "asperge", 300), (1, "", "citron|citrons", "citron", 60),
    (10, "g", "de beurre", "beurre", 10), (1, "c. à soupe", "d'huile d'olive", "huile", 10), S],
    ["Cuire les asperges 6 min à l'eau puis les poêler dans le beurre.", "Saisir les escalopes 2 min de chaque côté dans l'huile.",
     "Déglacer avec le jus de citron.", "Assaisonner et servir avec les asperges."], meat="veau")
