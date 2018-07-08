from psycopg2 import connect


class DatabaseHelper(object):

    def __init__(self, host, dbname, user, password):
        try:
            self.conn = connect(dbname=dbname, user=user, host=host, password=password)
        except:
            print("Connection failed!")

    def execute_script(self, script):
        cur = self.conn.cursor()
        cur.execute(script)
        self.conn.commit()

    def execute_select(self, script):
        cur = self.conn.cursor()
        cur.execute(script)
        rows = cur.fetchall()
        return rows