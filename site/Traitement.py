from ON import *

def traitement_sociopro(P):
        
    yes=10*[0]
    no=10*[0]
    for k in range (len(P)):
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

def traitement_catembert(H):
    p=10*[0]
    for k in range (len(H)):
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

def traitement_parents(Y):
    oui=2*[0]
    non=2*[0]
    for k in range (len(Y)):
        
        if Y[k][1]=='Oui':
            if Y[k][0]=='Parents':
                oui[0]+=1
            if Y[k][0]=='Pas parents':
                oui[1]+=1
        if Y[k][1]=='Non':
            if Y[k][0]=='Parents':
                non[0]+=1
            if Y[k][0]=='Pas parents':
                non[1]+=1
    return oui,non

def traitement_parembert(Z):
    p=2*[0]
    for k in range (len(Z)):
        if Z[k]=='Parents':
            p[0]+=1
        if Z[k]=='Pas parents':
            p[1]+=1
    return p

def traitement_sexe(U):
    oui=3*[0]
    non=3*[0]
    for k in range (len(U)):
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

def traitement_camembert_s(G):
    p=3*[0]
    for k in range (len(G)):
        if G[k][0]=='M.':
            p[0]+=1
        if G[k][0]=='Mme.':
            p[1]+=1
        if G[k][0]=='Autre':
            p[2]+=1
    return p