import sqlite3
from getpass import getpass

# This function checks if exists a system password
def check_system_password():
    cursor.execute("""CREATE TABLE IF NOT EXISTS system (password TEXT NOT NULL) """)
    cursor.execute(""" SELECT password FROM system """)
    return cursor.fetchall()

# This function creates a system password passed by parameter
def create_system_password(password):
    cursor.execute(f""" INSERT INTO system (password) VALUES ('{password}') """)
    conn.commit()
    
# Login
def login_system(password):
    cursor.execute(""" SELECT password FROM system """)
    sys_pwd = cursor.fetchone()[0]
    if password == sys_pwd:
        return True
    else:
        return False

# Menu with 4 options(Insert, Search, Delete and Exit)
def show_menu():
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    print('Select an option: ')
    print('1 - Insert Password')
    print('2 - Search Password')
    print('3 - Delete Password')
    print('4 - Exit')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')



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
        print('Success...')
    else:
        print('Fail...')
        conn.close()
        exit(0)

menu = True
while menu:
    show_menu()
    option = input()
    if option == '1':
        pass
    elif option == '2':
        pass
    elif option == '3':
        pass
    elif option == '4':
        menu = False
        print('Exitting...')
    else:
        print('Invalid option...')

conn.close()