import subprocess

def getMac() -> str:
    cmd = 'powershell "Get-CimInstance -ClassName Win32_NetworkAdapterConfiguration | Where-Object { $_.MACAddress -and $_.IPEnabled } | Select-Object MACAddress | Format-List"'
    serial = subprocess.check_output(cmd, shell=True)
    props = {}

    for row in serial.decode().strip().split('\r\n'):
        key, value = [d.strip() for d in row.split(':', 1)]
        props[key] = value

    return props['MACAddress']


print(getMac())