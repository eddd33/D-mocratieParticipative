from Traitement import *

def test_catembert1():
    res=traitement_catembert([('Etudiant',),('Etudiant',),('Retraité',)])
    assert res == [2,1,0,0,0,0,0,0,0,0]
def test_catembert2():
    res=traitement_catembert([])
    assert res == [0,0,0,0,0,0,0,0,0,0]
def test_catembert3():
    res=traitement_catembert([('Etudiant',),('Etudiant',),('Humoriste',)])
    assert res == [2,0,0,0,0,0,0,0,0,0]
