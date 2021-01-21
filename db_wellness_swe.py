import sqlite3
from sqlite3 import Error

# CREATE functions
def add_entry(con):
    cursorObj = con.cursor()
    cursorObj.execute(""" """)


# READ functions
def db_fetch_all(con):
    cursorObj = con.cursor()
    cursorObj.execute("""SELECT oid, * FROM wellness_swe_DB""")
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)
    print('\n')
    
def db_fetch_one(con):
    while True: 
        selected_oid = input('Select id to view: ')
        try:
            cursorObj = con.cursor()
            cursorObj.execute("""SELECT * FROM wellness_swe_DB WHERE oid = """ + selected_oid)
            row = cursorObj.fetchall()
            print(row)
            break
        except Error:
            print('Please enter a valid id ')


# UPDATE functions
def update_entry(con, id):
    while True:
        print('Columns:| 1)Date&Time | 2)Sleep | 3)Rested | 4)Exercise | 5)Water | 6)Productivity | 7)Feeling | 8)Notes |')
        select_col = input('Select column to update: ')
        if select_col == '1':
            select_col = 'datetime'
            break
        elif select_col == '2':
            select_col = 'sleep_hours'
            break
        elif select_col == '3':
            select_col = 'rested_yes_no'
            break
        elif select_col == '4':
            select_col = 'exercise_hours'
            break
        elif select_col == '5':
            select_col = 'water_cups'
            break
        elif select_col == '6':
            select_col = 'conclusion1_production'
            break
        elif select_col == '7':
            select_col = 'conclusion2_feeling'
            break
        elif select_col == '8':
            select_col = 'conclusion3_additional'
            break
        else:
            print('Please select a valid column')
    update_value = input('Enter updated value: ')
    cursorObj = con.cursor()
    cursorObj.execute("""UPDATE wellness_swe_DB SET """ + select_col + """ = """ + update_value + """ WHERE oid = """ + id)
    print('Database Updated')

# DELETE functions 
def delete_all(con):
    delete_confirm = input('CAUTION: Delete all entries? yes/no ')
    if delete_confirm == 'yes': 
        cursorObj = con.cursor()
        cursorObj.execute("""DELETE from wellness_swe_DB""")
        print('Database is now empty ')
    else:
        return

def delete_row(con, id):
    cursorObj = con.cursor()
    cursorObj.execute("""DELETE FROM wellness_swe_DB WHERE oid = """ + id)
    print('Entry Deleted ')

def check_exist_db(con, id):
    db_id = id
    cursorObj = con.cursor()
    cursorObj.execute("""SELECT * FROM wellness_swe_DB 
                                    WHERE oid = ? """,
                                    (db_id))
    result = cursorObj.fetchone()
    if result:
        return True
    else:
        return False

def main():
    try:
        # Create or connect to database
        con = sqlite3.connect('wellness_swe.db')
        print("Connection is established to database wellness_swe.db \n")
    except Error:
        print(Error)

    while True:
        print('wellness_swe Database Menu: ')
        print('(1) Add ') # Create
        print('(2) View ') # Read
        print('(3) Edit ') # Update
        print('(4) Delete ') # Delete
        print('(5) Exit ')
        menu_item = input('Enter Menu Item: ')
        if menu_item == '1':
            break
        elif menu_item == '2':
            while True:
                print('View Menu: ')
                print('1) View all')
                print('2) View by ID')
                view_item = input('Enter: ')
                if view_item == '1':
                    db_fetch_all(con)
                    break
                elif view_item == '2':
                    db_fetch_one(con)
                    break
                else:
                    print('Please enter a valid selection ')
        elif menu_item == '3':
            while True:
                update_id = input('Enter ID to edit: ')
                if check_exist_db(con, update_id):
                    update_entry(con, update_id)
                    break
                else:
                    print('ID not in Database')
                    break
        elif menu_item == '4':
            while True:
                delete_id = input('Enter ID to delete: ')
                if check_exist_db(con, delete_id):
                    delete_row(con, delete_id)
                    break
                else:
                    print('ID not in Database')
                    break
        elif menu_item == '5':
            break
        else:
            print('Please enter a valid selection ')


    # Create cursor
    #c = con.cursor()

    # RUN ONCE: 
    ##### Create table #####
    # c.execute("""CREATE TABLE wellness_swe_DB (
    #         datetime text,
    #         sleep_hours float,
    #         rested_yes_no text,
    #         exercise_hours float,
    #         water_cups float,
    #         conclusion1_production float,
    #         conclusion2_feeling text,
    #         conclusion3_additional text
    #         )""")
    #####

    # Commit changes
    con.commit()
    #Close connection
    con.close()
    print("Connection with database wellness_swe.db closed")

main()
