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
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    redis: Redis
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
        misc=Miscellaneous()
    )
