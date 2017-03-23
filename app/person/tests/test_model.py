from person.model import Person


def test_is_major_with_over_18_age():
    p = Person("charles", 25)
    assert p.is_major() is True


def test_is_major_with_under_18_age():
    p = Person("michael", 16)
    assert p.is_major() is False


def test_is_major_with_age_equal_18():
    p = Person("guilherme", 18)
    assert p.is_major() is True


def test_is_major_with_age_equal_None():
    p = Person("guilherme", None)
    assert p.is_major() is False
