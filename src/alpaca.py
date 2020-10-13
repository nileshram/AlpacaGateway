# Created by nilesh at 09/10/2020
from configuration import ConfigurationFactory
from os.path import dirname
import sys

def _configure_env():
    #configure the environment and append project root to path
    env_path = dirname(__file__)
    sys.path.append(env_path)

if __name__ == "__main__":
    _configure_env()

