from Traitement import *

def test_parents1():
    res=traitement_parents([])
    assert res == ([0,0],[0,0])
def test_parents2():
    res=traitement_parents([('Parents','Oui'),('Parents','Non'),('Pas parents','Oui')])
    assert res == ([1,1],[1,0])    
def test_parents3():
    res=traitement_parents([('Parents','oui'),('Parents','Non'),('Pas parents','Oui')])
    assert res == ([0,1],[1,0])    
def test_parents4():
    res=traitement_parents([('parents','Oui'),('Parents','Non'),('Pas parents','Oui')])
    assert res == ([0,1],[1,0])    

    

