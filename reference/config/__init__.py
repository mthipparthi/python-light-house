import os

import yaml
import logging
from pathlib import Path

logger = logging.getLogger()

from dataclasses import dataclass


@dataclass
class Config:
    config_1: str
    config_2: str
    config_3: str


def get_config():
    try:
        environment = os.getenv("ENV", "dev")
        logger.info("Environment {}".format(environment))
        config_file = Path(__file__).resolve().parent.joinpath("config.yaml")
        with open(config_file) as f:
            config = Config(**yaml.load(f, Loader=yaml.CLoader)[environment])
        return config
    except IOError:
        raise ValueError("Failed to get Config File - Please set env variables environment")


config = get_config()


if __name__ == "__main__":
    print(get_config())
