class TrackedResource:
    def __init__(self, events: list[str]) -> None:
        self.events = events

    def __enter__(self) -> "TrackedResource":
        self.events.append("enter")
        return self

    def __exit__(self, exc_type: object, exc: object, traceback: object) -> bool:
        self.events.append("exit")
        return False
