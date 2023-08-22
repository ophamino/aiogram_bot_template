import configparser
from dataclasses import dataclass


@dataclass
class DbConfig:
    host: str
    password: str
    user: str
    name: str
    port: str


@dataclass
class TgBot:
    token: str
    admin_id: int
    use_redis: bool


@dataclass
class Settings:
    tg_bot: TgBot
    db: DbConfig


def load_settings() -> Settings:
    settings = configparser.ConfigParser()
    settings.read("settings.ini")

    tg_bot = settings["tg_bot"]

    return Settings(
        tg_bot=TgBot(
            token=tg_bot.get("token"),
            admin_id=tg_bot.getint("channel_id"),
            use_redis=tg_bot.getboolean("use_redis"),
        ),
        db=DbConfig(**settings["db"]),
    )
