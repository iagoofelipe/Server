from mysql.connector import connect
import logging as log
import os

from .consts import *

class Database:
    _instance = None

    __machineDetailsInsertFields = None
    __machineDetailsInsertPlaceholders = None

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
        
        fields = []
        placeholders = []

        for k, _fields in MACHINE_DETAIL_FIELDS.items():

            for v in _fields:
                field = f'{k}_{v}'

                fields.append(field)
                placeholders.append(f'%({field})s')

        self.__machineDetailsInsertFields = ','.join(fields)
        self.__machineDetailsInsertPlaceholders = ','.join(placeholders)
        self.__cursor = self.__con.cursor()
    
        return True
    
    def validateUser(self, cpf:str) -> tuple[int, str] | None:
        self.__cursor.execute('SELECT id, name FROM inventory.user WHERE cpf=%s', (cpf, ))
        r = self.__cursor.fetchone()
        success = r is not None

        log.info(f'[Database] validate user <{cpf=}>, result: {r}')
        return r if success else None
    
    def createUser(self, name:str, cpf:str) -> bool:
        v = self.validateUser(cpf)
        log.info(f'[Database] create user <{cpf=} {name=}>, found: {v}')
        
        if v is not None:
            return False

        self.__cursor.execute('INSERT INTO inventory.user (name, cpf) VALUES (%s, %s)', (name, cpf))
        self.__con.commit()

        log.info('[Database] user created')
        return True
    
    def checkMachine(self, mac:str) -> int | None:
        log.info(f'[Database] checking machine with mac {mac}...')
        self.__cursor.execute('SELECT id FROM inventory.machine WHERE mac=%s', (mac, ))
        r = self.__cursor.fetchone()
        success = r is not None
        _id = None

        if success:
            _id = r[0]
            log.info(f'[Database] machine found with id {_id}')
        else:
            log.info('[Database] machine not found')

        return _id
    
    def newMachine(self, userId:int, data:dict) -> bool:

        # verify fields
        if data['programs']['fields'] != MACHINE_PROGRAM_FIELDS:
            return False
        
        for key, fields in MACHINE_DETAIL_FIELDS.items():
            if set(data['machine'][key]) != fields:
                return False

        mac = data['mac']
        machineId = self.checkMachine(mac)

        # create a new machine if needed
        if machineId is None:
            self.__cursor.execute('INSERT INTO inventory.machine (creation, mac, user_id) VALUES (now(), %s, %s)', (mac, userId))
            self.__con.commit()
            machineId = self.__cursor.lastrowid
            log.info(f'[Database] new machine created with id {machineId}')

        # create a extraction point
        self.__cursor.execute('INSERT INTO inventory.machine_extraction (extractionDate, machine_id) VALUES (now(), %s)', (machineId, ))
        self.__con.commit()
        extractionId = self.__cursor.lastrowid

        log.info(f'[Database] extraction point created with id {extractionId}')

        # save machine details
        machine_data = {}

        for k, _d in data['machine'].items():
            machine_data.update({ f'{k}_{field}': v for field, v in _d.items() })

        self.__cursor.execute(f'INSERT INTO inventory.machine_details (extraction_id, {self.__machineDetailsInsertFields}) VALUES ({extractionId}, {self.__machineDetailsInsertPlaceholders})', machine_data)
        self.__con.commit()

        # save machine programs
        fields = ','.join(data['programs']['fields'])
        placeholders = ','.join(['%s' for _ in range(len(data['programs']['fields']))])

        self.__cursor.executemany(f'INSERT INTO inventory.machine_programs (extraction_id, {fields}) VALUES ({extractionId}, {placeholders})', data['programs']['data'])
        self.__con.commit()
        
        return True