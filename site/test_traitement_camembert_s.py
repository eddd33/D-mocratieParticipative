import Traitement as t

def test_traitement_camembert_s_1():
    res = t.traitement_camembert_s([('Mme.',0,0),('Autre',0,0),('Mme.',0,0)])
    assert res == [0,2,1]

def test_traitement_camembert_s_2():
    res = t.traitement_camembert_s([('Mme.',0,0),('Autre',0,0),('Mme',0,0)])
    assert res == [0,1,1]

def test_traitement_camembert_s_3():
    res = t.traitement_camembert_s([])
    assert res == [0,0,0]
