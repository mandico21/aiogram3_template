from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]
    use_redis: bool


@dataclass
class Redis:
    host: str


@dataclass
class DB:
    host: str
    port: int
    name: str
    user: str
    password: str


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    redis: Redis
    db: DB
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            admin_ids=list(map(int, env.list("ADMINS"))),
            use_redis=env.bool("USE_REDIS"),
        ),
        redis=Redis(
            host=env.str("REDIS_HOST")
        ),
        db=DB(
            host=env.str('POSTGRES_HOST'),
            password=env.str('POSTGRES_PASSWORD'),
            user=env.str('POSTGRES_USER'),
            name=env.str('POSTGRES_DB'),
            port=env.str('POSTGRES_PORT'),
        ),
        misc=Miscellaneous()
    )
