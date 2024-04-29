import bmi 

def test_bmi_normal_weight():
    assert(bmi.calculate_bmi(1.65,55)==0)


def test_bmi_over_weight():
    assert(bmi.calculate_bmi(1.65,85)==1)


def test_bmi_under_weight():
    assert(bmi.calculate_bmi(1.65,30)==-1)