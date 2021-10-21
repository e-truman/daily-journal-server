import sqlite3
import json
from models import Entry


def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./journal.db") as conn: # allows to use sqlite3 with package we imported. use .connect to interact with database. use with as syntax

        # Just use these. It's a Black Box.
        # on conn class instance, row factory is a property or method. set equal to sqlite3.row. tells to get rows out of database. isntructions for how to get row
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        #conn.cursor after we know how to get rows. have to do this conn.cursor and execute in order. makes environment to execute query

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.date,
            a.entry,
            a.mood_id
        FROM journal a
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall() # gets everything in select statement

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
        FROM journal a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an entry instance from the current row
        entry = Entry(data['id'], data['date'], data['entry'],
                            data['mood_id'])

        return json.dumps(entry.__dict__)

def delete_entry(id):
    with sqlite3.connect("./journal.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Journal
        WHERE id = ?
        """, (id, ))


