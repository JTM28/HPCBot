from exchanges import binance


from src.db.mongodb import Database


METHODS = [binance.get_pairs]


def update():
    db = Database(db='CRYPTO-CRATE', coll='exchanges')
    for meth in METHODS:
        record = meth()
        db.coll().update_one({'exchange': record['exchange']}, {'$set': record}, upsert=True)

update()