import flask
import datetime

app = flask.Flask(__name__)

nb_visites = 0
contenu_liste_interactive = []


@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/heure/')
def heure():
    date_et_heure = datetime.datetime.now()
    return date_et_heure.strftime(
        "Nous sommes le %d/%m/%Y et il est %H:%M:%S."
    )

@app.route('/compteur/')
def compteur():
    global nb_visites
    nb_visites += 1
    return f"Cette page a été visitée {nb_visites} fois."

@app.route('/liste/')
def liste():
    return flask.Response(flask.render_template(
        "liste.html.jinja2",
        auteur_liste="Prénom Nom",
        contenu_liste=["Fruits", "Légumes", "Boissons"]
    ))

@app.route('/liste_interactive/', methods=['GET', 'POST'])
def liste_interactive():
    global contenu_liste_interactive
    nouvel_element = flask.request.form.get('element')

    if nouvel_element is not None:
        contenu_liste_interactive.append(nouvel_element)

    return flask.Response(flask.render_template(
        "liste_interactive.html.jinja2",
        auteur_liste="Prénom Nom",
        contenu_liste=contenu_liste_interactive
    ))


if __name__ == '__main__':
    app.run()
