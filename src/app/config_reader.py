import configparser
from dataclasses import dataclass


@dataclass
class Bot:
    TOKEN: str
    admins: tuple
    local_tz: str


@dataclass
class Base:
    dbname: str
    user: str
    password: str
    host: str
    port: int


@dataclass
class Config:
    bot: Bot
    base: Base


def load_config(path: str):
    config = configparser.ConfigParser()
    config.read(path)

    bot = config["bot"]
    base = config["base"]

    return Config(
        bot=Bot(
            TOKEN=bot["TOKEN"],
            admins=eval(bot["admins"]),
            local_tz=bot["local_tz"]
        ),
        base=Base(
            dbname=base["dbname"],
            user=base["user"],
            password=base["password"],
            host=base["host"],
            port=int(base["port"])
        )
    )
