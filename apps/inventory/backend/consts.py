from base.consts import SERVER_CMD_SEP

DEFAULT_PROPS = {
    'Motherboard': {
        'className': 'Win32_ComputerSystemProduct',
        'properties': ('Name', 'Vendor', 'IdentifyingNumber'),
    },
    'OS': {
        'className': 'Win32_OperatingSystem',
        'properties': ('Caption', 'Version', 'BuildNumber', 'Manufacturer', 'SerialNumber', 'InstallDate'),
    },
    'Processor': {
        'className': 'Win32_Processor',
        'properties': ('Name', 'NumberOfLogicalProcessors', 'NumberOfCores'),
    }
}

UI_ID_ALERT_FORM = 0
UI_ID_INVENTORY_FORM = 1
UI_ID_USER_FORM = 2

CMD_SYSINFO = SERVER_CMD_SEP + 'SYSINFO'
CMD_USER_VALIDATE = SERVER_CMD_SEP + 'USER_VALIDATE'
CMD_USER_CREATE = SERVER_CMD_SEP + 'USER_CREATE'