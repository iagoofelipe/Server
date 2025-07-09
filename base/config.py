from typing import Sequence
from argparse import ArgumentParser

class Configuration:
    def __init__(self, package:str, argv:Sequence[str]=None):
        self.__pkg = package
        self.__parser = parser = ArgumentParser()

        parser.add_argument('--debug', action='store_true', help='display the log in DEBUG mode (if omitted, INFO mode is used instead)')
        parser.add_argument('--save-log', dest='saveLog', action='store_true', help=f'save the log in the file')

    def exec(self):
        pass