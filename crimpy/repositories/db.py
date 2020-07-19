from pony import orm


database = orm.Database()
database.bind(
    provider="sqlite",
    filename="crimpy.sqlite",
    create_db=True
)
# orm.sql_debug(True)

def start_database():
    database.generate_mapping(create_tables=True)