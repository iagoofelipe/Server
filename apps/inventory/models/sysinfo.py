from typing import NamedTuple, Iterable
import subprocess

from ..backend.consts import DEFAULT_PROPS

class Program(NamedTuple):
    DisplayName:str
    DisplayVersion:str
    InstallDate:str
    Publisher:str


def getPrograms() -> tuple[Program]:
    cmd = f'powershell "Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, InstallDate, Publisher | Format-List"'
    serial = subprocess.check_output(cmd, shell=True)
    programs = [{}]

    for row in serial.decode(errors='ignore').strip().split('\r\n'):
        if not row:
            programs.append({})
            continue

        key, value = [d.strip() for d in row.split(':', 1)]
        programs[-1][key] = value

    # removing empty data and casting from dict to Program class
    return tuple(map(lambda d: Program(**d), filter(lambda d: d['DisplayName'], programs)))


def getProperties(className:str, properties:Iterable[str]) -> dict:
    cmd = f'powershell "Get-CimInstance -ClassName {className} | Select-Object -Property {', '.join(properties)} | Format-List"'
    serial = subprocess.check_output(cmd, shell=True)
    props = {}

    for row in serial.decode().strip().split('\r\n'):
        key, value = [d.strip() for d in row.split(':', 1)]
        props[key] = value

    return props

def getDefaultProperties():
    pass