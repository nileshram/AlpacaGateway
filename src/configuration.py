# Created by nilesh at 09/10/2020
from os.path import dirname, join, exists, isfile
import json

class ConfigurationFactory:

    @staticmethod
    def create_config(file):
        conf_dir = join(dirname(dirname(__file__)), "conf")
        conf_path = join(conf_dir, "".join((file, ".json")))
        if exists(conf_path) and isfile(conf_path):
            with open(conf_path) as f:
                conf = json.load(f)
        else:
            raise Exception("Config file not located inside directory, please check")
        return conf
