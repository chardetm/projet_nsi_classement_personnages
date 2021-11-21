class Annuaire:
    """
    Permet de stocker un ensemble de contacts ainsi que leurs numéro de téléphone
    et adresse e-mail.
    """

    def __init__(self):
        """
        Construit un nouvel annuaire vide.
        """
        self.__liste_dictionnaires_contacts = []

    def ajouter_contact(self, nom, prenom = None, numero = None, email = None):
        """
        Ajoute un contact à l'annuaire.
        :param nom: chaîne de caractères, nom de famille ou surnom du contact
        :param prenom: chaîne de caractères (optionnel), prénom du contact
        :param numero: entier (optionnel), numéro de téléphone du contact
        :param email: chaîne de caractères (optionnel), adresse e-mail du contact
        :return: None
        """
        self.__liste_dictionnaires_contacts.append({
            "nom": nom,
            "prenom": prenom,
            "numero": numero,
            "email": email
        })

    def nombre_contacts(self):
        """
        Permet de connaître le nombre de contacts présents dans l'annuaire.
        :return: entier, nombre de contacts
        """
        return len(self.__liste_dictionnaires_contacts)

    def __afficher_dictionnaire_contact(self, dictionnaire_contact):
        """
        Affiche un contact à partir de sa représentation interne (dictionnaire).
        :param dictionnaire_contact: dictionnaire, représentation interne du contact
        :return: None
        """
        print("- Nom :", dictionnaire_contact["nom"])
        if dictionnaire_contact["prenom"] is not None:
            print("  Prenom :", dictionnaire_contact["prenom"])
        if dictionnaire_contact["numero"] is not None:
            print("  Numéro :", dictionnaire_contact["numero"].rjust(10, "0"))
        if dictionnaire_contact["email"] is not None:
            print("  E-mail :", dictionnaire_contact["email"])

    def afficher_contact(self, id):
        """
        Affiche un contact particulier à partir de son identifiant.
        :param id: entier, identifiant du contact à afficher.
        :return: None
        """
        assert id < len(self.__liste_dictionnaires_contacts)
        dictionnaire_contact = self.__liste_dictionnaires_contacts[id]
        self.__afficher_dictionnaire_contact(dictionnaire_contact)

    def afficher_tous_contacts(self):
        """
        Affiche tous les contacts
        :return: None
        """
        for dictionnaire_contact in self.__liste_dictionnaires_contacts:
            self.__afficher_dictionnaire_contact(dictionnaire_contact)

    def rechercher_contacts(self, requete):
        """
        Permet de rechercher des contacts à partir d'un motif (recherche dans nom, prénom, numéro de téléphone et
        adresse e-mail).
        :param requete: chaîne de caractère, motif à rechercher
        :return: liste d'entiers, identifiants des contacts correspondants
        """
        contacts = []
        for id in range(len(self.__liste_dictionnaires_contacts)):
            dictionnaire_contact = self.__liste_dictionnaires_contacts[id]
            recherche = self.__liste_dictionnaires_contacts[id]["nom"]
            if dictionnaire_contact["prenom"] is not None:
                recherche += (" " + dictionnaire_contact["prenom"]
                              + " " + self.__liste_dictionnaires_contacts[id]["nom"])
            if dictionnaire_contact["numero"] is not None:
                recherche += (" " + dictionnaire_contact["numero"].rjust(10, "0"))
            if dictionnaire_contact["email"] is not None:
                recherche += (" " + dictionnaire_contact["email"])

            if requete in recherche:
                contacts.append(id)
        return contacts


if __name__ == '__main__':
    annuaire = Annuaire()
    assert annuaire.nombre_contacts() == 0
    annuaire.ajouter_contact("Dupond", "Martin", "0123456789", "martin.dupond@fournisseur.fr")
    annuaire.ajouter_contact("Dupond", "Sylvie", "0123456787", "sylvie.dupond@fournisseur.fr")
    annuaire.ajouter_contact("Kenz", "Amine", "0987654321", "amine.kenz@autref.fr")
    annuaire.ajouter_contact("Grassa", "Sarah", "0987654323", "sarah.grassa@autref.fr")
    assert annuaire.nombre_contacts() == 4
    annuaire.afficher_tous_contacts()
    for id_contact in annuaire.rechercher_contacts("pond"):
        annuaire.afficher_contact(id_contact)
