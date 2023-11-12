from sqlalchemy import inspect

def get_tables_have_data(engine):
    inspector = inspect(engine)
    table_names = inspector.get_table_names()

    for table_name in table_names:
        result = engine.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = result.scalar()

        if row_count > 0:
            return True

    return False
