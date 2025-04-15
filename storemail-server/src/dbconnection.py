import sqlite3

class DbConnection():
    def __init__(self):
        try:
            with sqlite3.connect("../database.db", check_same_thread=False) as conn:
                print(f"Opened SQLite database with version {sqlite3.sqlite_version} successfully.")
                self.cursor = conn.cursor();
                sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS COUNTER (
                id integer PRIMARY KEY,
                count integer NOT NULL
                ); """
                self.create_table(conn, sql_create_projects_table);
                self.cursor.execute('''INSERT OR IGNORE INTO COUNTER VALUES (1, 0)''') 
                conn.commit() 

                

        except sqlite3.OperationalError as e:
            print("Failed to open database:", e)
    
    def create_table(self, conn, create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Exception as e:
            print(e)

    def increase_counter(self):
        row = self.cursor.execute('''SELECT COUNT FROM COUNTER WHERE ID=1''').fetchone()
        c = row[0] + 1
        query = '''UPDATE COUNTER SET COUNT = ? WHERE ID=1;'''
        args = (c,)
        self.cursor.execute(query, args) 
        return c 