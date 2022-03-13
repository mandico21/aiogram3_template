from tgbot.config import DB


def make_connection_string(db: DB, async_fallback: bool = False) -> str:
    result = (
        f"postgresql+asyncpg://{db.user}:{db.password}@{db.host}:{db.port}/{db.name}"
    )
    if async_fallback:
        result += "?async_fallback=True"
    return result


def check_number(text: str) -> bool:
    if text.isdigit():
        return True
    else:
        try:
            float(text)
            return True
        except ValueError:
            return False
