from os import memfd_create
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
import sqlite3
from ON import *
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
    
    partis=['Gauche démocrate et républicaine','La France insoumise','Socialistes et apparentés','Libertés et territoires','La République en marche','Mouvement démocrate et démocrates apparentés','Agir ensemble','UDI et indépendants','Les Républicains','Non-inscrits']
    departements=[i for i in range(1,96)]+[262,590,594,596,976]
    regions=['Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté','Bretagne','Centre-Val de Loire','Corse','Grand Est','Hauts-de-France','Île-de-France','Normandie','Nouvelle-Aquitaine','Occitanie','Pays de la Loire','Provence-Alpes-Côte d''Azur','Guadeloupe','Martinique','Guyane','La Réunion','Mayotte']
    return render_template('inscriptelu.html',regions=regions,departements=departements,partis=partis)


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
    cur.execute("SELECT * FROM elu")
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
    annee_naissance=request.form.get("date_naissance")
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

@app.route('/logincitdeux',methods=["GET","POST"])
def logincitdeux():
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    email=request.form.get("email")
    mdp=request.form.get("mdp")
    cur.execute("""SELECT mdp FROM utilisateur WHERE email='{}'""".format(email))
    mdptest=cur.fetchone()
    if not mdptest:
        return redirect('/logincit')
    mdpnormalement=mdptest[0]
    cur.execute("""SELECT nom FROM utilisateur WHERE email='{}'""".format(email))
    nom=cur.fetchone()[0]
    cur.execute("""SELECT prenom FROM utilisateur WHERE email='{}'""".format(email))
    prénom=cur.fetchone()[0]

    db.commit()
    db.close()
    if mdp==mdpnormalement:
        global nomut
        global prenomut
        global idut
        nomut=nom
        prenomut=prénom
        idut=0
        return redirect('/accueil_c/""')
    else:
        return redirect('/logincit')

@app.route('/accueil_c/<string:cat>',methods=["GET","POST"])
def accueil_c(cat=""):
    global nomut,prenomut,idut
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    print(cat)
    if cat=='""':
        print("rien")
        cur.execute("""SELECT ref_id,titre FROM referendum""")
        L=cur.fetchall()
        T=separeidtitre(L)
    else:
        print("catego")
        cur.execute("""SELECT ref_id,titre FROM referendum WHERE categorie1='{}' OR categorie2='{}'""".format(cat,cat))
        L=cur.fetchall()
        T=separeidtitre(L)


    db.commit()
    db.close()
    return render_template('accueil_c.html',nom=nomut,prénom=prenomut,liste=T)


@app.route('/loginelu')
def loginelu():
    return render_template('loginelu.html')


@app.route('/logineludeux',methods=["POST"])
def logineludeux():
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    email=request.form.get("email")
    mdp=request.form.get("mdp")
    print("Oskur",mdp)

    cur.execute("""SELECT mdp FROM elu WHERE email='{}'""".format(email))
    mdptest=cur.fetchone()
    if not mdptest:
        return redirect('/loginelu')
    mdpnormalement=mdptest[0]
    print(mdp,mdpnormalement)
    cur.execute("""SELECT nom FROM elu WHERE email='{}'""".format(email))
    nom=cur.fetchone()[0]
    cur.execute("""SELECT prenom FROM elu WHERE email='{}'""".format(email))
    prénom=cur.fetchone()[0]
    
    if mdp==mdpnormalement:
        global nomut
        global prenomut
        global idut
        nomut=nom
        prenomut=prénom
        cur.execute("""SELECT elu_id FROM elu WHERE email='{}' and mdp='{}'""".format(email,mdp))
        idut=cur.fetchone()[0]
        print(idut)
        db.commit()
        db.close()
        return redirect('/accueil_e/""')
        
    else:
        db.commit()
        db.close()
        return redirect('/loginelu')

@app.route('/accueil_e/<string:cat>',methods=["GET","POST"])
def accueil_e(cat=""):
    global nomut,prenomut,idut
    db=sqlite3.connect('projet.db')
    cur=db.cursor()


    if cat=='""':
        cur.execute("""SELECT ref_id,titre FROM referendum""")
        L=cur.fetchall()
        T=separeidtitre(L)
    else:
        cur.execute("""SELECT ref_id,titre FROM referendum WHERE categorie1='{}' OR categorie2='{}'""".format(cat,cat))
        L=cur.fetchall()
        T=separeidtitre(L)


    db.commit()
    db.close()
    return render_template('accueil_e.html',nom=nomut,prénom=prenomut,liste=T)





@app.route('/resultats/<int:ref>')
def resultats(ref):
    global prenomut,nomut,idut
    db=sqlite3.connect('projet.db')
    cur=db.cursor()

    cur.execute("""SELECT enonce,presentation,oui,non,debut,fin,createur FROM referendum WHERE ref_id={}""".format(ref))
    L=cur.fetchone()
    enonce,presentation,oui,non,debut,fin,createur=L[0],L[1],L[2],L[3],L[4],L[5],L[6]
    cur.execute("""SELECT nom,prenom FROM elu WHERE elu_id={}""".format(createur))
    T=cur.fetchone()
    nom,prenom=T[0],T[1]

    ouinon=pourcentage(oui,non)
    oui,non=ouinon[0],ouinon[1]

    db.commit()
    db.close()

    return render_template('resultats.html',e=enonce,pres=presentation,o=oui,n=non,d=debut,f=fin,nom=nom,pren=prenom)

@app.route('/creationreferendum')
def creationreferendum():
    global prenomut,nomut,idut
    departements=[i for i in range(1,96)]
    regions=['Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté','Bretagne','Centre-Val de Loire','Corse','Grand Est','Hauts-de-France','Île-de-France','Normandie','Nouvelle-Aquitaine','Occitanie','Pays de la Loire','Provence-Alpes-Côte d''Azur']
    if idut==0:
        return redirect('/accueil_c')
    else:
    
        return render_template('creationreferendum.html',regions=regions,departements=departements,nom=nomut,prénom=nomut)

@app.route('/refcree',methods=['POST'])
def refcree():
    global prenomut,idut,nomut
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    enonce=request.form.get("enonce")
    ville=request.form.get("ville")
    region=request.form.get("region")
    dep=int(request.form.get("dep"))
    debut=request.form.get("debut")
    fin=request.form.get("fin")
    cat1=request.form.get("cat1_ref")
    cat2=request.form.get("cat2_ref")
    titre=request.form.get("titre")
    presentation=request.form.get("resume")
    oui=0
    non=0
    cur.execute("INSERT INTO referendum (categorie1,categorie2,ville,dep,region,oui,non,enonce,presentation,debut,fin,createur,titre) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",(cat1,cat2,ville,dep,region,0,0,enonce,presentation,debut,fin,idut,titre))
    db.commit()
    db.close()
    return render_template('refcree.html')


@app.route('/referendum/<int:ref_id>')
def referendum(ref_id):
    global nomut,prenomut
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    cur.execute ("""SELECT enonce,presentation,debut,fin,createur,titre FROM referendum WHERE ref_id={}""".format(ref_id))
    L=cur.fetchone()
    print(L)
    enonce=L[0]
    presentation=L[1]
    debut=L[2]
    fin=L[3]
    createur=L[4]
    titre=L[5]
    cur.execute("""SELECT nom,prenom FROM elu WHERE elu_id={}""".format(createur) )
    T=cur.fetchone()
    nom,prenom=T[0],T[1]
    elu=[nom,prenom]
    db.commit()
    db.close()
    return render_template('referendum.html',enonce=enonce,presentation=presentation,debut=debut,fin=fin,createur=createur,titre=titre,elu=elu,nom=nomut,prénom=prenomut)

@app.route('/filtre',methods=["POST"])
def filtre():
    global idut
    catfiltre=request.form.get("categories")
    print(catfiltre)
    if idut==0:

        return redirect(f"/accueil_c/{catfiltre}")
    else:
        return redirect(f"/accueil_e/{catfiltre}")