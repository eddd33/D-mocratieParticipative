import matplotlib.pyplot as plt
import numpy as np
import datetime

def pourcentage(o,n):
    t=o+n
    po=o*100/t
    pn=n*100/t
    return (round(po,1),round(pn,1))

def graphe_sociopro(oui:list,non:list):
    catégorie=['Etudiant','Retraité','Agriculteurs \n exploitants',
    'Cadres\n et \nprofessions\n intellectuelles\n supérieures',
    'Artisans,\n commerçants, \nchefs \nd entreprise',
    'Professions\n intermédiaires',
    'Employés\n qualifiés','Employés\n non\n qualifiés',
    'Ouvriers\n qualifiés','Ouvriers\n non\n qualifiés']
    for k in range (len(oui)):
        p=oui[k]
        oui[k]=(100*p)/(p+non[k])
        non[k]=(100*non[k])/(p+non[k])
    position=np.arange(1,101,10)
    width=0.45
    plt.bar(position - width/2, oui, width, color='lightsteelblue')
    plt.bar(position + width/2, non, width, color='IndianRed')
    plt.xticks(position, catégorie,fontsize=5)
    plt.xlabel('Catégories', fontsize=4)
    plt.title('Diagramme en bâtons - répartition des votes en fonction des catégories socioprofessionnelles',
    fontsize=12)
    plt.legend(loc=1)
    plt.show()

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

def calcul_age(date): #format JJ/MM/AAAA
    date=date.split('/')
    J=int(date[0])
    M=int(date[1])
    A=int(date[2])
    date=datetime.date(A,M,J)
    auj=datetime.date.today()
    return auj.year - date.year - ((auj.month, auj.day) < (date.month, date.day))

