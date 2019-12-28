import sqlite3
from getpass import getpass

def check_system_password():
    cursor.execute("""CREATE TABLE IF NOT EXISTS system (password TEXT NOT NULL) """)
    cursor.execute(""" SELECT password FROM system """)
    return cursor.fetchall()

def create_system_password(password):
    cursor.execute(f""" INSERT INTO system (password) VALUES ('{password}') """)
    conn.commit()
    
def login_system(password):
    cursor.execute(""" SELECT password FROM system """)
    sys_pwd = cursor.fetchone()[0]
    if password == sys_pwd:
        return True
    else:
        return False

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

if not check_system_password():
    print('You don\'t have a system password')
    print('Type your new system Password')
    password = getpass()
    create_system_password(password)
    print('Password entered successfully !')

else:
    print('Type your password')
    password = getpass()
    if login_system(password):
        print('Success !')
    else:
        print('Fail !')

conn.close()