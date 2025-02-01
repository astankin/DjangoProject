import sqlite3

def get_all_students_as_dict(database_path):

    query = "SELECT student_number, first_name, last_name, email, field_of_study, gpa FROM students_student"
    
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Execute the query
        cursor.execute(query)

        # Fetch all rows
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]  # Get column names

        # Convert rows into a dictionary of dictionaries
        results = {row[0]: dict(zip(columns, row)) for row in rows}
        return results
    except sqlite3.Error as e:
        print(f"Error accessing database: {e}")
        return {}
    finally:
        # Ensure the connection is closed
        if conn:
            conn.close()

if __name__ == "__main__":
    database_path = "db.sqlite3"  # Replace with your database file path
    students = get_all_students_as_dict(database_path)
    print(students)
