import sqlite3
from getpass import getpass
from tabulate import tabulate

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
    print('Select an option:')
    print('1 - Insert Password')
    print('2 - Search Password')
    print('3 - Delete Password')
    print('4 - Update Password')
    print('5 - Show all')
    print('6 - Exit')
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')

# This function inserts a new password 
# Return : True -> It's inserted a new password
#          False -> app and user already exist
def insert_password(app, user, password):
    if not search_password(app, user):
        cursor.execute(f""" INSERT INTO database (app , user , password) VALUES ('{app}' , '{user}' , '{password}') """)
        conn.commit()
        return True
    return False

# This function does a search in database
# Return : search result (app, user, password)
def search_password(app, user):
    cursor.execute(""" CREATE TABLE IF NOT EXISTS database (app TEXT NOT NULL, user TEXT NOT NULL, password TEXT NOT NULL) """)    
    cursor.execute(f""" SELECT * FROM database WHERE app='{app}' AND user='{user}' """)
    return cursor.fetchone()

# Delete a password by app and user
# Return : True -> It's possible to delete the password info
#          False -> password doesn't exist
def delete_password(app, user):
    if not search_password(app, user):
        return False
    cursor.execute(f""" DELETE FROM database WHERE app='{app}' AND user='{user}' """)
    conn.commit()
    return True

# Show all infos
# Return : all database
def show_all():
    cursor.execute(""" CREATE TABLE IF NOT EXISTS database (app TEXT NOT NULL, user TEXT NOT NULL, password TEXT NOT NULL) """)
    cursor.execute(""" SELECT * FROM database """)
    return cursor.fetchall()

# Updates a password by app end user
# Return : True -> It's possible to delete the password info
#          False -> password doesn't exist 
def update_password(app, user, password):
    if not search_password(app, user):
        return False
    cursor.execute(f""" UPDATE database SET password='{password}' WHERE app='{app}' AND user='{user}' """)
    return True

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

    # INSERT
    if option == '1':
        print('Please, type these infos: ')
        app = input('App: ')
        user = input('User: ')
        password = getpass()
        if insert_password(app, user, password):
            print('Password inserted !')
        else:
            print('An error occurred')

    # SEARCH
    elif option == '2':
        print('Please, type these infos: ')
        app = input('App: ')
        user = input('User: ')
        info = search_password(app, user)
        if not info:
            print('An error occurred')
        else:
            app, user, password = info
            print(tabulate([[app, user, password]], headers=['App', 'User', 'Password']))

    # DELETE
    elif option == '3':
        print('Please, type these infos: ')
        app = input('App: ')
        user = input('User: ')
        if delete_password(app, user):
            print('Password deleted !')
        else:
            print('An error occurred')

    # UPDATE
    elif option == '4':
        print('Please, type these infos: ')
        app = input('App: ')
        user = input('User: ')
        password = getpass()
        if update_password(app, user, password):
            print('Password updated !')
        else:
            print('An error occurred')

    # SHOW ALL
    elif option == '5':
        all_info = show_all()
        if not all_info:
            print('A database doesn\'t exist')
        else:
            print(tabulate(all_info, headers=['App', 'User', 'Password']))

    # EXIT
    elif option == '6':
        menu = False
        print('Exitting...')
    else:
        print('Invalid option...')

conn.close()