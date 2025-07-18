"""

Main entry, used to invoke the needed resource by commandline.

"""

import sys, os
from base.consts import FILE_CONFIG

def helpMessage():
    print(
        f'usage: {os.path.basename(__file__)} [option [-h]]',
        '',
        'options:',
        '\tchat.app',
        '\tchat.server',
        '\tinventory.app',
        '\tinventory.server',
        '',
        '\treset',
        '',
        '\ttest',
        '\t\tinventory.app',
        '\t\t\tuserForm',
        '',
        'parameters:',
        '\t-h, --help\t\tshow the help message',
        sep='\n'
    )

if __name__ == '__main__':
    argv = sys.argv
    length = len(argv)
    option = None
    args = []

    if length > 1:
        option = argv[1]
    
    if length > 2:
        args = argv[2:]

    if option == 'chat.app':
        from apps.chat.app import ChatApp
        app = ChatApp(args)
        app.exec()

    elif option == 'chat.server':
        from servers.chat.server import ChatServer
        server = ChatServer(args)
        server.startloop()

    elif option == 'inventory.app':
        from apps.inventory.app import InventoryApp
        app = InventoryApp(args)
        app.exec()

    elif option == 'inventory.server':
        from servers.inventory.server import InventoryServer
        server = InventoryServer(args)
        server.startloop()

    elif option == 'reset':
        if os.path.exists(FILE_CONFIG):
            print('config file removed')
            os.remove(FILE_CONFIG)
        else:
            print('config not found')

    elif option == 'test':
        if len(args) != 2:
            helpMessage()
        
        elif args[0] == 'inventory.app':
            from apps.inventory.tests import *

            eval(f'test_{args[1]}()')

    else:
        helpMessage()