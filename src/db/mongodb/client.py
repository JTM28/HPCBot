from time import sleep
from pymongo import (
    MongoClient,
    errors
)


from src.conf import RUNTIME



class MongoBackend:
    """
    Backend Adapter for MongoDB.

    For configuring the MongoBackend, a valid mongo_uri is needed

    """
    __slots__ = ['_uri', '_threads', '_retries', '_delay', 'client']

    def __init__(self,
                 uri=RUNTIME['MONGO_URI'],
                 threads=100,
                 retries=3,
                 retry_delay=3,
                 ):
        self._uri = uri
        self._threads = 100
        self._retries = retries

        self._connect()


    def _connect(self):
        count = 0

        while count < self._retries:
            try:
                self.client = MongoClient(self._uri)
                return

            except errors.ServerSelectionTimeoutError:
                count += 1
                sleep(self._delay)
        print('DatabaseConnectionError: Could Not Connect to MongoDB')





