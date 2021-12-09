from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
import sqlite3
app=Flask(__name__)


@app.route('/')
def initial():
    return redirect("/login")
@app.route('/login')
def login():
    return render_template('login.html')
@app.route('/citoyen')
def citoyen():
    return render_template('citoyen.html',methods=["POST","GET"])
@app.route('/elu')
def elu():
    return render_template('elu.html')
@app.route('/accueil_c')
def accueil_c():
    return render_template('accueil_c.html')
@app.route('/accueil_e')
def accueil_e():
    return render_template('accueil_e.html')
@app.route('/reponse')
def reponse():
    return render_template('login.html',methods=["POST","GET"])

@app.route('/inscriptcit')
def inscriptcit():
    categories=['Etudiant','Retraité','Agriculteurs exploitants','Cadres et professions intellectuelles supérieures','Artisans, commerçants, chefs d entreprise','Professions intermédiaires','Employés qualifiés','Employés non qualifiés','Ouvriers qualifiés','Ouvriers non qualifiés']
    sexes=['M.','Mme.','Autre']
    departements=[i for i in range(1,96)]+[262,590,594,596,976]
    regions=['Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté','Bretagne','Centre-Val de Loire','Corse','Grand Est','Hauts-de-France','Île-de-France','Normandie','Nouvelle-Aquitaine','Occitanie','Pays de la Loire','Provence-Alpes-Côte d''Azur','Guadeloupe','Martinique','Guyane','La Réunion','Mayotte']
    return render_template('inscriptcit.html',categories=categories,sexes=sexes,departements=departements,regions=regions)

@app.route('/inscriptelu')
def inscriptelu():
    
    departements=[i for i in range(1,96)]+[262,590,594,596,976]
    regions=['Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté','Bretagne','Centre-Val de Loire','Corse','Grand Est','Hauts-de-France','Île-de-France','Normandie','Nouvelle-Aquitaine','Occitanie','Pays de la Loire','Provence-Alpes-Côte d''Azur','Guadeloupe','Martinique','Guyane','La Réunion','Mayotte']
    return render_template('inscriptelu.html',regions=regions,departements=departements)

@app.route('/registere',methods=["POST"])
def registere():
    departements=[i for i in range(1,96)]
    regions=['Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté','Bretagne','Centre-Val de Loire','Corse','Grand Est','Hauts-de-France','Île-de-France','Normandie','Nouvelle-Aquitaine','Occitanie','Pays de la Loire','Provence-Alpes-Côte d''Azur']
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    nom=request.form.get("nom")
    prenom=request.form.get("prenom")
    email=request.form.get("email")
    mdp=request.form.get("mdp")
    ville=request.form.get("ville")
    region=request.form.get("region")
    dep=int(request.form.get("dep"))
    role=request.form.get("role")
    parti=request.form.get("parti")
    if not nom:
        return render_template("error.html",message="Nom non renseigné")
    if not prenom:
        return render_template("error.html",message="Prénom non renseigné")
    if not ville:
        return render_template("error.html",message="Ville non renseignée")
    if not role:
        return render_template("error.html",message="Rôle non renseigné")
    if not parti:
        return render_template("error.html",message="Parti non renseigné")
    if not dep:
        return render_template("error.html",message="Département non renseigné")
    if dep not in departements:
        return render_template("error.html",message="Département non existant")
    if not region:
        return render_template("error.html",message="Région non renseigné")
    if region not in regions:
        return render_template("error.html",message="Région non existante")
    if not email:
        return render_template("error.html",message="Adresse email non renseignée")
    if not mdp:
        return render_template("error.html",message="Mot de passe non renseigné")
    cur.execute("INSERT INTO elu (nom,prenom,role,parti,ville,dep,region,email,mdp) VALUES (?,?,?,?,?,?,?,?,?)",(nom,prenom,role,parti,ville,dep,region,email,mdp))
    cur.execute("SELECT * FROM utilisateur")
    db.commit()
    db.close()
    return render_template('registere.html')

@app.route('/registerc',methods=["POST"])
def registerc():
    
    categories=['Etudiant','Retraité','Agriculteurs exploitants','Cadres et professions intellectuelles supérieures','Artisans, commerçants, chefs d entreprise','Professions intermédiaires','Employés qualifiés','Employés non qualifiés','Ouvriers qualifiés','Ouvriers non qualifiés']
    sexes=['M.','Mme.','Autre']
    departements=[i for i in range(1,96)]
    regions=['Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté','Bretagne','Centre-Val de Loire','Corse','Grand Est','Hauts-de-France','Île-de-France','Normandie','Nouvelle-Aquitaine','Occitanie','Pays de la Loire','Provence-Alpes-Côte d''Azur']
    
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    nom=request.form.get("nom")
    prenom=request.form.get("prenom")
    email=request.form.get("email")
    mdp=request.form.get("mdp")
    annee_naissance=request.form.get("annee_naissance")
    sexe=request.form.get("sexe")
    cat_soc_pro=request.form.get("cat_soc_pro")
    ville=request.form.get("ville")
    region=request.form.get("region")
    dep=int(request.form.get("dep"))
    print(dep)
    nb_enfants=request.form.get("nb_enfants")

    if not nom:
        return render_template("error.html",message="Nom non renseigné")
    if not prenom:
        return render_template("error.html",message="Prénom non renseigné")
    if not annee_naissance:
        return render_template("error.html",message="Année de naissance non renseignée")
    if not sexe:
        return render_template("error.html",message="Sexe non renseigné")
    if sexe not in sexes:
        return render_template("error.html",message="Sexe non existant")
    if not cat_soc_pro:
        return render_template("error.html",message="Catégorie socioprofessionelle non renseignée")
    if cat_soc_pro not in categories:
        return render_template("error.html",message="Catégorie socioprofessionelle non existante")
    if not ville:
        return render_template("error.html",message="Ville non renseignée")
    if not dep:
        return render_template("error.html",message="Département non renseigné")
    if dep not in departements:
        return render_template("error.html",message="Département non existant")
    if not region:
        return render_template("error.html",message="Région non renseigne")
    if region not in regions:
        return render_template("error.html",message="Région non existante")
    if not nb_enfants:
        return render_template("error.html",message="Nombre d'enfants non renseigné")
    if not email:
        return render_template("error.html",message="Adresse email non renseignée")
    if not mdp:
        return render_template("error.html",message="Mot de passe non renseigné")

    cur.execute("INSERT INTO utilisateur (nom,prenom,annee_naissance,sexe,cat_socio_pro,ville,dep,region,nb_enfants,email,mdp) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(nom,prenom,annee_naissance,sexe,cat_soc_pro,ville,dep,region,nb_enfants,email,mdp))
    cur.execute("SELECT * FROM utilisateur")
    db.commit()
    db.close()

    return render_template('registerc.html')
@app.route('/logincit')
def logincit():
    return render_template("logincit.html")
@app.route('/logincitdeux',methods=["POST"])
def logincitdeux():
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    email=request.form.get("email")
    mdp=request.form.get("mdp")
    

    cur.execute("""SELECT mdp FROM utilisateur WHERE email='{}'""".format(email))
    mdpnormalement=cur.fetchone()[0]
    db.commit()
    db.close()
    if mdp==mdpnormalement:
        return redirect('/accueil_c')
    else:
        return redirect('/logincit')

@app.route('/loginelu')
def loginelu():
    return render_template('loginelu.html')
@app.route('/logineludeux')
def logineludeux():
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    email=request.form.get("email")
    mdp=request.form.get("mdp")
    

    cur.execute("""SELECT mdp FROM elu WHERE email='{}'""".format(email))
    mdpnormalement=cur.fetchone()[0]
    db.commit()
    db.close()
    if mdp==mdpnormalement:
        return redirect('/accueil_e')
    else:
        return redirect('/loginelu')

    

    
    