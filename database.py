import sqlite3

cx = sqlite3.connect('projects.db')
cu = cx.cursor()

def insert_project(name: str):
    _backup_db()
    cu.execute('INSERT INTO Projects (name) VALUES (?)', [name])
    cx.commit()

def update_project(id=None, name=None, **categories):
    _backup_db()
    if id:
        for category, value in categories.items():
            cu.execute('UPDATE Projects SET ? = ? WHERE id = ?', [category, value, id])
    elif name:
        for category, value in categories.items():
            cu.execute('UPDATE Projects SET ? = ? WHERE name = ?', [category, value, name])
    else:
        raise 'Identifier not given'

def delete_project(name: str):
    _backup_db()
    cu.execute('DELETE FROM Projects WHERE Projects.name = ?', [name])
    cx.commit()

def _reset_db():
    want_to_reset = 'y'
    # want_to_reset = input('Are you sure you want to reset the database? (y/n)')
    if want_to_reset == 'y':
        _backup_db()
        cu.execute('DROP TABLE IF EXISTS Projects')
        cu.execute('''CREATE TABLE IF NOT EXISTS Projects(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            upload_date DATE DEFAULT CURRENT_DATE,
            completed  DEFAULT 0)''')
        cx.commit()

def _print_db():
    print(cu.execute('SELECT * FROM Projects').fetchall())

def _backup_db():
    cu.execute('DROP TABLE IF EXISTS Backup')
    cu.execute('CREATE TABLE Backup AS SELECT * FROM Projects')
    cx.commit()

if __name__ == '__main__':
    _reset_db()
    insert_project('Calculator')
    _print_db()
    