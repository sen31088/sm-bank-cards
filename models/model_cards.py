from config import DB_Config

class Carddetails:
    collection = DB_Config.col_carddetails

    @classmethod
    def save(cls, data):
        return cls.collection.insert_one(data)

    @classmethod
    def get_data(cls, data):
        return dict(cls.collection.find_one(data))