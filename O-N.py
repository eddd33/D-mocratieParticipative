import matplotlib.pyplot as plt
import numpy as np

def pourcentage(o,n):
    t=o+n
    po=o*100/t
    pn=n*100/t
    return (round(po,1),round(pn,1))

def graphe_sociopro(oui:list,non:list):
    catégorie=['Etudiant','Retraité','Agriculteurs exploitants',
    'Cadres et professions intellectuelles supérieures',
    'Artisans, commerçants, chefs d entreprise',
    'Professions intermédiaires',
    'Employés qualifiés','Employés non qualifiés',
    'Ouvriers qualifiés','Ouvriers non qualifiés']
    for k in range (len(oui)):
        p=oui[k]
        oui[k]=(100*p)/(p+non[k])
        non[k]=(100*non[k])/(p+non[k])
    position = np.arange(len(catégorie))
    largeur = .25
    fig, ax = plt.subplots()
    r1 = ax.bar(position - largeur/2, oui, largeur)
    r2 = ax.bar(position + largeur/2, non, largeur,color='red')
    ax.set_xticks(position)
    ax.set_xticklabels(catégorie)

def camembert(p:list):   #p la liste du nombre de votes par catégorie
    explode=[0,0,0,0,0,0,0,0,0,0]
    explode[max_indice(p)]=0.1
    explode=tuple(explode)
    plt.figure(figsize = (8, 8))
    plt.pie(p, explode=explode,labels = ['Etudiant','Retraité','Agriculteurs exploitants',
    'Cadres et professions intellectuelles supérieures',
    'Artisans, commerçants, chefs d entreprise',
    'Professions intermédiaires',
    'Employés qualifiés','Employés non qualifiés',
    'Ouvriers qualifiés','Ouvriers non qualifiés'],autopct='%1.1f%%')

def max_indice(p:list):
    i=0
    M=p[0]
    for k in range (1,len(p)):
        if p[k]>M:
            M=p[k]
            i=k
    return i