from sqlalchemy import Connection, text

class GenomeRepository:
    def __init__(self, connection: Connection):
        self.connection = connection

        self.add_statement = text("INSERT INTO sequence (name, data) VALUES (:name, :data);")
        self.get_statement = text("SELECT * FROM sequence WHERE sequence.id = :sequence_id;")
        self.getall_statement = text("SELECT id FROM sequence;")
    
    def add(self, sequence: str):
        self._add(sequence)
    
    def get(self, sequence_id: int):
        return self._get(sequence_id)
    
    def getall(self):
        return self._getall()

    def _add(self, name: str, data: str):
        with self.connection.begin():
            result = self.connection.execute(self.add_statement.bindparams(name=name, data=data))
            self.connection.commit()
            return result

    def _get(self, sequence_id: int):
        with self.connection.begin():
            self.connection.execute(self.get_statement.bindparams(sequence_id=sequence_id))
            self.connection.commit()
    
    def _getall(self):
        with self.connection.begin():
            self.connection.execute(self.getall_statement)