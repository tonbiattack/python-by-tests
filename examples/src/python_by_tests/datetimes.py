from datetime import UTC, datetime


def utc_at(hour: int) -> datetime:
    return datetime(2026, 1, 1, hour, tzinfo=UTC)


def naive_at(hour: int) -> datetime:
    return datetime(2026, 1, 1, hour)
