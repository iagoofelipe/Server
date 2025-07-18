from base.consts import SERVER_CMD_SEP

CMD_MACHINE_DATA = SERVER_CMD_SEP + 'MACHINE_DATA'
CMD_USER_VALIDATE = SERVER_CMD_SEP + 'USER_VALIDATE'
CMD_USER_CREATE = SERVER_CMD_SEP + 'USER_CREATE'

# Machine Data Fields

MACHINE_DETAIL_FIELDS = {
    'Motherboard': {'Name', 'Vendor', 'IdentifyingNumber'},
    'OS': {'Caption', 'Version', 'BuildNumber', 'Manufacturer', 'SerialNumber', 'InstallDate'},
    'Processor': {'Name', 'NumberOfLogicalProcessors', 'NumberOfCores'},
}

MACHINE_PROGRAM_FIELDS = ['DisplayName', 'DisplayVersion', 'InstallDate', 'Publisher'] # deve ser lista para seguir o padrão json tratado no servidor


# Database
