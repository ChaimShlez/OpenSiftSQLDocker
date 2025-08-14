from services.data_loader.dataLoader import ConnectionWrapper


class Queries:

    def __init__(self):
        self._connection=ConnectionWrapper()







    def getAll(self):
        sql = "SELECT * FROM agents"
        res = self._connection.select(sql)

        return res


