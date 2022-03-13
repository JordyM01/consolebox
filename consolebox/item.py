
class Item():
    quantity = 0 # Number of items

    def __init__(self, name , index):
        self.name = name
        self.index = index
        self._position = (1,1)
        self.quantity += 1

    def __len__(self):
        return len(self.name)

    def __str__(self):
        return self.name

    @property
    def getposition(self):
        return self._position

    def _setposition(self, position):
        self._position = position


