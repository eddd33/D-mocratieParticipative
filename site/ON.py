import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import datetime
import os
from typing import List

def separeidtitre(L:List[tuple]):     #Transforme une liste de tples de ongueur 2 en liste de liste de longueur 2
    T=[]
    for i in range(len(L)):
        if type(L[i])==tuple:
            T.append([L[i][0],L[i][1]])
    return T

def pourcentage(o:int,n:int):
    if o == None or n == None:
        return (0,0)
    elif o == 0 and n == 0 :
        return (0,0)
    t=o+n
    po=o*100/t   #On calcule le pourcentage de vote oui
    pn=n*100/t   #On calcule le pourcentage de vote non
    return (round(po,1),round(pn,1))

catégorie=['Etudiant','Retraité','Agriculteurs \n exploitants',
    'Cadres et professions \n intellectuelles supérieures',
    'Artisans, commerçants, \nchefs d entreprise',
    'Professions\n intermédiaires',
    'Employés\n qualifiés','Employés\n non qualifiés',
    'Ouvriers\n qualifiés','Ouvriers\n non qualifiés']

def graphe_sociopro(oui:List[int],non:List[int]):        #oui la liste dont le n-ième élément est le nombre d'individu votant oui pour la n-ième catégorie (idem pour non)
    if os.path.isfile('../site/static/sociopro.png'):    #Si un graphe est déjà enregistré
            os.remove('../site/static/sociopro.png')     #On le supprime pour pouvoir en créer un nouveau
    if len(oui)==len(non)==len(catégorie) and (oui!=[0]*10 or non!=[0]*10):  #On contrôle l'existance d'une valeurs pour chaque catégorie dans chacune des 2 listes et l'existance d'au moins 1 vote
        for k in range (len(oui)):
            p=oui[k]
            if p<0 or non[k]<0:
                return ('Valeur négative en entrée')
            if p+non[k]==0:
                pass
            else:
                oui[k]=(100*p)/(p+non[k])       #On remplace les nombres par les pourcentages qu'ils représentent au sein de la catégorie
                non[k]=(100*non[k])/(p+non[k])
        position=np.arange(len(catégorie))
        width=0.3
        fig=plt.figure(figsize = (8, 8))
        plt.bar(position - width/2, oui, width, color='lightsteelblue')  #On trace le poucentage de vote oui et non en fonction de la catégorie socio-professionnelle
        plt.bar(position + width/2, non, width, color='IndianRed')
        plt.xticks(position, catégorie,fontsize=10,rotation=90)
        plt.xlabel('Catégories', fontsize=8)
        plt.title('Diagramme en bâtons - répartition des votes en fonction des catégories socioprofessionnelles',fontsize=12)
        plt.legend(loc=1)
        fig.savefig('../site/static/sociopro.png',bbox_inches='tight')
    elif len(oui)==len(non)==len(catégorie) and oui==[0]*10 and non==[0]*10:   #Si aucun vote n'a été enregistré on enregistre un message d'information 
        img=mpimg.imread('pas_d_info.jpg')
        mpimg.imsave('../site/static/sociopro.png', img)
    else :
        print ('la longueur de la liste est incorrecte')
        
        
#on ne peut pas faire de camembert si l'une des valeurs de la liste est nulle, il faut donc enlever ces valeurs

def retire_zero(l:List[int]):  #Retire les zéros et les valeurs négatives d'une liste 
    compteur=l.count(0)        #On compte le nombre de zéro
    for k in range (compteur):
        l.remove(0)            #Puis on les retire
    i=len(l)
    while i!=0:                #On parcours la liste restante
        if l[i-1]<0:
            l.remove(l[i-1])   #Et on retire les valeurs négatives
        i=i-1
    return l



def catembert(p:List[int]):     #p la liste du nombre de votes par catégorie
    if len(p)==len(catégorie):  #On contrôle l'existence d'une valeurs pour chaque catégorie 
        explode=[]              #liste de même longueur que p mais faite de 0 sauf pour l'indice correspondant au max de p où l'on met 0.1
        présence=[]             #liste des indices des valeurs non nulles de p
        for k in range (len(p)):
            if p[k]!=0:
                explode.append(0) #on rajoute un 0 pour chaque valeur non nulle de p
                présence.append(k) #on ajoute dans la liste présence les indices de ces valeurs non nulles
        p=retire_zero(p)
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
        if os.path.isfile('../site/static/catembert.png'):    #Si un graphe est déjà enregistré
            os.remove('../site/static/catembert.png')         #On supprime l'ancien graphique
        if p!=[]:
            explode[max_indice(p)]=0.1
            explode=tuple(explode)
            fig=plt.figure(figsize = (8, 8))
            plt.pie(p, explode=explode,labels = catégories,autopct='%1.1f%%')
            fig.savefig('../site/static/catembert.png')
        else:
            img=mpimg.imread('pas_d_info.jpg')
            mpimg.imsave('../site/static/catembert.png', img)   #Si aucun vote n'a été enregistré on enregistre un message d'information 
    else:
        print ('la longueur de la liste est incorrecte')

def max_indice(p:List[int]):  
    if p == []:
        return None
    i=0
    M=p[0]
    for k in range (1,len(p)):
        if p[k]>M:
            M=p[k]
            i=k
    return i

def calcul_age(date): #format 'AAAA-MM-JJ'
    date=datetime.date(int(date[0:4]),int(date[5:7]),int(date[8:10]))
    auj=datetime.date.today()
    if str(datetime.datetime.now())[:11] < str(date) :
        return 0
    return auj.year - date.year - ((auj.month, auj.day) < (date.month, date.day))

def age(agevote:List[int]): #liste de tuples contenant la date de naissance du votant ainsi que son vote
    cat=['18-25 ans','26-35 ans','36-45 ans',
    '46-55 ans','56-65 ans','66-75 ans',
    '76 ans et plus']
    oui=7*[0]
    non=7*[0]
    for k in range (len(agevote)):
        age=calcul_age(agevote[k][0])
        vote=agevote[k][1]
        if age>=18 and age<=25:
            if vote=='Oui':
                oui[0]+=1
            else:
                non[0]+=1
        if age>=26 and age<=35:
            if vote=='Oui':
                oui[1]+=1
            else:
                non[1]+=1
        if age>=36 and age<=45:
            if vote=='Oui':
                oui[2]+=1
            else:
                non[2]+=1
        if age>=46 and age<=55:
            if vote=='Oui':
                oui[3]+=1
            else:
                non[3]+=1
        if age>=56 and age<=65:
            if vote=='Oui':
                oui[4]+=1
            else:
                non[4]+=1
        if age>=66 and age<=75:
            if vote=='Oui':
                oui[5]+=1
            else:
                non[5]+=1
        if age>=76:
            if vote=='Oui':
                oui[6]+=1
            else:
                non[6]+=1
    for t in range (len(oui)):
        p=oui[t]
        if p+non[t]==0:
            None
        else:
            oui[t]=(100*p)/(p+non[t])       #On remplace les nombres par les pourcentages qu'ils représentent au sein de la catégorie
            non[t]=(100*non[t])/(p+non[t])
    if os.path.isfile('../site/static/age.png'):     #Si un graphe est déjà enregistré
        os.remove('../site/static/age.png')          #On le supprime pour pouvoir en créer un nouveau
    if oui==[0]*7 and non==[0]*7 :
        img=mpimg.imread('pas_d_info.jpg')
        mpimg.imsave('../site/static/age.png',img)   #Si aucun vote n'a été enregistré on enregistre un message d'information 
    else:
        position=np.arange(len(cat))
        width=0.3
        fig=plt.figure(figsize = (8, 8))
        plt.bar(position - width/2, oui, width, color='lightsteelblue')  #On trace le poucentage de vote oui et non en fonction de la catégorie socio-professionnelle
        plt.bar(position + width/2, non, width, color='IndianRed')
        plt.xticks(position, cat,fontsize=10,rotation=45)
        plt.xlabel('Âge', fontsize=8)
        plt.title('Diagramme en bâtons - répartition des votes en fonction de l âge des votants',fontsize=12)
        plt.legend(loc=1)
        fig.savefig('../site/static/age.png',bbox_inches='tight')
    

def camemb_age(date:List[int]):
    for k in range (len(date)):
        date[k]=calcul_age(date[k][0])
    age=7*[0]                        #liste dont le n-ième élément est le nombre de personne dans la n-ième tranche d'age      
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
    if os.path.isfile('../site/static/camem_age.png'):    #Si un graphe est déjà enregistré
        os.remove('../site/static/camem_age.png')         #On le supprime pour pouvoir un créer un nouveau
    if age_présent!=[]:
        explode=len(labels)*[0]
        explode[max_indice(age_présent)]=0.1
        explode=tuple(explode)
        fig=plt.figure(figsize = (8, 8))
        plt.pie(age_présent, explode=explode,labels = labels,autopct='%1.1f%%')
        fig.savefig('../site/static/camem_age.png')
    else:
        img=mpimg.imread('pas_d_info.jpg')
        mpimg.imsave('../site/static/camem_age.png', img)   #Si aucun vote n'a été enregistré on enregistre un message d'information 
    
    
def parents(oui:List[int],non:List[int]): #oui la liste dont le n-ième élément est le nombre d'individu votant oui pour la n-ième catégorie (idem pour non)
    parent=['Parent','Pas parent']
    if os.path.isfile('../site/static/parents.png'):     #Si un graphe est déjà enregistré
       os.remove('../site/static/parents.png')           #On le supprime pour pouvoir en creer un nouveau
    if len(oui)==len(non)==2 and (oui!=[0]*2 or non!=[0]*2):  #On contrôle l'existence d'une valeurs pour chaque catégorie dans chacune des 2 listes
        for k in range (len(oui)):
            p=oui[k]
            if p<0 or non[k]<0:
                return ('Valeur négative en entrée')
            if p+non[k]==0:
                pass
            else:
                oui[k]=(100*p)/(p+non[k])
                non[k]=(100*non[k])/(p+non[k])
        position=np.arange(len(parent))
        width=0.3
        fig=plt.figure(figsize = (8, 8))
        plt.bar(position - width/2, oui, width, color='lightsteelblue') #On trace le poucentage de vote oui et non en fonction de la situation familiale
        plt.bar(position + width/2, non, width, color='IndianRed')
        plt.xticks(position, parent,fontsize=10)
        plt.xlabel('Situation familiale', fontsize=8)
        plt.title('Diagramme en bâtons - répartition des votes en fonction de la situation familiale', fontsize=12)
        plt.legend(loc=1)
        fig.savefig('../site/static/parents.png',bbox_inches='tight')
    elif oui==[0]*2 and non==[0]*2:
        img=mpimg.imread('pas_d_info.jpg')
        mpimg.imsave('../site/static/parents.png', img)     #Si aucun vote n'a été enregistré on enregistre un message d'information 
    else:
        print ('la longueur de la liste est incorrecte')

def parembert(p:List[int]):
    if len(p)==2:  #On contrôle l'existence d'une valeurs pour chaque catégorie 
        explode=[]
        présence=[]
        for k in range (len(p)):
            if p[k]>0:
                explode.append(0)
                présence.append(k)
        p=retire_zero(p)
        parent=[]
        for t in range (len(présence)):
            if présence[t]==0:
                parent.append('Parent')
            if présence[t]==1:
                parent.append('Pas parent')
        if os.path.isfile('../site/static/parembert.png'):   #Si un graphe est déjà enregistré
            os.remove('../site/static/parembert.png')        #On le supprime pour pouvoir en créer un nouveau
        if p!=[]:
            explode[max_indice(p)]=0.1
            fig=plt.figure(figsize = (8, 8))
            plt.pie(p, explode=explode,labels = parent ,autopct='%1.1f%%')
            fig.savefig('../site/static/parembert.png')
        else:
            img=mpimg.imread('pas_d_info.jpg')
            mpimg.imsave('../site/static/parembert.png', img)  #Si aucun vote n'a été enregistré on enregistre un message d'information 
    else:
        print ('la longueur de la liste est incorrecte')
        

def sexe(oui:List[int],non:List[int]):
    if os.path.isfile('../site/static/sexe.png'):    #Si un graphe est déjà enregistré
        os.remove('../site/static/sexe.png')         #On le supprime pour pouvoir en créer un nouveau
    if len(oui)==len(non)==3 and (oui!=[0]*3 or non!=[0]*3): #On contrôle l'existence d'une valeurs pour chaque catégorie dans chacune des 2 listes
        for k in range (len(oui)):
            p=oui[k]
            if p<0 or non[k]<0:
                return ('Valeur négative en entrée')
            if p+non[k]==0:
                pass
            else:
                oui[k]=(100*p)/(p+non[k])
                non[k]=(100*non[k])/(p+non[k])
        sexe=['Homme','Femme','Autres']
        position=np.arange(len(sexe))
        width=0.3
        fig=plt.figure(figsize=(8,8))
        plt.bar(position - width/2, oui, width, color='lightsteelblue')
        plt.bar(position + width/2, non, width, color='IndianRed')
        plt.xticks(position, sexe,fontsize=10)
        plt.xlabel('Sexe', fontsize=8)
        plt.title('Diagramme en bâtons - répartition des votes en fonction du sexe',fontsize=12)
        plt.legend(loc=1)
        fig.savefig('../site/static/sexe.png',bbox_inches='tight')
    elif len(oui)==len(non)==3 and oui==[0]*3 or non==[0]*3: 
        img=mpimg.imread('pas_d_info.jpg')
        mpimg.imsave('../site/static/sexe.png', img)     #Si aucun vote n'a été enregistré on enregistre un message d'information 
    else:
        print ('la longueur de la liste est incorrecte')

def camembert_s(p:List[int]):    #p la liste du nombre de votes par catégories
    if len(p)==3:                #On contrôle l'existence d'une valeurs pour chaque catégorie 
        explode=[]
        présence=[]
        for k in range (len(p)):
            if p[k]>0:
                explode.append(0)
                présence.append(k)
        p=retire_zero(p)
        sexe=[]
        for t in range (len(présence)):
            if présence[t]==0:
                sexe.append('Homme')
            if présence[t]==1:
                sexe.append('Femme')
            if présence[t]==2:
                sexe.append('Autres')
        if os.path.isfile('../site/static/camembert_s.png'):  #Si un graphe est déjà enregistré
            os.remove('../site/static/camembert_s.png')       #On le supprime pour pouvoir en créer un nouveau
        if p!=[]:
            explode[max_indice(p)]=0.1
            explode=tuple(explode)
            fig=plt.figure(figsize = (8, 8))
            plt.pie(p, explode=explode,labels = sexe ,autopct='%1.1f%%')
            fig.savefig('../site/static/camembert_s.png')
        else:
            img=mpimg.imread('pas_d_info.jpg')
            mpimg.imsave('../site/static/camembert_s.png', img)          #Si aucun vote n'a été enregistré on enregistre un message d'information 
    else:
        print ('la longueur de la liste est incorrecte')
        