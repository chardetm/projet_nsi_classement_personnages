class CalculateurElo:
    """
    Classe proposant une implantation simplifiée du système ELO (voir https://fr.wikipedia.org/wiki/Classement_Elo).
    """

    def __init__(self, k=32):
        """
        Initialise un calculateur d'ELO avec le coefficient k.
        :param k: coefficient de développement K (plus K est élevé, plus les changements dans le classement seront
        importants)
        """

        self.k = k

    @staticmethod
    def _resultat_attendu(score, score_adversaire):
        """
        Calcule le résultat attendu d'un match du point de vue d'un participant en fonction de son score actuel et de
        celui de son adversaire.

        :param score: score du participant avant le match (float)
        :param score_adversaire: score de son adversaire avant le match (float)
        :return: résultat attendu du match (float)
        """

        return 1 / (1 + 10 ** ((score_adversaire - score) / 400))

    def nouveau_score(self, score, score_adversaire, resultat):
        """
        Calcule le nouveau score du participant d'un match en fonction de son score actuel, de celui de son adversaire
        et du résultat du match.

        :param score: score du participant avant le match (float)
        :param score_adversaire: score de son adversaire avant le match (float)
        :param resultat: 1.0 pour une victoire, 0.5 pour un nul et 0.0 pour une défaite (float)
        :return: nouveau score du participant (float)
        """

        resultat_attendu = self._resultat_attendu(score, score_adversaire)
        return score + self.k * (resultat - resultat_attendu)

    def nouveau_score_gagnant(self, score_gagnant, score_perdant):
        """
        Calcule le nouveau score du gagnant d'un match en fonction de son score actuel et de celui de son adversaire.

        :param score_gagnant: score du gagnant avant le match (float)
        :param score_perdant: score du perdant avant le match (float)
        :return: nouveau score du gagnant (float)
        """

        return self.nouveau_score(score_gagnant, score_perdant, 1)

    def nouveau_score_perdant(self, score_perdant, score_gagnant):
        """
        Calcule le nouveau score du perdant d'un match en fonction de son score actuel et de celui de son adversaire.

        :param score_perdant: score du perdant avant le match (float)
        :param score_gagnant: score du gagnant avant le match (float)
        :return: nouveau score du perdant (float)
        """

        return self.nouveau_score(score_perdant, score_gagnant, 0)
