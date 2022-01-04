import Traitement as t

def test_traitement_sexe_1():
    res = t.traitement_sexe([('Mme.','Oui',0),('Autre','Non',0),('Mme.','Non',0)])
    assert res == ([0,1,0],[0,1,1])


def test_traitement_sexe_2():
    res = t.traitement_sexe([('Mme','Oui',0),('Autre','Non',0),('Mme.','Non',0)])
    assert res == ([0,0,0],[0,1,1])


def test_traitement_sexe_3():
    res = t.traitement_sexe([('Mme.','Oui',0),('Autre','non',0),('Mme.','Non',0)])
    assert res == ([0,1,0],[0,1,0])

def test_traitement_sexe_4():
    res = t.traitement_sexe([])
    assert res == ([0,0,0],[0,0,0])