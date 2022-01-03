import ON as on
import datetime

date1 = datetime.date(1993,1,1)
date2 = datetime.date(2022,3,9)
date3 = datetime.date(2001,11,26)


def test_calcul_age_1():
    res = on.calcul_age(date1)
    assert res == 29

def test_calcul_age_2():
    res = on.calcul_age(date2)
    assert res == 0

def test_calcul_age_3():
    res = on.calcul_age(date3)
    assert res == 20


