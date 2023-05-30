import mysql.connector

class DBhelper:
    def __init__(self):
        self.conn = self.create_connection()
        self.cursor = self.conn.cursor()

    def create_connection(self):
        response = mysql.connector.connect(host='localhost', user='root', password='', database='my_data')
        return response

    def close_connection(self):
        self.conn.close()
        return True

    def see_profile(self, email):
        query = f"SELECT * FROM users WHERE email = %s"
        values = (email,)
        self.cursor.execute(query, values)
        return  self.cursor.fetchall()

    def edit_profile(self, email, update_name, update_email, update_password):
        query = "UPDATE users SET name = %s , email = %s , password = %s WHERE email = %s"
        values = (update_name, update_email, update_password, email)
        self.cursor.execute(query, values)
        self.conn.commit()

        query = f"SELECT * FROM users WHERE email = %s"
        values = (update_email,)
        self.cursor.execute(query, values)

        if self.cursor.fetchone():
            return True
        else:
            return False

    def delete_account(self, email, password):
        query = "DELETE FROM users WHERE email = %s AND password = %s"
        values = (email, password)
        self.cursor.execute(query, values)
        self.conn.commit()

        query = f"SELECT * FROM users WHERE email = %s"
        values = (email,)
        self.cursor.execute(query, values)

        if not self.cursor.fetchone():
            return True
        else:
            return False

    def login(self, email, password):
        query = "SELECT * FROM users WHERE email = %s AND password = %s"
        values = (email, password)
        self.cursor.execute(query, values)
        response = self.cursor.fetchall()
        return response

    def register(self, name, email, password):
        query = """
        INSERT INTO users (name, email, password) VALUES (%s, %s, %s)
        """
        values = (name, email, password)
        initial_row_count = self.cursor.rowcount
        self.cursor.execute(query, values)
        self.conn.commit()

        final_row_count = self.cursor.rowcount
        if final_row_count > initial_row_count:
            return True
        else:
            return False