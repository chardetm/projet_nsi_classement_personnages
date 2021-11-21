from elo import CalculateurElo


calculateur_elo = CalculateurElo()


def appliquer_resultat_match(bdd, id_match_en_cours, choix):
    """
    Etant donnés un identifiant de match en cours et un choix fait par l'utilisateur, met à jour la base de données en
    mettant à jour les scores de chaque personnage.

    :param bdd: objet base de données (type BDD du fichier `bdd.py`)
    :param id_match_en_cours: identifiant du match en cours (int)
    :param choix: choix fait par l'utilisateur (int, 1 ou 2)
    :return: None
    """

    # On récupère toutes les infos
    match_en_cours = bdd.match_en_cours(id_match_en_cours)
    id_gagnant = match_en_cours["id_personnage1"] if choix == 1 else match_en_cours["id_personnage2"]
    id_perdant = match_en_cours["id_personnage1"] if choix == 2 else match_en_cours["id_personnage2"]
    gagnant = bdd.personnage(id_gagnant)
    perdant = bdd.personnage(id_perdant)

    # Si le perdant ou le gagnant n'a pas pu être trouvé avec son ID, il y a une erreur
    if gagnant is None or perdant is None:
        print("Résultat de match incorrect !")
        return

    # On garde en mémoire l'ancien score des personnages et on calcule leur nouveau score
    ancien_score_gagnant = gagnant["score"]
    ancien_score_perdant = perdant["score"]
    nouveau_score_gagnant = calculateur_elo.nouveau_score_gagnant(ancien_score_gagnant, ancien_score_perdant)
    nouveau_score_perdant = calculateur_elo.nouveau_score_perdant(ancien_score_perdant, ancien_score_gagnant)

    # Alternative plus simple aux deux lignes précédentes :
    # nouveau_score_gagnant = ancien_score_gagnant + 1
    # nouveau_score_perdant = ancien_score_perdant - 1

    bdd.changer_score_personnage(id_gagnant, nouveau_score_gagnant)
    bdd.changer_score_personnage(id_perdant, nouveau_score_perdant)

    bdd.ajouter_match({
        "id_gagnant":            id_gagnant,
        "id_perdant":            id_perdant,
        "ancien_score_gagnant":  ancien_score_gagnant,
        "ancien_score_perdant":  ancien_score_perdant,
        "nouveau_score_gagnant": nouveau_score_gagnant,
        "nouveau_score_perdant": nouveau_score_perdant
    })

    bdd.supprimer_match_en_cours(id_match_en_cours)

    # Affichage dans le terminal du serveur du résultat du match (log)
    print("%d : +%d (%d -> %d), %d : -%d (%d -> %d)" %
          (id_gagnant,
           nouveau_score_gagnant-ancien_score_gagnant,
           ancien_score_gagnant,
           nouveau_score_gagnant,
           id_perdant,
           ancien_score_perdant - nouveau_score_perdant,
           ancien_score_perdant,
           nouveau_score_perdant))


def creer_nouveau_match_en_cours(bdd):
    """
    Crée un nouveau match en cours entre deux personnages aléatoires et renvoie les informations du nouveau match en
    cours.

    :param bdd: objet base de données (type BDD du fichier `bdd.py`)
    :return: 3-uplet (id_nouveau_match_en_cours : int, personnage1 : dictionnaire (valeur de retour de BDD.personnage),
    personnage2 : dictionnaire (valeur de retour de BDD.personnage))
    """

    from random import randint

    nb_personnages = bdd.nombre_personnages()

    id_personnage1 = randint(1, nb_personnages)
    id_personnage2 = randint(1, nb_personnages-1)
    if id_personnage2 == id_personnage1:
        id_personnage2 = nb_personnages

    personnage1 = bdd.personnage(id_personnage1)
    personnage2 = bdd.personnage(id_personnage2)

    informations_nouveau_match = {
        "id_personnage1": personnage1["id"],
        "id_personnage2": personnage2["id"]
    }

    id_nouveau_match_en_cours = bdd.ajouter_match_en_cours(informations_nouveau_match)

    return id_nouveau_match_en_cours, personnage1, personnage2
