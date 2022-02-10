from logging import config as logging_config

import yaml


def setup_logging(logging_config_path: str) -> None:
    with open(logging_config_path, "r") as stream:
        logging_config_yaml = yaml.load(stream, Loader=yaml.FullLoader)

    logging_config.dictConfig(logging_config_yaml)
