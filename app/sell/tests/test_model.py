from pytest import fixture
from sell.model import Sell
from person.model import Person
from vehicle.model import Vehicle


@fixture
def sell():
    return Sell(price=1000, client=Person('Test', 0), vehicle=Vehicle())


def test_get_total_parcels_under_25(sell):
    assert sell.get_total_parcels() == 12


def test_get_total_parcels_under_35(sell):
    sell.client.age = 26
    assert sell.get_total_parcels() == 8


def test_get_total_parcels_over_35(sell):
    sell.client.age = 36
    assert sell.get_total_parcels() == 6


def test_get_parcel_price(sell, mocker):
    mocked_valid = mocker.patch.object(
        sell,
        'get_total_parcels',
        autospec=True,
    )

    mocked_valid.return_value = 2
    assert sell.get_parcel_price() == (1000/2)


def test_valid_sell_client_major(sell, mocker):
    mocked_valid = mocker.patch.object(
        sell.client,
        'is_major',
        autospec=True,
    )

    mocked_valid.return_value = True
    assert sell.valid_sell() is True


def test_valid_sell_client_no_major(sell, mocker):
    mocked_valid = mocker.patch.object(
        sell.client,
        'is_major',
        autospec=True,
    )

    mocked_valid.return_value = False
    assert sell.valid_sell() is False
