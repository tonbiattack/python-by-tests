class ProductCode:
    def __init__(self, code: str) -> None:
        self.code = code

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ProductCode) and self.code == other.code
