
class Item():
    _quantity: int = 0 # Number of items

    def __init__(self, name: str, index: int):
        self.name: str = name
        self.index: int = index
        self.marked = False
        self._position: tuple[int,int] = (1,1)
        self._quantity += 1

    def __len__(self) -> int:
        return len(self.name)

    def __str__(self) -> str:
        return self.name

    @property
    def getposition(self) -> tuple[int,int]:
        return self._position

    def _setposition(self, position: tuple[int,int]) -> None:
        self._position = position

    @property
    def getmarked(self) -> bool:
        return self.marked

    def _setmarked(self, marked: bool = True) -> None:
        self.marked = marked


