import os
import sqlite3


class PasswordDatabase:
    def __init__(self, db_name):
        if not db_name:
            raise ValueError("Database name must be provided")
        self.db_name = db_name
        self.create_table()
        try:
            os.chmod(self.db_name, 0o600)
        except FileNotFoundError:
            pass
        self.connection = None

    def connect(self):
        self.connection = sqlite3.connect(self.db_name)

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        cursor.execute(query, params or ())
        self.connection.commit()
        return cursor

    def create_table(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS user_passwords (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT NOT NULL,
            password TEXT NOT NULL
        );
        """
        self.connect()
        self.execute_query(create_table_query)
        self.disconnect()

    def disconnect(self):
        if self.connection:
            self.connection.close()

    def get_service_to_password_dict(self):
        cursor = self.execute_query("SELECT service, password FROM user_passwords")
        rows = cursor.fetchall()
        return {service: password for service, password in rows} if rows else {}

    def add_password(self, service, password):
        self.connect()
        self.execute_query(
            "INSERT INTO user_passwords (service, password) VALUES (?, ?)",
            (service, password),
        )
        self.disconnect()

    def remove_password(self, service):
        self.connect()
        self.execute_query(
            "DELETE FROM user_passwords WHERE service = ?",
            (service,),
        )
        self.disconnect()
