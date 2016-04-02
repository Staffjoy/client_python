import logging


class DefaultConfig:
    ENV = "prod"
    LOG_LEVEL = logging.INFO
    BASE = "https://www.staffjoy.com/api/v2/"
    REQUEST_SLEEP = 0.5


class StageConfig(DefaultConfig):
    ENV = "stage"
    BASE = "https://stage.staffjoy.com/api/v2/"


class DevelopmentConfig(DefaultConfig):
    ENV = "dev"
    LOG_LEVEL = logging.DEBUG
    BASE = "http://dev.staffjoy.com/api/v2/"


config_from_env = {  # Determined in main.py
    "dev": DevelopmentConfig,
    "stage": StageConfig,
    "prod": DefaultConfig,
}
