import matplotlib.pyplot as plt
import numpy as np
import datetime

def separeidtitre(L):
    T=[]
    for i in range(len(L)):
        T.append([L[i][0],L[i][1]])
    return T

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
    plt.xticks(position, catégorie,fontsize=10)
    plt.xlabel('Catégories', fontsize=8)
    plt.title('Diagramme en bâtons - répartition des votes en fonction des catégories socioprofessionnelles',
    fontsize=12)
    plt.legend(loc=1)
    plt.show()

def catembert(p:list):   #p la liste du nombre de votes par catégorie
    explode=[]
    présence=[]
    for k in range (len(p)):
        if p[k]!=0:
            explode.append(0)
            présence.append(k)
    for t in range (len(présence)):
        if t not in présence:
            p.pop(t)
    catégories=[]
    for t in range (len(présence)):
        if présence[t]==0:
            catégories.append('Etudiant')
        if présence[t]==1:
            catégories.append('Retraité')
        if présence[t]==2:
            catégories.append('Agriculteurs exploitants')
        if présence[t]==3:
            catégories.append('Cadres et professions intellectuelles supérieures')
        if présence[t]==4:
            catégories.append('Artisans, commerçants, chefs d entreprise')
        if présence[t]==5:
            catégories.append('Professions intermédiaires')
        if présence[t]==6:
            catégories.append('Employés qualifiés')
        if présence[t]==7:
            catégories.append('Employés non qualifiés')
        if présence[t]==8:
            catégories.append('Ouvriers qualifiés')
        if présence[t]==9:
            catégories.append('Ouvriers non qualifiés')
    explode[max_indice(p)]=0.1
    explode=tuple(explode)
    plt.figure(figsize = (8, 8))
    plt.pie(p, explode=explode,labels = catégories,autopct='%1.1f%%')

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

def camemb_age(date:list):
    for k in range (len(date)):
        date[k]=calcul_age(date[k])
    age=7*[0]
    for t in range (len(date)):
        if date[t]>=18 and date[t]<=25:
            age[0]+=1
        if date[t]>=26 and date[t]<=35:
            age[1]+=1
        if date[t]>=36 and date[t]<=45:
            age[2]+=1
        if date[t]>=46 and date[t]<=55:
            age[3]+=1
        if date[t]>=56 and date[t]<=65:
            age[4]+=1
        if date[t]>=66 and date[t]<=75:
            age[5]+=1
        if date[t]>=76:
            age[6]+=1
    labels=[]
    age_présent=[]
    cat=['18-25 ans','26-35 ans','36-45 ans',
    '46-55 ans','56-65 ans','66-75 ans',
    '76 ans et plus']
    for j in range (len(age)):
        if age[j]!=0:
            labels.append(cat[j])
            age_présent.append(age[j])
    explode=len(labels)*[0]
    explode[max_indice(age_présent)]=0.1
    explode=tuple(explode)
    plt.figure(figsize = (8, 8))
    plt.pie(age_présent, explode=explode,labels = labels,autopct='%1.1f%%')

def parents(oui:list,non:list):
    for k in range (len(oui)):
        p=oui[k]
        oui[k]=(100*p)/(p+non[k])
        non[k]=(100*non[k])/(p+non[k])
    situation=['Parents','Pas parents']
    position=np.arange(len(situation))
    width=0.45
    plt.bar(position - width/2, oui, width, color='lightsteelblue')
    plt.bar(position + width/2, non, width, color='IndianRed')
    plt.xticks(position, situation,fontsize=10)
    plt.xlabel('Situation familiale', fontsize=8)
    plt.title('Diagramme en bâtons - répartition des votes en fonction de la situation familiale',
    fontsize=12)
    plt.legend(loc=1)
    plt.show()

def parembert(p:list):
    explode=2*[0]
    explode[max_indice(p)]=0.1
    plt.figure(figsize = (8, 8))
    plt.pie(p, explode=explode,labels = ['Parents','Pas Parents'] ,
    autopct='%1.1f%%')

def sexe(oui:list,non:list):
    for k in range (len(oui)):
        p=oui[k]
        oui[k]=(100*p)/(p+non[k])
        non[k]=(100*non[k])/(p+non[k])
    sexe=['Homme','Femme','Autres']
    position=np.arange(len(sexe))
    width=0.45
    plt.bar(position - width/2, oui, width, color='lightsteelblue')
    plt.bar(position + width/2, non, width, color='IndianRed')
    plt.xticks(position, sexe,fontsize=10)
    plt.xlabel('Sexe', fontsize=8)
    plt.title('Diagramme en bâtons - répartition des votes en fonction du sexe',
    fontsize=12)
    plt.legend(loc=1)
    plt.show()

def camembert_s(p:list):    #p la liste du nombre de votes par catégories
    explode=[]
    présence=[]
    for k in range (len(p)):
        if p[k]!=0:
            explode.append(0)
            présence.append(k)
    for t in range (len(présence)):
        if t not in présence:
            p.pop(t)
    sexe=[]
    for t in range (len(présence)):
        if présence[t]==0:
            sexe.append('Homme')
        if présence[t]==1:
            sexe.append('Femme')
        if présence[t]==2:
            sexe.append('Autres')
    explode[max_indice(p)]=0.1
    explode=tuple(explode)
    plt.figure(figsize = (8, 8))
    plt.pie(p, explode=explode,labels = sexe ,autopct='%1.1f%%')