import sqlite3

connection = sqlite3.connect("project_tracker.db")

def initialize_database():
    cursor = connection.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS Projects")
        cursor.execute("DROP TABLE IF EXISTS Members")
    except:
        pass

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Members (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Projects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            member_id INTEGER,
            FOREIGN KEY (member_id) REFERENCES Members (id)
        )
    ''')

    for member in [
        {'name': 'John Doe'},
        {'name': 'Jane Smith'},
        {'name': 'Bob Johnson'},
    ]:
        cursor.execute(f"INSERT INTO Members (name) VALUES ('{member['name']}')")

    for project in [
        {'title': 'Project A', 'description': 'Description for Project A', 'member_id': 1},
        {'title': 'Project B', 'description': 'Description for Project B', 'member_id': 2},
        {'title': 'Project C', 'description': 'Description for Project C', 'member_id': 3},
    ]:
        cursor.execute(f"INSERT INTO Projects (title, description, member_id) VALUES ('{project['title']}', '{project['description']}', {project['member_id']})")

    connection.commit()

def get_all_projects():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Projects")
    columns = [column[0] for column in cursor.description]
    projects = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return projects

def add_project(title, description, member_id):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Projects (title, description, member_id) VALUES ('{title}', '{description}', {member_id})")
    connection.commit()

def get_project_details(project_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Projects WHERE id = {project_id}")
    columns = [column[0] for column in cursor.description]
    project = dict(zip(columns, cursor.fetchone()))
    return project

def update_project(project_id, title, description, member_id):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE Projects SET title = '{title}', description = '{description}', member_id = {member_id} WHERE id = {project_id}")
    connection.commit()

def delete_project(project_id):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM Projects WHERE id = {project_id}")
    connection.commit()

if __name__ == "__main__":
    initialize_database()
