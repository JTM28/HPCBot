from src.db.mongodb.client import MongoBackend



class Database(MongoBackend):

    """
    Database interface for MongoDB

    NOT Fork Safe:
        This class should be inherited by each process since the "pymongo" library is not fork safe.
        Meaning that any attempt to share an instance of the "Database" class across processes / from a
        parent process to child processes is not considered viable.

    IS Thread Safe:
        This class is thread safe however, thread pool size is set by default to 100 in the "MongoBackend"
        class. This can be changed for allowing more or less concurrent threads to use the same instance
        of the Database class


    Arguments *OPTIONAL*:
        db: str: The database to interact



    """

    def __init__(self, **kwargs):
        super().__init__()
        """
        Arguments: 
            db: Sets the active database within MongoDB 
            coll: Sets the collection within the "db"
        """
        if len(list(kwargs.items())) > 0:
            for k, v in kwargs.items():
                setattr(self, '_%s' % str(k), v)

    def db(self):
        """
        :returns The instance of "BaseClient(MongoClient).client.<database> "

        :raises
            :AttributeError if the "db" attr is missing
        """
        try:
            if not hasattr(self, '_db'):
                raise AttributeError

            return self.client[getattr(self, '_db')]
        except AttributeError:
            print('Missing Attribute "db" ')


    def coll(self):
        """
        :returns The instance of "BaseClient(MongoClient).client.<database>.<collection>"

        :raises
            :AttributeError if the "coll" attr is missing
        """
        try:
            self.db()
            if not hasattr(self, '_coll'):
                raise AttributeError
            return self.client[str(getattr(self, '_db'))][str(getattr(self, '_coll'))]

        except AttributeError:
            print('Missing Attribute "coll" ')









