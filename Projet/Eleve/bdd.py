import sqlite3


class BDD:
    """
    Classe permettant de manipuler une base de données SQLite 3 stockant une liste de personnages avec un score et une
    liste de matchs, en cours ou terminés.
    """

    def __init__(self, chemin_fichier_bdd):
        """
        Crée le fichier de base de données au format SQLite 3 s'il n'existe pas déjà et crée les tables nécessaires si
        elles n'existent pas déjà.

        :param chemin_fichier_bdd: chemin du fichier de base de données, ou :memory: pour la créer en mémoire vive
        """

        ...

    def ajouter_personnage(self, infos_personnage):
        """
        Ajoute un personnage et renvoie son ID.

        :param infos_personnage: dictionnaire contenant les informations du personnage (clés : nom (str),
        url_image (str), acteur (str), score (float))
        :return: identifiant du personnage ajouté (int)
        """

        ...

    def ajouter_personnages(self, liste_infos_personnages):
        """
        Ajoute plusieurs personnages.

        :param liste_infos_personnages: itérable de dictionnaires contenant les informations du personnage (clés :
        nom (str), url_image (str), acteur (str), score (float))
        :return: None
        """

        ...

    def nombre_personnages(self):
        """
        Renvoie le nombre de personnages présents dans la base de données.

        :return: nombre de personnages (int)
        """

        ...

    @staticmethod
    def _dictionnaire_infos_personnage(tableau_infos_personnage):
        """
        Transforme un tableau contenant les informations d'un personnage en dictionnaire.

        :param tableau_infos_personnage: tableau contenant les informations d'un personnage : [id (int), nom (str),
        url_image (str), acteur (str), score (float)]
        :return: dictionnaire (clés : id (int), nom (str), url_image (str), acteur (str), score (float))
        """

        assert len(tableau_infos_personnage) == 5
        return {
            "id":        tableau_infos_personnage[0],
            "nom":       tableau_infos_personnage[1],
            "url_image": tableau_infos_personnage[2],
            "acteur":    tableau_infos_personnage[3],
            "score":     tableau_infos_personnage[4]
        }

    def personnage(self, id_personnage):
        """
        Renvoie les informations d'un personnage en fonction de son ID.

        :param id_personnage: identifiant du personnage (int)
        :return: dictionnaire (clés : id (int), nom (str), url_image (str), acteur (str), score (float)) si le
        personnage existe, sinon None
        """

        ...

    def personnages(self):
        """
        Renvoie les informations de tous les personnages triés par ordre décroissant de score.

        :return: liste de dictionnaires (clés : id (int), nom (str), url_image (str), acteur (str), score (float))
        """

        ...
        return []

    def changer_score_personnage(self, id_personnage, nouveau_score):
        """
        Change le score d'un personnage en fonction de son ID.

        :param id_personnage: identifiant du personnage (int)
        :param nouveau_score: nouveau score du personnage (float)
        :return: None
        """

        ...

    def ajouter_match(self, infos_match):
        """
        Ajoute un match et renvoie son ID.

        :param infos_match: dictionnaire contenant les informations du match (clés : id_gagnant (int), id_perdant (int),
        ancien_score_gagnant (float), ancien_score_perdant (float), nouveau_score_gagnant (float),
        nouveau_score_perdant (float))
        :return: identifiant du match ajouté (int)
        """

        ...

    @staticmethod
    def _dictionnaire_infos_match(tableau_infos_match):
        """
        Transforme un tableau contenant les informations d'un match avec nom des personnages en dictionnaire.

        :param tableau_infos_match: tableau contenant les informations d'un match : [id (int), id_gagnant (int),
        id_perdant (int), ancien_score_gagnant (float), ancien_score_perdant (float), nouveau_score_gagnant (float),
        nouveau_score_perdant (float), nom_gagnant (str), nom_perdant (str)]
        :return: dictionnaire (clés : id (int), id_gagnant (int), id_perdant (int), ancien_score_gagnant (float),
        ancien_score_perdant (float), nouveau_score_gagnant (float), nouveau_score_perdant (float), nom_gagnant (str),
        nom_perdant (str))
        """

        assert len(tableau_infos_match) == 9
        return {
            "id":                    tableau_infos_match[0],
            "id_gagnant":            tableau_infos_match[1],
            "id_perdant":            tableau_infos_match[2],
            "ancien_score_gagnant":  tableau_infos_match[3],
            "ancien_score_perdant":  tableau_infos_match[4],
            "nouveau_score_gagnant": tableau_infos_match[5],
            "nouveau_score_perdant": tableau_infos_match[6],
            "nom_gagnant":           tableau_infos_match[7],
            "nom_perdant":           tableau_infos_match[8]
        }

    def matchs(self):
        """
        Renvoie les informations de tous les matchs avec nom des personnages triés par ordre décroissant d'identifiants.

        :return: liste de dictionnaires (clés : id (int), id_gagnant (int), id_perdant (int),
        ancien_score_gagnant (float), ancien_score_perdant (float), nouveau_score_gagnant (float),
        nouveau_score_perdant (float), nom_gagnant (str), nom_perdant (str))
        """

        ...
        return []

    def ajouter_match_en_cours(self, infos_match_en_cours):
        """
        Ajoute un match en cours et renvoie son ID.

        :param infos_match_en_cours: dictionnaire contenant les informations du match en cours (clés :
        id_personnage1 (int), id_personnage2 (int))
        :return: identifiant du match en cours ajouté (int)
        """

        ...

    @staticmethod
    def _dictionnaire_infos_match_en_cours(tableau_infos_match_en_cours):
        """
        Transforme un tableau contenant les informations d'un match en cours en dictionnaire.

        :param tableau_infos_match_en_cours: tableau contenant les informations d'un match en cours : [id (int),
        id_personnage1 (int), id_personnage2 (int)]
        :return: dictionnaire (clés : id (int), id_personnage1 (int), id_personnage2 (int))
        """

        assert len(tableau_infos_match_en_cours) == 3
        return {
            "id":             tableau_infos_match_en_cours[0],
            "id_personnage1": tableau_infos_match_en_cours[1],
            "id_personnage2": tableau_infos_match_en_cours[2]
        }

    def match_en_cours(self, id_match_en_cours):
        """
        Renvoie les informations d'un match en cours en fonction de son ID.

        :param id_match_en_cours: identifiant du match en cours (int)
        :return: dictionnaire (clés : id (int), id_personnage1 (int), id_personnage2 (int)) si le match en cours existe,
        sinon None
        """

        ...

    def supprimer_match_en_cours(self, id_match_en_cours):
        """
        Supprime un match en cours en fonction de son ID
        :param id_match_en_cours: identifiant du match en cours à supprimer (int)
        :return: None
        """

        ...

    def fermer(self):
        """
        Ferme la connexion au fichier de base de données, l'instance de classe ne peut ensuite plus être utilisée.
        :return: None
        """

        ...


# =============================================
# =================== Tests ===================
# =============================================

class TestBDD:
    avec_matchs_en_cours = True
    harry = {
        "nom": "Harry Potter",
        "url_image": "./hpotter.jpg",
        "acteur": "Daniel Radcliffe",
        "score": 1200
    }
    hermione = {
        "nom": "Hermione Granger",
        "url_image": "./hgranger.jpg",
        "acteur": "Emma Watson",
        "score": 1300
    }
    ron = {
        "nom": "Ron Weasley",
        "url_image": "./jeannedupond.jpg",
        "acteur": "Rupert Grint",
        "score": 1100
    }

    def test_constructeur(self):
        import os
        fichier_bdd_test = "test/test_constructeur.db"
        if os.path.exists(fichier_bdd_test):
            os.remove(fichier_bdd_test)
        bdd = BDD(fichier_bdd_test)

        liste_tables = {"personnages",
                        "matchs",
                        "matchs_en_cours"} if self.avec_matchs_en_cours else {"personnages",
                                                                              "matchs"}

        curseur = bdd.connexion.cursor()
        curseur.execute('''SELECT name
                           FROM sqlite_master
                           WHERE type ="table" AND name NOT LIKE "sqlite_%"''')
        liste_tables_bdd = [r[0] for r in curseur.fetchall()]
        assert set(liste_tables_bdd) == liste_tables

        bdd.fermer()
        os.remove(fichier_bdd_test)

    def test_ajouter_personnage(self):
        import os
        fichier_bdd_test = "test/test_ajouter_personnage.db"
        if os.path.exists(fichier_bdd_test):
            os.remove(fichier_bdd_test)
        bdd = BDD(fichier_bdd_test)

        assert bdd.nombre_personnages() == 0
        id_harry = bdd.ajouter_personnage(self.harry)
        assert bdd.nombre_personnages() == 1
        assert id_harry == 1
        id_hermione = bdd.ajouter_personnage(self.hermione)
        assert bdd.nombre_personnages() == 2
        assert id_hermione == 2
        id_ron = bdd.ajouter_personnage(self.ron)
        assert bdd.nombre_personnages() == 3
        assert id_ron == 3

        bdd.fermer()
        os.remove(fichier_bdd_test)

    def test_ajouter_personnages(self):
        import os
        fichier_bdd_test = "test/test_ajouter_personnages.db"
        if os.path.exists(fichier_bdd_test):
            os.remove(fichier_bdd_test)
        bdd = BDD(fichier_bdd_test)

        assert bdd.nombre_personnages() == 0
        bdd.ajouter_personnages([])
        assert bdd.nombre_personnages() == 0
        bdd.ajouter_personnages([self.harry])
        assert bdd.nombre_personnages() == 1
        bdd.ajouter_personnages([self.hermione, self.ron])
        assert bdd.nombre_personnages() == 3

        bdd.fermer()
        os.remove(fichier_bdd_test)

    def test_personnage(self):
        import os
        fichier_bdd_test = "test/test_personnage.db"
        if os.path.exists(fichier_bdd_test):
            os.remove(fichier_bdd_test)
        bdd = BDD(fichier_bdd_test)

        bdd.ajouter_personnages([self.harry, self.hermione, self.ron])
        assert bdd.nombre_personnages() == 3

        personnage_id_1 = bdd.personnage(1)
        assert personnage_id_1["id"] == 1
        personnage_id_1.pop("id")
        assert personnage_id_1 == self.harry

        personnage_id_2 = bdd.personnage(2)
        assert personnage_id_2["id"] == 2
        personnage_id_2.pop("id")
        assert personnage_id_2 == self.hermione

        personnage_id_3 = bdd.personnage(3)
        assert personnage_id_3["id"] == 3
        personnage_id_3.pop("id")
        assert personnage_id_3 == self.ron

        personnage_id_4 = bdd.personnage(4)
        assert personnage_id_4 is None

        bdd.fermer()
        os.remove(fichier_bdd_test)

    def test_personnages(self):
        import os
        fichier_bdd_test = "test/test_personnages.db"
        if os.path.exists(fichier_bdd_test):
            os.remove(fichier_bdd_test)
        bdd = BDD(fichier_bdd_test)

        personnages_tri_score = bdd.personnages()
        assert len(personnages_tri_score) == 0

        bdd.ajouter_personnages([self.harry, self.hermione, self.ron])

        personnages_tri_score = bdd.personnages()
        assert personnages_tri_score[0]["id"] == 2  # Hermione
        assert personnages_tri_score[1]["id"] == 1  # Harry
        assert personnages_tri_score[2]["id"] == 3  # Ron

        bdd.fermer()
        os.remove(fichier_bdd_test)

    def test_changer_score_personnage(self):
        import os
        fichier_bdd_test = "test/test_changer_score_personnage.db"
        if os.path.exists(fichier_bdd_test):
            os.remove(fichier_bdd_test)
        bdd = BDD(fichier_bdd_test)

        bdd.ajouter_personnages([self.harry, self.hermione, self.ron])
        bdd.changer_score_personnage(1, 800)
        harry_bdd = bdd.personnage(1)
        assert harry_bdd["score"] == 800
        bdd.changer_score_personnage(2, 1700)
        hermione_bdd = bdd.personnage(2)
        assert hermione_bdd["score"] == 1700

        bdd.fermer()
        os.remove(fichier_bdd_test)

    def test_match(self):
        import os
        fichier_bdd_test = "test/test_match.db"
        if os.path.exists(fichier_bdd_test):
            os.remove(fichier_bdd_test)
        bdd = BDD(fichier_bdd_test)

        bdd.ajouter_personnages([self.harry, self.hermione, self.ron])
        match1 = {
            "id_gagnant": 3,
            "id_perdant": 2,
            "ancien_score_gagnant": 1100,
            "ancien_score_perdant":  1300,
            "nouveau_score_gagnant": 1150,
            "nouveau_score_perdant": 1250
        }
        match2 = {
            "id_gagnant": 2,
            "id_perdant": 1,
            "ancien_score_gagnant": 1250,
            "ancien_score_perdant":  1200,
            "nouveau_score_gagnant": 1300,
            "nouveau_score_perdant": 1150
        }
        id_match1 = bdd.ajouter_match(match1)
        assert id_match1 == 1
        id_match2 = bdd.ajouter_match(match2)
        assert id_match2 == 2
        matchs = bdd.matchs()
        assert matchs[0]["id"] == 2
        assert matchs[0]["nom_gagnant"] == "Hermione Granger"
        assert matchs[0]["nom_perdant"] == "Harry Potter"
        matchs[0].pop("id")
        matchs[0].pop("nom_gagnant")
        matchs[0].pop("nom_perdant")
        assert matchs[0] == match2

        assert matchs[1]["id"] == 1
        assert matchs[1]["nom_gagnant"] == "Ron Weasley"
        assert matchs[1]["nom_perdant"] == "Hermione Granger"
        matchs[1].pop("id")
        matchs[1].pop("nom_gagnant")
        matchs[1].pop("nom_perdant")
        assert matchs[1] == match1

        bdd.fermer()
        os.remove(fichier_bdd_test)

    def test_match_en_cours(self):
        if not self.avec_matchs_en_cours:
            return
        import os
        fichier_bdd_test = "test/test_match_en_cours.db"
        if os.path.exists(fichier_bdd_test):
            os.remove(fichier_bdd_test)
        bdd = BDD(fichier_bdd_test)

        bdd.ajouter_personnages([self.harry, self.hermione, self.ron])
        match_en_cours1 = {
            "id_personnage1": 3,
            "id_personnage2": 2
        }
        match_en_cours2 = {
            "id_personnage1": 2,
            "id_personnage2": 1
        }
        id_match_en_cours1 = bdd.ajouter_match_en_cours(match_en_cours1)
        assert id_match_en_cours1 == 1
        id_match_en_cours2 = bdd.ajouter_match_en_cours(match_en_cours2)
        assert id_match_en_cours2 == 2

        match_en_cours_bdd_none = bdd.match_en_cours(100)
        assert match_en_cours_bdd_none is None

        match_en_cours_bdd1 = bdd.match_en_cours(1)
        assert match_en_cours_bdd1["id"] == 1
        match_en_cours_bdd1.pop("id")
        assert match_en_cours_bdd1 == match_en_cours1

        match_en_cours_bdd2 = bdd.match_en_cours(2)
        assert match_en_cours_bdd2["id"] == 2
        match_en_cours_bdd2.pop("id")
        assert match_en_cours_bdd2 == match_en_cours2

        bdd.supprimer_match_en_cours(1)
        match_en_cours_bdd_none = bdd.match_en_cours(1)
        assert match_en_cours_bdd_none is None

        match_en_cours_bdd2 = bdd.match_en_cours(2)
        match_en_cours_bdd2.pop("id")
        assert match_en_cours_bdd2 == match_en_cours2

        bdd.supprimer_match_en_cours(2)
        match_en_cours_bdd_none = bdd.match_en_cours(2)
        assert match_en_cours_bdd_none is None

        bdd.fermer()
        os.remove(fichier_bdd_test)


# Si on n'utilise pas pytest depuis le terminal, lancer les tests directement
if __name__ == "__main__":
    import pytest
    pytest.main(["bdd.py"])
