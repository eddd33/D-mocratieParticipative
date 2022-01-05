from os import memfd_create, umask
from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
import sqlite3
from ON import *
from Traitement import *
import datetime

app=Flask(__name__)

departements=[str(i) for i in range(1,20)] + ['2A','2B'] + [str(i) for i in range(21,96)] + ['971','972','973','974','976']
regions=['Auvergne-Rhône-Alpes','Bourgogne-Franche-Comté','Bretagne','Centre-Val de Loire','Corse','Grand Est','Guadeloupe','Guyane','Hauts-de-France','Île-de-France','La Réunion','Martinique','Mayotte','Normandie','Nouvelle-Aquitaine','Occitanie','Pays de la Loire','Provence-Alpes-Côte d''Azur']
categories=['Etudiant','Retraité','Agriculteurs exploitants','Cadres et professions intellectuelles supérieures','Artisans, commerçants, chefs d entreprise','Professions intermédiaires','Employés qualifiés','Employés non qualifiés','Ouvriers qualifiés','Ouvriers non qualifiés']
sexes=['M.','Mme.','Autre']
partis=['Gauche démocrate et républicaine','La France insoumise','Socialistes et apparentés','Libertés et territoires','La République en marche','Mouvement démocrate et démocrates apparentés','Agir ensemble','UDI et indépendants','Les Républicains','Non-inscrits']
categorieref1=['education','ecologie','transport','tourisme','commerce','culture']
categorieref2=['education','ecologie','transport','tourisme','commerce','culture','null']


def testconnect():
    global nomut,prenomut,idut
    if 'idut' in globals() and 'prenomut' in globals() and 'nomut' in globals():
        return True
    else:
        print("redirect")
        return False

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


@app.route('/deconnect')
def deconnect():
    global prenomut,nomut,idut
    prenomut,nomut,idut=None,None,None
    return redirect('/login')


@app.route('/voteoui/<int:ref_id>')
def voteoui(ref_id):
    global prenomut,nomut,idut
    if not testconnect():
        return redirect('/login')
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    cur.execute("SELECT user_id FROM votes WHERE ref_id={}".format(ref_id))
    ids=cur.fetchall()
    print(ids)
    ids2=[]
    for K in ids:
        ids2.append(K[0])
    if idut!=0:
        return render_template('changercompte.html')
    if ids2==None or userid not in ids2:
        cur.execute("INSERT INTO votes  (ref_id,user_id,vote) VALUES (?,?,?)",(ref_id,userid,'Oui'))
        db.commit()
        db.close()
        return render_template('vousavezvoté.html')
    else:
        return render_template('dejavote.html')

@app.route('/votenon/<int:ref_id>')
def votenon(ref_id):
    global prenomut,nomut,idut
    if not testconnect():
        return redirect('/login')
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    cur.execute("SELECT user_id FROM votes WHERE ref_id={}".format(ref_id))
    ids=cur.fetchall()
    ids2=[]
    for K in ids:
        ids2.append(K[0])
    if idut!=0:
        return render_template('changercompte.html')
    if ids2==None or userid not in ids2:
        cur.execute("INSERT INTO votes (ref_id,user_id,vote) VALUES (?,?,?)",(ref_id,userid,'Non'))
        db.commit()
        db.close()
        return render_template('vousavezvoté.html')
    else:
        return render_template('dejavote.html')

@app.route('/inscriptcit')
def inscriptcit():
    return render_template('inscriptcit.html',categories=categories,sexes=sexes,departements=departements,regions=regions)

@app.route('/inscriptelu')
def inscriptelu():
    return render_template('inscriptelu.html',regions=regions,departements=departements,partis=partis)


@app.route('/registere',methods=["POST"])
def registere():
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    nom=request.form.get("nom")
    prenom=request.form.get("prenom")
    email=request.form.get("email")
    mdp=request.form.get("mdp")
    ville=request.form.get("ville")
    region=request.form.get("region")
    dep=request.form.get("dep")
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
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    nom=request.form.get("nom")
    prenom=request.form.get("prenom")
    email=request.form.get("email")
    mdp=request.form.get("mdp")
    date_naissance=request.form.get("date_naissance")
    sexe=request.form.get("sexe")
    cat_soc_pro=request.form.get("cat_soc_pro")
    ville=request.form.get("ville")
    region=request.form.get("region")
    dep=request.form.get("dep")
    parent=request.form.get("parent")

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

    cur.execute("INSERT INTO utilisateur (nom,prenom,date_naissance,sexe,cat_socio_pro,ville,dep,region,parent,email,mdp) VALUES (?,?,?,?,?,?,?,?,?,?,?)",(nom,prenom,date_naissance,sexe,cat_soc_pro,ville,dep,region,parent,email,mdp))
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
    cur.execute("""SELECT user_id FROM utilisateur WHERE email='{}'""".format(email))
    user=cur.fetchone()[0]
    db.commit()
    db.close()
    if mdp==mdpnormalement:
        global nomut
        global prenomut
        global idut
        global userid
        nomut=nom
        prenomut=prénom
        idut=0
        userid=user
        return redirect('/accueil_c/""')
    else:
        return redirect('/logincit')

@app.route('/accueil_c/<string:cat>',methods=["GET","POST"])
def accueil_c(cat=""):
    global nomut,prenomut,idut

    if not testconnect():
        return redirect('/login')

    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    print(cat)
    cur.execute("""SELECT ville,dep,region FROM utilisateur WHERE user_id={}""".format(userid))
    Y=cur.fetchone()
    ville,departement,region=Y[0],Y[1],Y[2]
    print(ville,departement,region)
    cur.execute("""SELECT ref_id,titre FROM referendum WHERE echelle="regionale" AND region='{}'""".format(region))
    refregion=cur.fetchall()
    REFregion=separeidtitre(refregion)
    cur.execute("""SELECT ref_id,titre FROM referendum WHERE echelle="departementale" AND dep='{}'""".format(departement))
    refdep=cur.fetchall()
    REFdep=separeidtitre(refdep)
    cur.execute("""SELECT ref_id,titre FROM referendum WHERE echelle="locale" AND ville='{}'""".format(ville))
    refville=cur.fetchall()
    REFville=separeidtitre(refville)
    
    if cat=='""' or cat=='None':
        print("rien")
        listetrie=REFregion+REFdep+REFville
    elif cat=='regionale':
        listetrie=REFregion
    elif cat=='departementale':
        listetrie=REFdep
    elif cat=='locale':
        listetrie=REFville 
    else:
        print("catego")
        listetrie=REFregion+REFdep+REFville
        cur.execute("""SELECT ref_id FROM referendum WHERE categorie1='{}' OR categorie2='{}'""".format(cat,cat))
        L=cur.fetchall()
        A=[]
        B=[]
        C=[]
        for K in listetrie:
            A.append(K[0])
        for J in L:
            B.append(J[0])
        for i in range(len(A)):
            if A[i] in B:
                C.append(listetrie[i])
        listetrie=C

    db.commit()
    db.close()
    return render_template('accueil_c.html',nom=nomut,prénom=prenomut,liste=listetrie)


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

    if not testconnect():
        return redirect('/login')

    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    cur.execute("""SELECT ville,dep,region FROM elu WHERE elu_id={}""".format(idut))
    Y=cur.fetchone()
    ville,departement,region=Y[0],Y[1],Y[2]
    print(ville,departement,region)
    cur.execute("""SELECT ref_id,titre FROM referendum WHERE echelle="regionale" AND region='{}'""".format(region))
    refregion=cur.fetchall()
    REFregion=separeidtitre(refregion)
    cur.execute("""SELECT ref_id,titre FROM referendum WHERE echelle="departementale" AND dep='{}'""".format(departement))
    refdep=cur.fetchall()
    REFdep=separeidtitre(refdep)
    cur.execute("""SELECT ref_id,titre FROM referendum WHERE echelle="locale" AND ville='{}'""".format(ville))
    refville=cur.fetchall()
    REFville=separeidtitre(refville)
    
    if cat=='""':
        print("rien")
        listetrie=REFregion+REFdep+REFville
    elif cat=='regionale':
        listetrie=REFregion
    elif cat=='departementale':
        listetrie=REFdep
    elif cat=='locale':
        listetrie=REFville 
    else:
        print("catego")
        listetrie=REFregion+REFdep+REFville
        cur.execute("""SELECT ref_id FROM referendum WHERE categorie1='{}' OR categorie2='{}'""".format(cat,cat))
        L=cur.fetchall()
        A=[]
        B=[]
        C=[]
        for K in listetrie:
            A.append(K[0])
        for J in L:
            B.append(J[0])
        for i in range(len(A)):
            if A[i] in B:
                C.append(listetrie[i])
        listetrie=C

    db.commit()
    db.close()
    return render_template('accueil_e.html',nom=nomut,prénom=prenomut,liste=listetrie)


@app.route('/resultatselu/<int:ref>')
def resultatselu(ref):
    global prenomut,nomut,idut
    if not testconnect():
        return redirect('/login')
    db=sqlite3.connect('projet.db')
    cur=db.cursor()

    cur.execute("""SELECT enonce,presentation,debut,fin,createur FROM referendum WHERE ref_id={}""".format(ref))
    L=cur.fetchone()
    enonce,presentation,debut,fin,createur=L[0],L[1],L[2],L[3],L[4]
    cur.execute("""SELECT COUNT(vote) FROM votes WHERE vote='Oui' AND ref_id={}""".format(ref))
    oui=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(vote) FROM votes WHERE vote='Non' AND ref_id={}""".format(ref))
    non=cur.fetchone()[0]
    cur.execute("""SELECT nom,prenom FROM elu WHERE elu_id={}""".format(createur))
    T=cur.fetchone()
    nom,prenom=T[0],T[1]

    ouinon=pourcentage(oui,non)
    oui,non=ouinon[0],ouinon[1]

    cur.execute("""SELECT cat_socio_pro,vote FROM utilisateur u JOIN votes v ON u.user_id=v.user_id WHERE ref_id={}""".format(ref))
    P=cur.fetchall()
    Ptuple=traitement_sociopro(P)
    graphe_sociopro(Ptuple[0],Ptuple[1])

    cur.execute("""SELECT cat_socio_pro FROM utilisateur u JOIN votes v ON u.user_id=v.user_id WHERE ref_id={}""".format(ref))
    H=cur.fetchall()
    catembert(traitement_catembert(H))

    cur.execute("""SELECT date_naissance,vote FROM utilisateur u JOIN votes v ON u.user_id=v.user_id WHERE ref_id={}""".format(ref))
    N=cur.fetchall()
    age(N)

    cur.execute("""SELECT date_naissance FROM utilisateur u JOIN votes v ON u.user_id=v.user_id WHERE ref_id={}""".format(ref))
    M=cur.fetchall()
    camemb_age(M)

    cur.execute("""SELECT parent,vote FROM utilisateur u JOIN votes v ON u.user_id=v.user_id WHERE ref_id={}""".format(ref))
    Y=cur.fetchall()
    Ytuple=traitement_parents(Y)
    print(Ytuple)
    parents(Ytuple[0],Ytuple[1])

    cur.execute("""SELECT parent,vote FROM utilisateur u JOIN votes v ON u.user_id=v.user_id WHERE ref_id={}""".format(ref))
    Z=cur.fetchall() #en minuscule parent ou pas (1ere position), en majuscule le vote (2eme postion)
    print(Z)
    parembert(traitement_parembert(Z))

    cur.execute("""SELECT sexe,vote FROM utilisateur u JOIN votes v ON u.user_id=v.user_id WHERE ref_id={}""".format(ref))
    U=cur.fetchall()
    Utuple=traitement_sexe(U)
    sexe(Utuple[0],Utuple[1])

    cur.execute("""SELECT sexe FROM utilisateur u JOIN votes v ON u.user_id=v.user_id WHERE ref_id={}""".format(ref))
    G=cur.fetchall()
    camembert_s(traitement_camembert_s(G))


    db.commit()
    db.close()

    return render_template('resultatselu.html',e=enonce,pres=presentation,o=oui,n=non,d=debut,f=fin,nom=nom,pren=prenom,nomut=nomut,prénomut=prenomut)

@app.route('/resultatscit/<int:ref>')
def resultatscit(ref):
    global prenomut,nomut,idut
    if not testconnect():
        return redirect('/login')
    db=sqlite3.connect('projet.db')
    cur=db.cursor()

    cur.execute("""SELECT enonce,presentation,debut,fin,createur FROM referendum WHERE ref_id={}""".format(ref))
    L=cur.fetchone()
    enonce,presentation,debut,fin,createur=L[0],L[1],L[2],L[3],L[4]
    cur.execute("""SELECT COUNT(vote) FROM votes WHERE vote='Oui' AND ref_id={}""".format(ref))
    oui=cur.fetchone()[0]
    cur.execute("""SELECT COUNT(vote) FROM votes WHERE vote='Non' AND ref_id={}""".format(ref))
    non=cur.fetchone()[0]
    cur.execute("""SELECT nom,prenom FROM elu WHERE elu_id={}""".format(createur))
    T=cur.fetchone()
    nom,prenom=T[0],T[1]

    ouinon=pourcentage(oui,non)
    oui,non=ouinon[0],ouinon[1]

    db.commit()
    db.close()

    return render_template('resultatscit.html',e=enonce,pres=presentation,o=oui,n=non,d=debut,f=fin,nom=nom,pren=prenom,nomut=nomut,prénomut=prenomut)

@app.route('/creationreferendum')
def creationreferendum():
    global prenomut,nomut,idut
    if not testconnect():
        return redirect('/login')
    if idut==0:
        print("non")
        return redirect('/accueil_c')
    else:
        print("oui")
        return render_template('creationreferendum.html',regions=regions,departements=departements,nom=nomut,prénom=prenomut)

@app.route('/refcree',methods=['POST'])
def refcree():
    global prenomut,idut,nomut
    if not testconnect():
        return redirect('/login')
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    enonce=request.form.get("enonce")
    ville=request.form.get("ville")
    region=request.form.get("region")
    dep=request.form.get("dep")
    print(dep, type(dep))
    debut=request.form.get("debut")
    fin=request.form.get("fin")
    cat1=request.form.get("cat1_ref")
    cat2=request.form.get("cat2_ref")
    titre=request.form.get("titre")
    presentation=request.form.get("resume")
    echelle=request.form.get("echelle")
    oui=0
    non=0
    if not titre:
        return render_template("error.html",message="Titre non renseigné")
    if not enonce:
        return render_template("error.html",message="Question non renseignée")
    if cat1 not in categorieref1:
        return render_template("error.html",message="Catégorie 1 non existante")
    if cat2 not in categorieref2:
        return render_template("error.html",message="Catégorie 2 non existante")
    if not presentation:
        return render_template("error.html",message="Résumé non renseignée")
    if not ville:    
        return render_template("error.html",message="Ville non renseigné")
    if not region:
        return render_template("error.html",message="Région non renseigne")
    if region not in regions:
        return render_template("error.html",message="Région non existante")
    if not dep:
        return render_template("error.html",message="Département non renseigné")
    if dep not in departements:
        return render_template("error.html",message="Département non existant")
    if not debut:
        return render_template("error.html",message="Date de début non renseignée")
    if not fin:
        return render_template("error.html",message="Date de fin non renseignée")


   

    cur.execute("INSERT INTO referendum (categorie1,categorie2,ville,dep,region,oui,non,enonce,presentation,debut,fin,createur,titre,echelle) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(cat1,cat2,ville,dep,region,0,0,enonce,presentation,debut,fin,idut,titre,echelle))
    db.commit()
    db.close()
    return render_template('refcree.html')


@app.route('/referendum/<int:ref_id>')
def referendum(ref_id):
    global nomut,prenomut
    if not testconnect():
        return redirect('/login')
    db=sqlite3.connect('projet.db')
    cur=db.cursor()
    cur.execute ("""SELECT enonce,presentation,debut,fin,createur,titre FROM referendum WHERE ref_id={}""".format(ref_id))
    L=cur.fetchone()
    enonce=L[0]
    presentation=L[1]
    debut=L[2]
    fin=L[3]
    createur=L[4]
    titre=L[5]

    now=str(datetime.datetime.now())[:11]
    if now>fin:
        if idut==0:
            return redirect('/resultatscit/{}'.format(ref_id))
        else:
            return redirect('/resultatselu/{}'.format(ref_id))


    cur.execute("""SELECT nom,prenom FROM elu WHERE elu_id={}""".format(createur) )
    T=cur.fetchone()
    nom,prenom=T[0],T[1]
    elu=[nom,prenom]
    db.commit()
    db.close()
    return render_template('referendum.html',enonce=enonce,presentation=presentation,debut=debut,fin=fin,createur=createur,titre=titre,elu=elu,nom=nomut,prénom=prenomut,ref_id=ref_id)

@app.route('/filtrecat',methods=["POST"])
def filtrecat():
    global idut
    if not testconnect():
        return redirect('/login')
    catfiltre=request.form.get("categories")
    
    if idut==0:

        return redirect(f"/accueil_c/{catfiltre}")
    else:
        return redirect(f"/accueil_e/{catfiltre}")
        
@app.route('/filtreech',methods=['POST'])
def filtreech():
    global idut
    if not testconnect():
        return redirect('/login')
    echfiltre=request.form.get("echelle")
    print(echfiltre)
    if idut==0:
        return redirect(f"/accueil_c/{echfiltre}")
        print("coucou")
    else:
        return redirect(f"/accueil_e/{echfiltre}")

@app.route('/apropos')
def apropos():
    return render_template('apropos.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/contactco')
def contactco():
    return render_template('contactco.html')

@app.route('/credits')
def credits():
    return render_template('credits.html') 

@app.route('/creditsco')
def creditsco():
    return render_template('creditsco.html') 