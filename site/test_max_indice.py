import ON as on

L1=[1,2,3,0,5,4]
L2=[0,0,0,0,0]
L3=[]
L4=[1,2,3,3]

def test_max_indice_1():
    res = on.max_indice(L1)
    assert res == 4

def test_max_indice_2():
    res = on.max_indice(L2)
    assert res == 0
    
def test_max_indice_3():
    res = on.max_indice(L3)
    assert res == None

def test_max_indice_4():
    res = on.max_indice(L4)
    assert res == 2