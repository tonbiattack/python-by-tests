from typing import Protocol, runtime_checkable


@runtime_checkable
class Renderable(Protocol):
    def render(self) -> str: ...


class Printer:
    def render(self) -> str:
        return "printed"
