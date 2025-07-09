import os, getpass
from configparser import ConfigParser
from argparse import ArgumentParser
import logging as log
from typing import Sequence

from base.consts import *

def config(pkg:str, appmode=False, database=False, argv:Sequence[str]=None):
    configName = pkg.upper() + '_CONFIG'

    if configName in os.environ:
        return
        
    os.environ[configName] = ''
    configParser = ConfigParser()
    valid = False
    logfile = f'{PATH_LOG}\\{pkg}.log'

    if os.path.exists(FILE_CONFIG):
        with open(FILE_CONFIG) as f:
            configParser.read_file(f)

        # validating file
        if configParser.has_option(pkg+'.Server', 'ip') and configParser.has_option(pkg+'.Server', 'port'):
            valid = True

        if database and (not configParser.has_option(pkg+'.Database', 'host') \
                            or not configParser.has_option(pkg+'.Database', 'username') \
                            or not configParser.has_option(pkg+'.Database', 'password')):
            valid = False
    
    if not valid:
        print('Please, provide the default settings to start...')
        ip = input(f'IP ({DEFAULT_IP}): ')
        port = input(f'Port ({DEFAULT_PORT}): ')
        data = {
            pkg+'.Server': {
                'ip': ip if ip else DEFAULT_IP,
                'port': port if port else DEFAULT_PORT,
            }
        }

        if database:
            host = input(f'Database Host ({DEFAULT_DB_HOST}): ')
            data[pkg+'.Database'] = {
                'host': host if host else DEFAULT_DB_HOST,
                'username': input('Database Username: '),
                'password': getpass.getpass('Database Password: '),
            }

        configParser.update(data)

        with open(FILE_CONFIG, 'w') as f:
            configParser.write(f)

    os.environ['SERVER_IP'] = configParser[pkg+'.Server']['ip']
    os.environ['SERVER_PORT'] = configParser[pkg+'.Server']['port']

    if database:
        os.environ['DATABASE_HOST'] = configParser[pkg+'.Database']['host']
        os.environ['DATABASE_USERNAME'] = configParser[pkg+'.Database']['username']
        os.environ['DATABASE_PASSWORD'] = configParser[pkg+'.Database']['password']

    # logs
    aparser = ArgumentParser()

    aparser.add_argument('--debug', action='store_true', help='display the log in DEBUG mode (if omitted, INFO mode is used instead)')
    aparser.add_argument('--save-log', dest='saveLog', action='store_true', help=f'save the log in the file {logfile}')

    args = aparser.parse_args(argv)
    log_params = {
        'level': log.DEBUG if args.debug else log.INFO,
        'filename': logfile if args.saveLog else None,
        'datefmt': '%Y-%m-%d %H:%M:%S',
        'format': '[%(asctime)s %(levelname)s] %(message)s',
    }

    if args.saveLog:
        os.makedirs(PATH_LOG, exist_ok=True)

    log.basicConfig(**log_params)
    log.info(f'[config] log level: {log.getLevelName(log_params['level'])}')