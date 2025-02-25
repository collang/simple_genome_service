from sqlalchemy import MetaData, Table, Column, Integer, String

metadata = MetaData()

sequence = Table(
    "sequence",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("data", String, nullable=False),
)