class Sell():
    def __init__(self, *arg, **kwarg):
        self.client = kwarg.get('client')
        self.vehicle = kwarg.get('vehicle')
        self.price = kwarg.get('price')

    def valid_sell(self):
        if self.client.is_major() and self.price > 0:
            return True

        return False

    def get_total_parcels(self):
        if self.client.age < 25:
            return 12
        elif self.client.age < 35:
            return 8

        return 6

    def get_parcel_price(self):
        parcels = self.get_total_parcels()
        return self.price / parcels
