import sqlite3
import json
from models import Entry


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./journal.db") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.date,
            a.entry,
            a.mood_id
        FROM entry a
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            entry = Entry(row['id'], row['date'], row['entry'],
                            row['mood_id'])

            entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)


# Function with a single parameter
def get_single_entry(id):
    with sqlite3.connect("./journal.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            a.id,
            a.date,
            a.entry,
            a.mood_id
        FROM entry a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        entry = Entry(row['id'], row['date'], row['entry'],
                            row['mood_id'])

        return json.dumps(entry.__dict__)