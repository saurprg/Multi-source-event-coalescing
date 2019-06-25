import sqlitedict as sql

class dictDBHelper:
    '''
        This file helps to get a global acess to the Singleton
        Sqlite object
    '''
    def __init__(self,dbpath):
        '''
            ..dbpath is path of directory where db is stored
        '''
        self.__db=None
        self.__created=False
        self.__dbpath=dbpath

    def getDB(self):
        '''
            returns and initialize sigleton instance of db
        '''
        if not self.__created :
            self.__db=sql.SqliteDict(self.__dbpath,autocommit=True)
            self.__created=True
        return self.__db

    def update_in_database(self,current_event,signature):
        '''
            updates Sqlitedict with current_event at given signature as key
        '''
        self.__db[signature].append(current_event)

    def get_sign(self,x):
        '''
            This method generates the signature for the event based
            on the inherent features of the events
        '''
        return str(x["Id"])+'.'+x["UserId"]+'.'+x["MachineName"]


    def shift_all_records_in_db(self,events_list):
        '''
            shifts all the event records in event list to Sqlitedict
        '''
        for events in events_list:
            self.__db[self.get_sign(events[0])] = events
