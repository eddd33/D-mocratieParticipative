import Traitement as t

def test_traitement_parembert_1():
    res = t.traitement_parembert(['Parents','Pas parents','Pas parents','Pas parents'])
    assert res == [1,3]

def test_traitement_parembert_2():
    res = t.traitement_parembert(['Parents','pas parents','Pas parents','Pas parents'])
    assert res == [1,2]

def test_traitement_parembert_3():
    res = t.traitement_parembert([])
    assert res == [0,0]