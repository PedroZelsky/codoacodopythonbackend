from app.database import get_db


class User:

    def __init__(self,name=None,lastname=None,email=None,password=None):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password


    def serialize(self):
        return {
            'Name':self.name,
            'Lastname':self.lastname,
            'E-mail':self.email
        }


    @staticmethod
    def get_users():
        db = get_db()
        cursor = db.cursor()
        query = "SELECT name,lastname,email,password FROM users"
        cursor.execute(query)
        rows = cursor.fetchall()
        users = [User(name=row[0], lastname=row[1], email=row[2], password=row[3]) for row in rows]
        cursor.close()
        return users


    @staticmethod
    def get_user(email):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT name,lastname,email,password FROM users WHERE email = %s", (email,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return User(name=row[0], lastname=row[1], email=row[2], password=row[3])
        return None


    def register(self):
        db = get_db()
        cursor = db.cursor()
        new_user = self.get_user(self.email)
        if new_user == None:
            cursor.execute("""
                INSERT INTO users (name, lastname, email, password) VALUES (%s, %s, %s, %s)
            """, (self.name, self.lastname, self.email, self.password))
        db.commit() 
        cursor.close()


    def unregister(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM users WHERE email = %s", (self.email,))
        db.commit()
        cursor.close()