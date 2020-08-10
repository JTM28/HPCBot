from src.db.mongodb import Database


def update_many(db: str, coll: str, query: dict, *args, upsert: bool = False):
    """
    Convenience function for updating many documents at once in MongoDB
    :param db: The database to apply the update to
    :param coll: The collection within the database to apply the update to
    :param query: The query to be applied to all documents matching a filter
    :param args: 1 or more filters in dict format {<key>: <val>} to be queried
    :param upsert: MongoClient argument to create the document if it doesnt exist yet
    """
    filts = []
    for arg in args:
        if isinstance(arg, dict):
            filts.append(arg)
    Database().client[db][coll].update_many({'$or': filts}, query, upsert=upsert)



def add_document_key(db, coll, key, val):
    obj = Database(db=db, coll=coll)
    docs = list(obj.coll().find())
    for d in docs:
        obj.coll().update_one({'_id': d['_id']}, {'$set': {key: val}})

    return


# add_document_key('CRATE', 'accounts', 'settings.hidden', False)



def remove_test_docs():
    db = Database().client['CRATE']
    colls = db.list_collection_names()
    user_doc = db['accounts'].find_one({'info.email': 'test@test'})
    if isinstance(user_doc, dict):
        user_id = user_doc['user-id']
        container_ids = list(user_doc['containers'].keys())
        for coll in colls:
            if coll != 'containers':
                db[coll].delete_one({'user-id': user_id})

        for uid in container_ids:
            db['containers'].delete_one({'container-id': uid})