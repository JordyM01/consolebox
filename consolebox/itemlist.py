from .item import Item

class ItemList(object):
    _quantity = 0
    _cont = 0

    def __init__(self, items):
        self._list: list[Item] = []
        for i in items:
            self._list.append(
                Item(items[i],i)
            )
            self._quantity += 1

    def setposition(self, length, columns, start = 1, alignment = 1) -> None:
        # Point from which to start printing
        items = self._quantity
        half_size = int(items / columns)
        half_length = int(length / columns)

        x = alignment + 1  # We start from the alignment # regulates the printing on the x-axis representing the column
        z = 0
        colum = columns
        w = 0

        for _ in range(0, columns):
            cont = start
            z = int(items / colum)
            for _ in range(0, z):
                posit = (x, cont + 1)
                self._list[w]._setposition(posit)
                cont += 1
                w += 1
            items -= z
            colum -= 1
            x += half_length
            z = half_size + 1

    def List(self, index) -> Item:
        return self._list[index]

    def __iter__(self):
        return self

    def __next__(self) -> Item:
        self._cont += 1
        if self._cont > self._quantity:
            self._cont = 0
            raise StopIteration()
        return self._list[self._cont - 1]

    def __str__(self):
        _string = ''
        cont = 0
        for item in self._list:
            cont += 1
            _string = _string + item.name
            if cont < len(self._list):
                _string += '\n'
        return _string

    def __len__(self):
        return self._quantity

    def __repr__(self):
        return repr(self)

    def __getitem__(self, index):
        if isinstance(index, (int, slice)):
            return self._list[index]
        return [self._list[i] for i in index]

