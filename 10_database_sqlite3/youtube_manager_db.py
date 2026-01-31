import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id, new_name, new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))    # tuple in sigle must add comma
    conn.commit()

def main():
    while True:
        print("\n Youtube manager app with DB")
        print("1. List Videos")
        print("2. Add Videos")
        print("3. Update Videos")
        print("4. Delete Videos")
        print("5. exit app")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_video(name, time)
        elif choice == '3':
            video_id = input("Enter video ID to update: ")
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            update_video(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter video ID to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print("Invalid Choice ")

    conn.close()

if __name__ == "__main__":
    main()



'''  Notes :-

    1. The Cursor Object

    Concept: The cursor is your main interface or "worker" to interact with the database.
    Usage: You don't execute SQL commands directly on the conn (connection) object; you must use cursor.execute().
    Analogy: If conn is the highway to the database, cursor is the truck that carries the data back and forth.

    2. conn.commit()

    Crucial Step: When you INSERT, UPDATE, or DELETE, the changes are initially stored in temporary memory.
    Function: commit() saves these changes permanently to the database file. If you forget this, your data will be lost when the script ends.

    3. SQL Injection Prevention (? Placeholders)

    The Syntax: VALUES (?, ?)
    Why: Never use Python f-strings (e.g., f"VALUES ({name})" ) inside SQL queries. It allows hackers to manipulate your database (SQL Injection).
    How it works: Passing the variables as a tuple (name, time) ensures Python treats them strictly as data, not executable code.

    4. The Single-Item Tuple Trap

    The Code: cursor.execute(..., (video_id,))
    The Comma: In Python, (value) is just a math expression. (value,) (with a comma) is a tuple.
    Why it matters: The execute method expects a sequence (tuple/list) for its second argument. Without the comma, Python will throw an error.

    5. fetchall() vs fetchone()

    fetchall(): Retrieves all rows from the last executed SELECT statement and returns them as a list of tuples.
    fetchone(): Retrieves the next row (one by one). Used to save memory when dealing with massive datasets.

    6. Primary Key

    id INTEGER PRIMARY KEY:

    This column automatically manages unique IDs for your videos (1, 2, 3...).
    You do not need to provide a value for id when inserting a new video; SQLite handles the auto-incrementing for you.

    7. Clean Up (conn.close())
    Best Practice: Always close the connection when the program ends to release system resources and ensure all locks on the database file are removed.
'''