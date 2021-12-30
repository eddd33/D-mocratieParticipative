def traitement_sociopro(P):
    yes=10*[0]
    no=10*[0]
    for k in range (0,len(P),2):
        if P[k+1]=='Oui':
            if P[k]=='Etudiant':
                yes[0]+=1
            if P[k]=='Retraité':
                yes[1]+=1
            if P[k]=='Agriculteurs exploitants':
                yes[2]+=1
            if P[k]=='Cadres et professions intellectuelles supérieures':
                yes[3]+=1
            if P[k]=='Artisans, commerçants, chefs d entreprise':
                yes[4]+=1
            if P[k]=='Professions intermédiaires':
                yes[5]+=1
            if P[k]=='Employés qualifiés':
                yes[6]+=1
            if P[k]=='Employés non qualifiés':
                yes[7]+=1
            if P[k]=='Ouvriers qualifiés':
                yes[8]+=1
            if P[k]=='Ouvriers non qualifiés':
                yes[9]+=1
        if P[k+1]=='Non':
            if P[k]=='Etudiant':
                no[0]+=1
            if P[k]=='Retraité':
                no[1]+=1
            if P[k]=='Agriculteurs exploitants':
                no[2]+=1
            if P[k]=='Cadres et professions intellectuelles supérieures':
                no[3]+=1
            if P[k]=='Artisans, commerçants, chefs d entreprise':
                no[4]+=1
            if P[k]=='Professions intermédiaires':
                no[5]+=1
            if P[k]=='Employés qualifiés':
                no[6]+=1
            if P[k]=='Employés non qualifiés':
                no[7]+=1
            if P[k]=='Ouvriers qualifiés':
                no[8]+=1
            if P[k]=='Ouvriers non qualifiés':
                no[9]+=1
    return yes,no

def traitement_catembert(H):
    p=10*[0]
    for k in range (len(H)):
        if H[k]=='Etudiant':
            p[0]+=1
        if H[k]=='Retraité':
            p[1]+=1
        if H[k]=='Agriculteurs exploitants':
            p[2]+=1
        if H[k]=='Cadres et professions intellectuelles supérieures':
            p[3]+=1
        if H[k]=='Artisans, commerçants, chefs d entreprise':
            p[4]+=1
        if H[k]=='Professions intermédiaires':
            p[5]+=1
        if H[k]=='Employés qualifiés':
            p[6]+=1
        if H[k]=='Employés non qualifiés':
            p[7]+=1
        if H[k]=='Ouvriers qualifiés':
            p[8]+=1
        if H[k]=='Ouvriers non qualifiés':
            p[9]+=1
    return p

#def traitement_age(N:list):

#def traitement_camemb_age(M:list):

def traitement_sexe(U):
    oui=3*[0]
    non=3*[0]
    for k in range (0,len(U),2):
        if U[k+1]=='Oui':
            if U[k]=='M.':
                oui[0]+=1
            if U[k]=='Mme.':
                oui[1]+=1
            if U[k]=='Autre':
                oui[2]+=1
        if U[k+1]=='Non':
            if U[k]=='M.':
                non[0]+=1
            if U[k]=='Mme.':
                non[1]+=1
            if U[k]=='Autre':
                non[2]+=1
    return oui,non

def traitement_camembert_s(G):
    p=3*[0]
    for k in range (len(G)):
        if G[k]=='M.':
            p[0]+=1
        if G[k]=='Mme.':
            p[1]+=1
        if G[k]=='Autre':
            p[2]+=1
    return p