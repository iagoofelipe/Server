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
    },
}

UI_ID_ALERT_FORM = 0
UI_ID_INVENTORY_FORM = 1