from sqlalchemy import create_engine, inspect, text


def explore_db():
    # Connect to the database
    engine = create_engine("sqlite:///instance/books.db")

    # Create an inspector object
    inspector = inspect(engine)

    # Get table names
    tables = inspector.get_table_names()
    print("Tables in the database:", tables)

    # Explore each table
    for table in tables:
        print(f"\nColumns in {table}:")
        columns = inspector.get_columns(table)
        for column in columns:
            print(f"{column['name']} - {column['type']}")

        # Print the first few rows
        with engine.connect() as connection:
            result = connection.execute(text(f"SELECT * FROM {table} LIMIT 5"))
            print("\nFirst 5 rows:")
            for row in result:
                print(row)


if __name__ == "__main__":
    explore_db()
