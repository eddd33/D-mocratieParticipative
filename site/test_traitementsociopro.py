from Traitement import *

def test_traitementsociopro1():
    res=traitement_sociopro([])
    assert res==(10*[0],10*[0])

def test_traitementsociopro2():
    res=traitement_sociopro([('Etudiant','Non'),('Agriculteurs exploitants','Oui'),('Retraité','Oui')])
    assert res==([0,1,1,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,0,0])

def test_traitementsociopro3():
    res=traitement_sociopro([('Humoriste','Oui')])
    assert res==(10*[0],10*[0])

def test_traitementsociopro4():
    res=traitement_sociopro(['Etudiant','oui'])
    assert res==(10*[0],10*[0])