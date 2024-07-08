from app import create_app, db
from app.models import Movie

app = create_app()

with app.app_context():
    print("Tables in the database:", db.engine.table_names())
    for table in db.metadata.tables.items():
        print("Columns in", table[0] + ":")
        for column in table[1].columns:
            print(f"{column.name} - {column.type}")
