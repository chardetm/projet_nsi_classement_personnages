import flask

from bdd import BDD


# Configuration de l'application
app = flask.Flask(__name__)
bdd = BDD("bdd.db")


# Points d'entrée

# Page principale de match
@app.route('/')
@app.route('/vote/<int:id_match_en_cours>/<int:choix>/')
def match(id_match_en_cours=None, choix=None):
    return flask.Response(flask.render_template(
        "match.html.jinja2",
        chemin_css=flask.url_for("static", filename="css/style.css"),
        id_match_en_cours=...,
        personnage1=...,
        personnage2=...
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
