
from app import app, db

with app.app_context():
    with db.engine.begin() as conn:

        columns = conn.exec_driver_sql(
            "PRAGMA table_info(post)"
        ).fetchall()

        column_names = [column[1] for column in columns]

        print("Existing columns:", column_names)

        if "auther_id" in column_names and "author_id" not in column_names:
            conn.exec_driver_sql(
                "ALTER TABLE post RENAME COLUMN auther_id TO author_id"
            )
            print("Column renamed successfully!")

        elif "author_id" in column_names:
            print("author_id already exists!")

        else:
            print("Neither column exists. Database needs further inspection.")
