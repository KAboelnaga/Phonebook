import pytest
from project import main, validate_name, validate_phone, validate_mail



def test_validate_name():
    assert validate_name("Kareem Aboelnaga") == "Kareem Aboelnaga"
    assert validate_name("Kareem") == "kareem"
    assert validate_name("Kareem ahmed Aboelnaga") == "Kareem ahmed Aboelnaga"
    with pytest.raises(ValueError):
        validate_name("kareem1234")
        validate_name("1234")
        validate_name("kareem@$%#")
        validate_name("kareem.aboelnaga")
        validate_name("kareem/aboelnaga")

def test_validate_phone():
    assert validate_phone("01019932727") == "01019932727"
    assert validate_phone("035484060") == "035484060"
    with pytest.raises(ValueError):
        validate_phone("yo5431")
        validate_phone("123yu")
        validate_phone("123@$%#")

def test_validate_email():
    assert validate_email("kareemaboelnaga18@gmail.com") == "kareemaboelnaga18@gmail.com"
    assert validate_email("ahaboelnaga@gmail.com") == "ahaboelnaga@gmail.com"
    with pytest.raises(ValueError):
        validate_email("cat/dog")
        validate_email("@asdf")
        validate_email("kareem@")
        validate_email("kareem.com")
        validate_email("kareem@gmail")