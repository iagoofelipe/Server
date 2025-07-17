from mysql.connector import connect
import logging as log
import os

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance
    
    def initialize(self):
        try:
            self.__con = connect(host=os.environ['DATABASE_HOST'], user=os.environ['DATABASE_USERNAME'], password=os.environ['DATABASE_PASSWORD'])

        except Exception as e:
            log.error(f'[Database] connection error: {e}')
            return False
        
        return True
    
    def validateUser(self, cpf:str) -> str | None:
        with self.__con.cursor() as cursor:
            cursor.execute('SELECT name FROM inventory.user WHERE cpf=%s', (cpf, ))
            r = cursor.fetchone()

        return r[0] if r is not None else None
    
    def createUser(self, name:str, cpf:str) -> bool:
        # log.debug('')
        if self.validateUser(cpf) is None:
            return False

        with self.__con.cursor() as cursor:
            cursor.execute('INSERT INTO inventory.user (name, cpf) VALUES (%s, %s)', (name, cpf))
            self.__con.commit()

        return True