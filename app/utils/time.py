from datetime import datetime, timezone


def now(utc: bool = True):
    return datetime.now(timezone.utc if utc else None)
