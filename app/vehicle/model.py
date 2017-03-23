class Vehicle():
    def __init__(self, wheels=4, doors=3, sedan=False, *args, **kwargs):
        self.wheels = wheels
        self.doors = doors
        self.sedan = sedan
        self.hp = kwargs.get('hp')
        self.name = kwargs.get('name')

    def is_familiar(self):
        if self.doors > 3 and self.sedan:
            return True

        return False

    def is_faster(self):
        return True if self.hp > 400 else False

    def get_sell_name(self):
        return '[SELL] {} - {} doors | {} hp'.format(
            self.name, self.doors, self.hp,
        )
