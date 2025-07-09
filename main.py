"""

Main entry, used to invoke the needed resource by commandline.

"""

import sys, os

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

    else:
        print(
            f'usage: {os.path.basename(__file__)} [option [-h]]',
            '',
            'options:',
            '\tchat.app\t\tChat application',
            '\tchat.server\t\tChat server',
            '',
            'parameters:',
            '\t-h, --help\t\tshow the help message',
            sep='\n'
        )