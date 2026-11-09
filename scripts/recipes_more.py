"""Recettes complémentaires de SEASON : au moins une recette pour chaque produit de saison, chaque mois (pour 2 personnes)."""


def add_more(r, S):
    # ---------- Légumes ----------
    r("houmous-betterave", "Houmous de betterave et crudités", "Entrée", 15, "vege", ["Betterave", "Carotte"], [
        (1, "", "betterave cuite|betteraves cuites", "betterave", 200), (200, "g", "de pois chiches cuits", "poischiche", 200),
        (1, "c. à soupe", "de tahini", "tahini", 15), (0.5, "", "citron|citrons", "citron", 30), (1, "gousse", "d'ail", "ail", 4),
        (2, "", "carotte|carottes", "carotte", 200), (1, "c. à soupe", "d'huile d'olive", "huile", 10), S],
        ["Mixer betterave, pois chiches, tahini, jus de citron, ail et huile jusqu'à obtenir une crème lisse.",
         "Allonger d'un peu d'eau si besoin, assaisonner.", "Servir avec les carottes en bâtonnets et du pain."],
        c="orient", o="Liban", tip="Le citron et l'ail suffisent à le relever sans sel.")
    r("betterave-rotie-chevre", "Betteraves rôties, chèvre frais et noix", "Entrée", 45, "vege", ["Betterave"], [
        (3, "", "betterave crue|betteraves crues", "betterave", 400), (100, "g", "de chèvre frais", "chevre", 100), (30, "g", "de cerneaux de noix", "noix", 30),
        (1, "c. à soupe", "de miel", "miel", 15), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (0.5, "botte", "de thym", "herbe", 5), S],
        ["Préchauffer le four à 200 °C.", "Couper les betteraves épluchées en quartiers, les arroser d'huile et de thym.",
         "Rôtir 35 min, en retournant à mi-cuisson.", "Servir tiède avec le chèvre émietté, les noix et un filet de miel."])
    r("choux-bruxelles-rotis", "Choux de Bruxelles rôtis au miel et noisettes", "Plat", 35, "vege", ["Chou de Bruxelles"], [
        (500, "g", "de choux de Bruxelles", "chou", 500), (1, "c. à soupe", "de miel", "miel", 15), (30, "g", "de noisettes", "noisette", 30),
        (1, "c. à soupe", "de moutarde à l'ancienne", "moutarde", 15), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (120, "g", "de quinoa ou de riz", "riz", 120), S],
        ["Préchauffer le four à 210 °C, cuire le quinoa.", "Couper les choux en deux, les mélanger à l'huile.",
         "Rôtir 20 min jusqu'à ce qu'ils dorent.", "Mélanger miel et moutarde, en enrober les choux, ajouter les noisettes concassées, rôtir encore 5 min."],
        tip="Rôtis, ils perdent leur amertume : même ceux qui ne les aiment pas s'y laissent prendre.")
    r("poulet-choux-bruxelles", "Poulet poêlé aux choux de Bruxelles et lardons de dinde", "Plat", 35, "viande", ["Chou de Bruxelles", "Carotte"], [
        (2, "", "cuisse de poulet|cuisses de poulet", "poulet_cuisse", 400), (400, "g", "de choux de Bruxelles", "chou", 400),
        (2, "", "carotte|carottes", "carotte", 150), (80, "g", "de lardons de dinde", "dinde", 80), (1, "", "oignon|oignons", "oignon", 100),
        (1, "c. à soupe", "d'huile", "huile", 10), S],
        ["Blanchir les choux 5 min à l'eau bouillante.", "Dorer les cuisses de poulet 10 min de chaque côté dans l'huile.",
         "Ajouter oignon, carottes en rondelles, lardons et choux, couvrir et cuire 15 min.", "Assaisonner et servir."], meat="volaille")
    r("veloute-topinambour", "Velouté de topinambours à la noisette", "Soupe", 35, "vege", ["Topinambour", "Poireau"], [
        (500, "g", "de topinambours", "topinambour", 500), (1, "", "poireau|poireaux", "poireau", 150), (50, "cl", "de bouillon de légumes", "bouillon", 500),
        (5, "cl", "de crème", "creme", 50), (20, "g", "de noisettes", "noisette", 20), S],
        ["Éplucher les topinambours et les couper en morceaux.", "Faire suer le poireau, ajouter topinambours et bouillon, cuire 25 min.",
         "Mixer avec la crème, assaisonner.", "Servir parsemé de noisettes torréfiées concassées."],
        tip="Son goût rappelle l'artichaut : la noisette le met bien en valeur.")
    r("topinambours-rotis-mache", "Topinambours rôtis, mâche et œuf mollet", "Plat", 40, "vege", ["Topinambour", "Mâche"], [
        (500, "g", "de topinambours", "topinambour", 500), (100, "g", "de mâche", "mache", 100), (2, "", "œuf|œufs", "oeuf", 110),
        (20, "g", "de noix", "noix", 20), (1, "c. à soupe", "d'huile de noix ou d'olive", "huile", 15), (1, "c. à café", "de vinaigre", "epice", 5), S],
        ["Rôtir les topinambours en tranches épaisses 30 min à 200 °C avec la moitié de l'huile.", "Cuire les œufs 6 min, les écaler.",
         "Assaisonner la mâche avec le reste d'huile et le vinaigre.", "Dresser mâche, topinambours, œuf coupé en deux et noix."])
    r("salade-mache-betterave", "Salade de mâche, betterave et pomme", "Entrée", 10, "vege", ["Mâche", "Pomme"], [
        (100, "g", "de mâche", "mache", 100), (1, "", "betterave cuite|betteraves cuites", "betterave", 150), (1, "", "pomme|pommes", "pomme", 150),
        (20, "g", "de cerneaux de noix", "noix", 20), (1, "c. à soupe", "d'huile de noix", "huile", 15), (1, "c. à café", "de vinaigre de cidre", "epice", 5), S],
        ["Couper betterave et pomme en dés.", "Mélanger huile et vinaigre.", "Assaisonner la mâche au dernier moment, ajouter dés et noix."])
    r("salsifis-persillade", "Salsifis à la persillade et filet de merlan", "Plat", 40, "poisson", ["Salsifis"], [
        (600, "g", "de salsifis", "salsifis", 600), (2, "", "filet de merlan|filets de merlan", "merlan", 300), (1, "gousse", "d'ail", "ail", 4),
        (0.5, "botte", "de persil", "herbe", 10), (20, "g", "de beurre", "beurre", 20), (0.5, "", "citron|citrons", "citron", 30), S],
        ["Éplucher les salsifis avec des gants, les plonger dans l'eau citronnée, puis les cuire 20 min à l'eau.",
         "Les faire dorer au beurre 5 min avec l'ail et le persil hachés.", "Cuire le merlan 3 min de chaque côté à la poêle.", "Servir avec un trait de citron."],
        tip="Les salsifis en bocal, déjà épluchés, font gagner 15 min.", f="Merlan")
    r("radis-noir-remoulade", "Radis noir en rémoulade et œufs durs", "Entrée", 15, "vege", ["Radis noir"], [
        (1, "", "radis noir|radis noirs", "radis", 250), (2, "c. à soupe", "de yaourt", "yaourt", 40), (1, "c. à café", "de moutarde", "moutarde", 5),
        (2, "", "œuf|œufs", "oeuf", 110), (0.5, "botte", "de ciboulette", "herbe", 5), S],
        ["Cuire les œufs 10 min, les écaler.", "Râper le radis noir finement.", "Mélanger yaourt et moutarde, en enrober le radis, ajouter la ciboulette.",
         "Servir avec les œufs coupés en quartiers."], tip="Épluché et râpé, le radis noir est bien moins piquant.")
    r("radis-beurre-tartines", "Tartines de radis, beurre et fleur de thym", "Entrée", 10, "vege", ["Radis"], [
        (1, "botte", "de radis", "radis", 200), (4, "", "tranche de pain de campagne|tranches de pain de campagne", "pain", 120),
        (20, "g", "de beurre doux", "beurre", 20), (0.5, "botte", "de ciboulette", "herbe", 5)],
        ["Tartiner le pain de beurre.", "Couper les radis en fines rondelles.", "Les disposer sur les tartines, parsemer de ciboulette."])
    r("artichauts-poivrade-salade", "Salade d'artichauts poivrade, citron et parmesan", "Entrée", 20, "vege", ["Artichaut"], [
        (6, "", "petit artichaut poivrade|petits artichauts poivrade", "artichaut", 400), (1, "", "citron|citrons", "citron", 60),
        (30, "g", "de parmesan", "parmesan", 30), (2, "c. à soupe", "d'huile d'olive", "huile", 20), (0.5, "botte", "de basilic", "herbe", 5), S],
        ["Parer les artichauts, retirer le foin et les citronner aussitôt.", "Les émincer très finement à la mandoline.",
         "Arroser de jus de citron et d'huile.", "Ajouter le parmesan en copeaux et le basilic."], c="med", o="Italie")
    r("petits-pois-laitue", "Petits pois à la française", "Plat", 30, "vege", ["Petits pois", "Laitue"], [
        (800, "g", "de petits pois à écosser", "petitspois", 300), (1, "", "laitue|laitues", "laitue", 200), (4, "", "oignon nouveau|oignons nouveaux", "oignon", 80),
        (20, "g", "de beurre", "beurre", 20), (2, "", "œuf|œufs", "oeuf", 110), S],
        ["Écosser les petits pois.", "Faire fondre le beurre, ajouter les oignons, les pois et la laitue émincée.",
         "Couvrir et cuire 15 min à feu doux avec un fond d'eau.", "Servir avec des œufs mollets (6 min)."],
        tip="La laitue cuite donne une sauce douce : on ne la jette pas !")
    r("pois-gourmands-maquereau", "Pois gourmands sautés et maquereau grillé", "Plat", 20, "poisson", ["Pois gourmands"], [
        (300, "g", "de pois gourmands", "petitspois", 300), (2, "", "maquereau|maquereaux", "maquereau", 300), (1, "c. à soupe", "de sauce soja", "soja", 15),
        (1, "c. à café", "de gingembre râpé", "epice", 5), (1, "c. à soupe", "d'huile", "huile", 10), (120, "g", "de riz", "riz", 120)],
        ["Cuire le riz.", "Griller les filets de maquereau côté peau 4 min.", "Sauter les pois gourmands 3 min avec le gingembre, ajouter la sauce soja.",
         "Servir le poisson sur les légumes croquants."], f="Maquereau", c="asie", o="Japon")
    r("aioli-provencal", "Aïoli de légumes et œufs durs", "Plat", 40, "vege", ["Ail", "Haricot vert"], [
        (2, "gousse", "d'ail", "ail", 8), (2, "", "œuf dur|œufs durs", "oeuf", 110), (200, "g", "de haricots verts", "haricotvert", 200),
        (1, "", "courgette|courgettes", "courgette", 150), (300, "g", "de pommes de terre", "pdt", 300), (1, "", "œuf|œufs", "oeuf", 55),
        (10, "cl", "d'huile d'olive", "huile", 60), S],
        ["Cuire pommes de terre, courgette et haricots à la vapeur.", "Cuire les œufs 10 min et les écaler.",
         "Piler l'ail, ajouter le jaune d'œuf et monter l'huile en filet comme une mayonnaise.", "Servir tiède avec l'aïoli."], o="Provence")
    # ---------- Fruits ----------
    r("crumble-cassis-pomme", "Petits crumbles abricot et cassis", "Dessert", 35, "vege", ["Cassis"], [
        (150, "g", "de cassis", "cassis", 150), (250, "g", "d'abricots", "abricot", 250), (40, "g", "de farine", "farine", 40),
        (30, "g", "de flocons d'avoine", "avoine", 30), (40, "g", "de beurre", "beurre", 40), (40, "g", "de sucre", "sucre", 40)],
        ["Préchauffer le four à 180 °C.", "Répartir les abricots en morceaux et le cassis dans deux ramequins.",
         "Sabler farine, avoine, sucre et beurre du bout des doigts.", "Couvrir les fruits, cuire 25 min."], sweet=True)
    r("pancakes-myrtilles", "Pancakes aux myrtilles", "Dessert", 25, "vege", ["Myrtille"], [
        (150, "g", "de myrtilles", "myrtille", 150), (100, "g", "de farine", "farine", 100), (1, "", "œuf|œufs", "oeuf", 55), (15, "cl", "de lait", "lait", 150),
        (1, "c. à soupe", "de sucre", "sucre", 15), (1, "c. à café", "de levure", "epice", 4), (10, "g", "de beurre", "beurre", 10)],
        ["Mélanger farine, levure et sucre, puis l'œuf et le lait.", "Ajouter la moitié des myrtilles.",
         "Cuire de petites louches 2 min par face dans une poêle beurrée.", "Servir avec le reste des myrtilles."], sweet=True, c="ameriques", o="États-Unis")
    r("clafoutis-mirabelles", "Clafoutis aux mirabelles", "Dessert", 45, "vege", ["Mirabelle"], [
        (400, "g", "de mirabelles", "mirabelle", 400), (2, "", "œuf|œufs", "oeuf", 110), (40, "g", "de farine", "farine", 40),
        (20, "cl", "de lait", "lait", 200), (50, "g", "de sucre", "sucre", 50), (10, "g", "de beurre", "beurre", 10)],
        ["Préchauffer le four à 180 °C, beurrer un plat.", "Dénoyauter les mirabelles et les étaler dans le plat.",
         "Fouetter œufs, sucre, farine et lait.", "Verser sur les fruits, cuire 35 min."], sweet=True, parts=4, o="Lorraine")
    r("yaourt-mures-miel", "Yaourt glacé aux mûres et au miel", "Dessert", 10, "vege", ["Mûre"], [
        (200, "g", "de mûres", "mure", 200), (2, "", "yaourt grec|yaourts grecs", "yaourt", 300), (1, "c. à soupe", "de miel", "miel", 15),
        (20, "g", "d'amandes effilées", "amande", 20)],
        ["Écraser la moitié des mûres avec le miel.", "Marbrer les yaourts avec cette purée.", "Ajouter les mûres entières et les amandes grillées, servir frais."],
        sweet=True)
    r("nectarines-roties-romarin", "Nectarines rôties au romarin et miel", "Dessert", 25, "vege", ["Nectarine"], [
        (3, "", "nectarine|nectarines", "peche", 450), (1, "c. à soupe", "de miel", "miel", 20), (1, "brin", "de romarin", "herbe", 2),
        (2, "c. à soupe", "de fromage blanc", "fromageblanc", 60)],
        ["Préchauffer le four à 200 °C.", "Couper les nectarines en deux, les dénoyauter.", "Arroser de miel, ajouter le romarin, rôtir 15 min.",
         "Servir tiède avec le fromage blanc."], sweet=True)
    r("melon-feta-menthe", "Melon, feta et menthe", "Entrée", 10, "vege", ["Melon"], [
        (1, "", "melon|melons", "melon", 600), (80, "g", "de feta", "chevre", 80), (0.5, "botte", "de menthe", "herbe", 5),
        (1, "c. à soupe", "d'huile d'olive", "huile", 10)],
        ["Couper le melon en cubes.", "Ajouter la feta émiettée et la menthe ciselée.", "Arroser d'un filet d'huile et poivrer."], c="orient", o="Grèce")
    r("financiers-noisette", "Financiers à la noisette", "Dessert", 30, "vege", ["Noisette"], [
        (60, "g", "de noisettes en poudre", "noisette", 60), (60, "g", "de beurre", "beurre", 60), (2, "", "blanc d'œuf|blancs d'œufs", "oeuf", 60),
        (60, "g", "de sucre", "sucre", 60), (25, "g", "de farine", "farine", 25)],
        ["Préchauffer le four à 200 °C.", "Faire fondre le beurre jusqu'à ce qu'il sente la noisette.",
         "Mélanger poudre de noisette, sucre, farine, puis les blancs et le beurre.", "Verser dans des moules, cuire 12 min."], sweet=True, parts=6)
    r("salade-mandarines-kiwis", "Salade de mandarines, kiwis et menthe", "Dessert", 15, "vege", ["Mandarine", "Kiwi"], [
        (4, "", "mandarine|mandarines", "orange", 320), (2, "", "kiwi|kiwis", "kiwi", 160),
        (1, "c. à soupe", "de miel", "miel", 15), (0.5, "botte", "de menthe", "herbe", 5)],
        ["Peler les mandarines et les séparer en quartiers, couper les kiwis en rondelles.", "Arroser du jus d'une mandarine mélangé au miel.", "Parsemer de menthe ciselée, servir frais."], sweet=True)
    r("pamplemousse-avocat-sardines", "Salade de pamplemousse, avocat et sardines", "Entrée", 15, "poisson", ["Pamplemousse"], [
        (1, "", "pamplemousse rose|pamplemousses roses", "pamplemousse", 300), (1, "", "avocat|avocats", "avocat", 150),
        (1, "boîte", "de sardines à l'huile", "sardine", 120), (50, "g", "de jeunes pousses", "mache", 50), S],
        ["Prélever les suprêmes de pamplemousse.", "Couper l'avocat en tranches.", "Dresser sur les pousses avec les sardines émiettées, arroser du jus du pamplemousse."])
    r("kiwis-yaourt-granola", "Kiwis, yaourt et granola maison", "Dessert", 15, "vege", ["Kiwi"], [
        (3, "", "kiwi|kiwis", "kiwi", 250), (2, "", "yaourt|yaourts", "yaourt", 250), (40, "g", "de flocons d'avoine", "avoine", 40),
        (1, "c. à soupe", "de miel", "miel", 15), (15, "g", "de noisettes", "noisette", 15)],
        ["Faire griller à sec avoine et noisettes 5 min, ajouter le miel.", "Couper les kiwis en dés.", "Superposer yaourt, kiwis et granola."], sweet=True)

    # ---------- Poissons et fruits de mer ----------
    r("seiches-plancha", "Seiches à la plancha, persillade et riz", "Plat", 25, "poisson", [], [
        (400, "g", "de seiches nettoyées", "seiche", 400), (2, "gousse", "d'ail", "ail", 8), (0.5, "botte", "de persil", "herbe", 10),
        (0.5, "", "citron|citrons", "citron", 30), (1, "c. à soupe", "d'huile d'olive", "huile", 15), (120, "g", "de riz", "riz", 120), S],
        ["Cuire le riz.", "Inciser les seiches en croisillons, les saisir 2 min par face à feu très vif.",
         "Ajouter ail et persil hachés hors du feu.", "Servir avec le riz et un trait de citron."], f="Seiche", o="Sète")
    r("saint-jacques-petits-pois", "Saint-Jacques snackées, crème de petits pois", "Plat", 30, "poisson", ["Petits pois"], [
        (8, "", "noix de Saint-Jacques|noix de Saint-Jacques", "stjacques", 240), (600, "g", "de petits pois à écosser", "petitspois", 250),
        (5, "cl", "de crème", "creme", 50), (10, "g", "de beurre", "beurre", 10), (0.5, "botte", "de menthe", "herbe", 5), S],
        ["Cuire les petits pois 8 min à l'eau, les mixer avec la crème et la menthe.", "Sécher les Saint-Jacques.",
         "Les saisir 1 min par face dans le beurre très chaud.", "Servir sur la crème de petits pois."], f="Saint-Jacques")
    r("sardines-escabeche", "Sardines en escabèche", "Entrée", 25, "poisson", [], [
        (8, "", "sardine|sardines", "sardine", 300), (1, "", "oignon|oignons", "oignon", 100), (1, "", "carotte|carottes", "carotte", 80),
        (5, "cl", "de vinaigre de vin", "epice", 10), (3, "c. à soupe", "d'huile d'olive", "huile", 30), (1, "", "feuille de laurier|feuilles de laurier", "herbe", 1), S],
        ["Fariner légèrement les filets de sardine et les dorer 1 min par face.", "Faire revenir oignon et carotte émincés, ajouter vinaigre et laurier.",
         "Verser chaud sur les sardines.", "Laisser mariner au frais au moins 2 h."], f="Sardine", c="med", o="Espagne")
    r("encornets-ail-persil", "Encornets sautés à l'ail et au piment d'Espelette", "Plat", 20, "poisson", [], [
        (400, "g", "d'encornets", "encornet", 400), (2, "gousse", "d'ail", "ail", 8), (0.5, "c. à café", "de piment d'Espelette", "epice", 2),
        (0.5, "botte", "de persil", "herbe", 10), (1, "c. à soupe", "d'huile d'olive", "huile", 15), (120, "g", "de riz", "riz", 120), S],
        ["Cuire le riz.", "Couper les encornets en anneaux, les sécher.", "Les saisir 2 min à feu très vif dans l'huile.",
         "Ajouter ail, piment et persil, servir aussitôt."], f="Encornet", o="Pays basque")
    r("rougets-papillote", "Rougets en papillote, citron et thym", "Plat", 25, "poisson", [], [
        (4, "", "filet de rouget|filets de rouget", "rouget", 300), (1, "", "citron|citrons", "citron", 60), (0.5, "botte", "de thym", "herbe", 5),
        (1, "c. à soupe", "d'huile d'olive", "huile", 15), (300, "g", "de pommes de terre", "pdt", 300), S],
        ["Préchauffer le four à 200 °C, cuire les pommes de terre à l'eau.", "Déposer les filets sur du papier cuisson avec citron, thym et huile.",
         "Fermer les papillotes, cuire 12 min.", "Servir avec les pommes de terre."], f="Rouget")
    r("bar-puree-celeri", "Bar rôti, purée de céleri", "Plat", 40, "poisson", ["Céleri-rave"], [
        (2, "", "filet de bar|filets de bar", "bar", 300), (0.5, "", "céleri-rave|céleris-raves", "celeri", 400), (10, "cl", "de lait", "lait", 100),
        (15, "g", "de beurre", "beurre", 15), (1, "c. à soupe", "d'huile d'olive", "huile", 10), (0.5, "", "citron|citrons", "citron", 30), S],
        ["Cuire le céleri en morceaux 20 min dans le lait et un peu d'eau.", "Le mixer avec le beurre.",
         "Rôtir le bar côté peau 4 min à la poêle, puis 1 min de l'autre côté.", "Servir sur la purée avec un trait de citron."], f="Bar")
