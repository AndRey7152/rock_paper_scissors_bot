from dataclasses import dataclass
from environs import Env

@dataclass
class Bot:
    token: str 
    
@dataclass
class Config:
    tg_bot: Bot
    
def load_config(path: str | None = None) -> Config:
    env = Env()
    env.read_env(path)
    return Config(tg_bot=Bot(token=env('BOT_TOKEN')))