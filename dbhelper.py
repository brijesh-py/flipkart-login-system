import mysql.connector
from mysql.connector import Error

class DBhelper:
    def __init__(self):
        self.conn = self.create_connection()

    def create_connection(self):
        try:
            connection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='my_data'
            )
            return connection
        except Error as e:
            print(f"Error connecting to database: {e}")
            sys.exit()

    def execute_query(self, query, params=None):
        try:
            cursor = self.conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.conn.commit()
            return cursor
        except Error as e:
            print(f"Error executing query: {e}")
            return None

    def register(self, name, email, password):
        try:
            query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            params = (name, email, password)
            self.execute_query(query, params)
            return True
        except Error as e:
            print(f"Error registering user: {e}")
            return False

    def login(self, email, password):
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        params = (email, password)
        cursor = self.execute_query(query, params)
        if cursor:
            response = cursor.fetchall()
            return response
        else:
            return None

    def see_profile(self, user_email):
        query = "SELECT * FROM users WHERE email = %s"
        params = (user_email,)
        cursor = self.execute_query(query, params)
        if cursor:
            response = cursor.fetchall()
            return response
        else:
            return None

    def edit_profile(self, email, update_name, update_email, update_password):
        query = "UPDATE users SET name = %s, email = %s, password = %s WHERE email = %s"
        params = (update_name, update_email, update_password, email)
        success = self.execute_query(query, params)
        return success is not None

    def delete_account(self, email, password):
        query = "DELETE FROM users WHERE email = %s AND password = %s"
        params = (email, password)
        success = self.execute_query(query, params)
        return success is not None
