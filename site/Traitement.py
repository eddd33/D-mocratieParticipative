from ON import *

#les algorithhmes ci-dessous permettent de transformer les résultats de requêtes SQL en listes utilisable pour l'affichage des données par nos algorithmes

def traitement_sociopro(P):     # P est une liste de tuples dont le premier élément est la catégorie socio-professionnelle et dont le second élément est le vote
    yes=10*[0]                  #On crée 2 listes de longueur le nombre de catégories, dont le n-ième élément sera le nombre de votes (respectivement "Oui" et "Non") pour la n-ième catégorie
    no=10*[0]
    for k in range (len(P)):    #On remplit les listes en lisant le vote et la catégorie récoltés pour chaque votant
        if P[k][1]=='Oui':
            if P[k][0]=='Etudiant':
                yes[0]+=1
            if P[k][0]=='Retraité':
                yes[1]+=1
            if P[k][0]=='Agriculteurs exploitants':
                yes[2]+=1
            if P[k][0]=='Cadres et professions intellectuelles supérieures':
                yes[3]+=1
            if P[k][0]=='Artisans, commerçants, chefs d entreprise':
                yes[4]+=1
            if P[k][0]=='Professions intermédiaires':
                yes[5]+=1
            if P[k][0]=='Employés qualifiés':
                yes[6]+=1
            if P[k][0]=='Employés non qualifiés':
                yes[7]+=1
            if P[k][0]=='Ouvriers qualifiés':
                yes[8]+=1
            if P[k][0]=='Ouvriers non qualifiés':
                yes[9]+=1
        if P[k][1]=='Non':
            if P[k][0]=='Etudiant':
                no[0]+=1
            if P[k][0]=='Retraité':
                no[1]+=1
            if P[k][0]=='Agriculteurs exploitants':
                no[2]+=1
            if P[k][0]=='Cadres et professions intellectuelles supérieures':
                no[3]+=1
            if P[k][0]=='Artisans, commerçants, chefs d entreprise':
                no[4]+=1
            if P[k][0]=='Professions intermédiaires':
                no[5]+=1
            if P[k][0]=='Employés qualifiés':
                no[6]+=1
            if P[k][0]=='Employés non qualifiés':
                no[7]+=1
            if P[k][0]=='Ouvriers qualifiés':
                no[8]+=1
            if P[k][0]=='Ouvriers non qualifiés':
                no[9]+=1
    return yes,no

def traitement_catembert(H):  #H est la liste des catégories socio-professionnelles des votants
    p=10*[0]                  #On crée une liste de longueur le nombre de catégories, dont le n-ième élément sera le nombre de votes pour la n-ième catégorie
    for k in range (len(H)):  #On remplit la liste en lisant la catégorie récoltée pour chaque votant
        if H[k][0]=='Etudiant':
            p[0]+=1
        if H[k][0]=='Retraité':
            p[1]+=1
        if H[k][0]=='Agriculteurs exploitants':
            p[2]+=1
        if H[k][0]=='Cadres et professions intellectuelles supérieures':
            p[3]+=1
        if H[k][0]=='Artisans, commerçants, chefs d entreprise':
            p[4]+=1
        if H[k][0]=='Professions intermédiaires':
            p[5]+=1
        if H[k][0]=='Employés qualifiés':
            p[6]+=1
        if H[k][0]=='Employés non qualifiés':
            p[7]+=1
        if H[k][0]=='Ouvriers qualifiés':
            p[8]+=1
        if H[k][0]=='Ouvriers non qualifiés':
            p[9]+=1
    return p

def traitement_parents(Y):    #Y est une liste de tuples dont le premier élément est la réponse à la question "Êtes vous parent?" et dont le second élément est le vote
    oui=2*[0]                 #On crée 2 listes de longueur le nombre de catégories, dont le n-ième élément sera le nombre de votes (respectivement "Oui" et "Non") pour la n-ième situation
    non=2*[0]
    for k in range (len(Y)):  #On remplit les listes en lisant le vote et la situation familiale récoltés pour chaque votant
        if Y[k][1]=='Oui':    
            if Y[k][0]=='oui':   #Si la réponse à "Êtes vous parent?" est "oui" 
                oui[0]+=1        #On ajoute un vote dans la liste oui en position 0
            if Y[k][0]=='non':
                oui[1]+=1
        if Y[k][1]=='Non':
            if Y[k][0]=='oui':
                non[0]+=1
            if Y[k][0]=='non':
                non[1]+=1
    return oui,non

def traitement_parembert(Z):  #Z est la liste des situations familiales des votants
    p=2*[0]                   #On crée une liste de longueur le nombre de situations, dont le n-ième élément sera la nombre de votes pour la n-ième situation
    for k in range (len(Z)):  #On remplit la liste en lisant la situation récoltée pour chaque votant
        if Z[k][0]=='oui':
            p[0]+=1
        if Z[k][0]=='non':
            p[1]+=1
    return p

def traitement_sexe(U):        #Y est une liste de tuples dont le premier élément est le sexe et dont le second élément est le vote
    oui=3*[0]                  #On crée 2 listes de longueur le nombre de sexes, dont le n-ième élément sera le nombre de votes (respectivement "Oui" et "Non") pour le n-ième sexe
    non=3*[0]
    for k in range (len(U)):    #On remplit les listes en lisant le vote et le sexe récoltés pour chaque votant
        if U[k][1]=='Oui':
            if U[k][0]=='M.':
                oui[0]+=1
            if U[k][0]=='Mme.':
                oui[1]+=1
            if U[k][0]=='Autre':
                oui[2]+=1
        if U[k][1]=='Non':
            if U[k][0]=='M.':
                non[0]+=1
            if U[k][0]=='Mme.':
                non[1]+=1
            if U[k][0]=='Autre':
                non[2]+=1
    return oui,non

def traitement_camembert_s(G):   #G est la liste des sexes des votants
    p=3*[0]                      #On crée une liste de longueur le nombre de sexes, dont le n-ième élément sera la nombre de votes pour le n-ième sexe
    for k in range (len(G)):     #On remplit la liste en lisant le sexe récolté pour chaque votant
        if G[k][0]=='M.':
            p[0]+=1
        if G[k][0]=='Mme.':
            p[1]+=1
        if G[k][0]=='Autre':
            p[2]+=1
    return p