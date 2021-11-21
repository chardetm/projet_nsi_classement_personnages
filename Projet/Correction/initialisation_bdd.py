import urllib.request
import json


def recuperer_infos_personnages(nb_apparitions_min):
    """
    Récupère les informations des personnages de la série en utilisant une API.

    :param nb_apparitions_min: nombre d'apparition minimum pour qu'un personnage soit inclus dans la liste
    :return: liste d'informations sur les personnages (dictionnaire, clés : nom (str), acteur (str), url_image (str))
    """

    # Appelle l'API "api.got.show" pour obtenir la liste des personnages
    api_url = "https://api.got.show/api/show/characters"
    # api_url = "http://localhost/characters_backup.json"
    liste_personnages = json.loads(urllib.request.urlopen(api_url).read())

    # On simplifie la liste : on ne garde que les personnages qui sont
    # apparus un certain nombre de fois, et on garde uniquement leur nom,
    # leur acteur et une URL d'image
    ma_liste = []
    for personnage in liste_personnages:
        if len(personnage["appearances"]) >= nb_apparitions_min:
            ma_liste.append({
                "nom":       personnage["name"],
                "acteur":    personnage["actor"],
                "url_image": personnage["image"]
            })

    return ma_liste


def remplir_bdd(bdd, score_initial, nb_apparitions_min):
    """
    Récupère les infos des personnages et les ajoute à la base de données si cette dernière est vide.

    :param bdd: objet base de données (type BDD du fichier `bdd.py`)
    :param score_initial: score initial à donner aux personnages (float)
    :param nb_apparitions_min: nombre d'apparitions minimum pour qu'un personnage soit ajouté à la base de données (int)
    :return: None
    """

    if bdd.nombre_personnages() == 0:  # Si la base de données est vide
        print("Base de données vide, récupération de la liste de personnages...")
        infos_personnages = recuperer_infos_personnages(nb_apparitions_min)
        for infos_perso in infos_personnages:
            infos_perso["score"] = score_initial

        bdd.ajouter_personnages(infos_personnages)

        # On affiche dans la console du serveur le nombre de personnages ajoutés
        print("%d personnages ajoutés !" % len(infos_personnages))

    else:  # Si la base de données n'est pas vide
        print("Chargement de la base de données existante...")
