import ON as on

L1 = [('id1', 'titre1',0,0),('id2', 'titre2','test',0),('id3', 'titre3',0,'sujet','lieu')]
L2 = [('id1', 'titre1',0,0),'id2',('id3', 'titre3',0,'sujet','lieu')]
L3 = []

def test_separeidtitre_1():
    res = on.separeidtitre(L1)
    assert res == [['id1','titre1'],['id2','titre2'],['id3','titre3']]

def test_separeidtitre_2():
    res = on.separeidtitre(L2)
    assert res == [['id1','titre1'],['id3','titre3']]

def test_separeidtitre_3():
    res = on.separeidtitre(L3)
    assert res == []