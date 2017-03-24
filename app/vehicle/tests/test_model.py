from pytest import fixture
from vehicle.model import Vehicle


@fixture
def vectra():
    return Vehicle(
        doors=5,
        hp=450,
        sedan=True,
        name='Vectra 2016'
    )


@fixture
def ka():
    return Vehicle(
        doors=3,
        hp=250,
        name='Ford KA'
    )


def test_is_faster_when_car_is(vectra):
    assert vectra.is_faster() is True


def test_is_faster_when_car_isnt(ka):
    assert ka.is_faster() is False


def test_is_familiar_when_car_is(vectra):
    assert vectra.is_familiar() is True


def test_is_familiar_when_car_isnt(ka):
    assert ka.is_familiar() is False


def test_get_sell_name_is_correct(vectra):
    assert vectra.get_sell_name() == '[SELL] Vectra 2016 - 5 doors | 450 hp'
