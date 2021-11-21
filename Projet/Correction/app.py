import flask

from bdd import BDD
from initialisation_bdd import remplir_bdd
from evolution_bdd import appliquer_resultat_match, creer_nouveau_match_en_cours


# Valeur initiale du score pour les nouveaux personnages
score_initial = 1400
# Lors du remplissage initial de la BDD, nombre d'apparitions minimum pour que le personnage soit ajouté
# (en nombre d'épisodes)
nb_apparences_min = 60


# Configuration de l'application
app = flask.Flask(__name__)
bdd = BDD("bdd.db")
remplir_bdd(bdd, score_initial, nb_apparences_min)


# Points d'entrée

# Page principale de match
@app.route('/')
@app.route('/vote/<int:id_match_en_cours>/<int:choix>/')
def match(id_match_en_cours=None, choix=None):
    if id_match_en_cours is not None:
        assert choix is not None
        appliquer_resultat_match(bdd, id_match_en_cours, choix)

    id_nouveau_match_en_cours, personnage1, personnage2 = creer_nouveau_match_en_cours(bdd)

    return flask.Response(flask.render_template(
        "match.html.jinja2",
        chemin_css=flask.url_for("static", filename="css/style.css"),
        id_match_en_cours=id_nouveau_match_en_cours,
        personnage1=personnage1,
        personnage2=personnage2
    ))


# Page de classement
@app.route('/classement/')
def classement():
    infos_personnages = bdd.personnages()
    infos_matchs = bdd.matchs()
    return flask.Response(flask.render_template(
        "classement.html.jinja2",
        chemin_css=flask.url_for("static", filename="css/style.css"),
        infos_personnages=infos_personnages,
        infos_matchs=infos_matchs
    ))


if __name__ == '__main__':
    app.run()
