import ON as on


def test_pourcentage_1():
    res = on.pourcentage(0,0)
    assert res == (0,0)

def test_pourcentage_2():
    res = on.pourcentage(1,4)
    assert res == (20.0,80.0)

def test_pourcentage_3():
    res = on.pourcentage(1,1)
    assert res == (50.0,50.0)

def test_pourcentage_4():
    res = on.pourcentage(1,None)
    assert res == (0,0)




