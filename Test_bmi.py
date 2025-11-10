from Lab_2 import bmi

def test_bmi_normal_weight():
    result1 = bmi.calculate_bmi(1.8,50)
    assert(result1 == -1)


def test_bmi_over_weight():
    result2 = bmi.calculate_bmi(1.75,70)
    assert(result2 == 0)


def test_bmi_under_weight():
    result3 = bmi.calculate_bmi(1.6,80)
    assert(result3 == 1)