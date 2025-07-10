import subprocess
from typing import Iterable

def getProperties(className:str, properties:Iterable[str]) -> dict:
    cmd = f'powershell "Get-CimInstance -ClassName {className} | Select-Object -Property {', '.join(properties)} | Format-List"'
    serial = subprocess.check_output(cmd, shell=True)
    props = {}

    for row in serial.decode().strip().split('\r\n'):
        key, value = [d.strip() for d in row.split(':', 1)]
        props[key] = value

    return props

def getPrograms():
    cmd = f'powershell "Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Select-Object DisplayName, DisplayVersion, InstallDate, Publisher | Format-List"'
    serial = subprocess.check_output(cmd, shell=True)
    programs = [{}]

    for row in serial.decode(errors='ignore').strip().split('\r\n'):
        if not row:
            programs.append({})
            continue

        key, value = [d.strip() for d in row.split(':', 1)]
        programs[-1][key] = value

    return programs


if __name__ == '__main__':

    options = (
        ('Win32_ComputerSystemProduct', ('Name', 'Vendor', 'IdentifyingNumber')),
        ('Win32_OperatingSystem', ('Caption', 'Version', 'BuildNumber', 'Manufacturer', 'SerialNumber', 'InstallDate')),
        ('Win32_Processor', ('Name', 'NumberOfLogicalProcessors', 'NumberOfCores')),
    )

    for className, properties in options:
        print('\nClassName', className, 'Properties', properties)

        for key, value in getProperties(className, properties).items():
            print(f'\t{key}: {value}')

    programs = getPrograms()

    for p in programs:
        print('-'*30)

        for k, v in p.items():
            print(f'"{k}": "{v}"')

