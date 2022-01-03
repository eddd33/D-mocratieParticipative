import ON as on

L1=[1,2,3,0,5,4,6]
L2=[0,0,0,0,0]
L3=[]
L4=[1,2,3]

def test_retire_zero_1():
    res = on.retire_zero(L1)
    assert res == [1,2,3,5,4,6]

def test_retire_zero_2():
    res = on.retire_zero(L2)
    assert res == []

def test_retire_zero_3():
    res = on.retire_zero(L3)
    assert res == []

def test_retire_zero_4():
    res = on.retire_zero(L4)
    assert res == [1,2,3]
    


