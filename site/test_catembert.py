import ON as on

def test_catembert1():
    res=on.catembert([])
    assert res==None

   
def test_catembert2():
    res=on.catembert([0,0,0,0,0,0,0,0,0,0])
    assert res==None
    
test_catembert1()    
test_catembert2()
