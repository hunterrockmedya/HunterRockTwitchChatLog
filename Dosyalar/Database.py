
import sqlite3, logging, random
logger = logging.getLogger(__name__)

class Database:
    def __init__(self):
        self.create_db()
    
    def create_db(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Messages (
            full_message TEXT,
            tags TEXT,
            command TEXT,
            user TEXT,
            type TEXT,
            params TEXT,
            channel TEXT,
            message TEXT,
            time INTEGER,
            time_since_last REAL,
            PRIMARY KEY(full_message, time))
        """
        logger.debug("Veritabanı Oluşturuluyor...")
        self.execute(sql)
        logger.debug("Veritabanı Oluşturuldu.")

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
        self.execute("INSERT INTO Messages(full_message, tags, command, user, type, params, channel, message, time, time_since_last) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", args)