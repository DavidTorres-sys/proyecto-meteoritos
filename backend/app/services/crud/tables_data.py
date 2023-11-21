from sqlalchemy import inspect

def get_tables_have_data(engine):
    inspector = inspect(engine)
    table_names = inspector.get_table_names()

    if "earthquake" in table_names:
        result = engine.execute("SELECT COUNT(*) FROM earthquake")
        row_count = result.scalar()

        return row_count > 0

    return False

