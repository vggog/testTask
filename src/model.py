from sqlalchemy import Table, Column, String, Integer, MetaData


metadata = MetaData()

user_table = Table(
    "users", metadata,
    Column("id", Integer(), primary_key=True),
    Column("sity", String()),
)
