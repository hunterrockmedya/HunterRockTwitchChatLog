
import sqlite3, logging, random
logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.create_db()
    
    def create_db(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Messages (
            user TEXT,
            type TEXT,
            channel TEXT,
            message TEXT,
            time INTEGER,
            time_since_last REAL)
        """
        logger.debug("Creating Database...")
        self.execute(sql)
        logger.debug("Database created.")

    def execute(self, sql, values=None, fetch=False):
        with sqlite3.connect("TwitchLog.db") as conn:
            cur = conn.cursor()
            if values is None:
                cur.execute(sql)
            else:
                cur.execute(sql, values)
            conn.commit()
            if fetch:
                return cur.fetchall()
    
    def add_item(self, *args):
        self.execute("INSERT INTO Messages(user, type, channel, message, time, time_since_last) VALUES (?, ?, ?, ?, ?, ?)", args)