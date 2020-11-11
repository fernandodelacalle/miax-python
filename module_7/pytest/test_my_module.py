import my_module


def test_suma():
    assert 2 == my_module.suma(1, 1)
    assert 4 == my_module.suma(2, 2)
    
def test_resta():
    assert 2 == my_module.resta(4, 2)
    assert 0 == my_module.resta(2, 2)