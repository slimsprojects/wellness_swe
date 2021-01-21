# This is an application to track the amount of sleep, water, and exercise done daily 
# and record production and feelings at the end of the day
# Data will be analyzed on a consistent occassion using machine learning to predict and 
# suggest advice 

import sqlite3
import datetime
from sqlite3 import Error

def db_fetch_all(con):
    cursorObj = con.cursor()
    cursorObj.execute("""SELECT oid, * FROM wellness_swe_DB""")
    rows = cursorObj.fetchall()
    for row in rows:
        print(row)


def main():
    try:
        # Connect to database
        con = sqlite3.connect('wellness_swe.db')
        print("Connection is established to database wellness_swe.db ")
    except Error:
        print(Error)

    # Create cursor
    c = con.cursor()


    # DateTime
    date_time = datetime.datetime.now()

    # Sleep (hrs)
    while True:
        sleep_hr = input('Enter hours of sleep last night: ')
        try:
            sleep_float = float(sleep_hr)
            break
        except ValueError:
            print('Please enter a decimal number ')


    # Rested (y/n)
    while True:
        rested_yn = input('Do you feel rested (y/n)? ')
        if rested_yn == 'y':
            break
        elif rested_yn == 'n':
            break
        else:
            print('Please enter y for yes or n for no ')


    # Excercise (hrs)
    while True:
        exercise_hr = input('Enter hours of exercise today: ')
        try:
            exercise_float = float(exercise_hr)
            break
        except ValueError:
            print('Please enter a decimal number ')


    # Water (cups)
    while True:
        water_cups = input('Enter cups of water drank today: ')
        try:
            water_float = float(water_cups)
            break
        except ValueError:
            print('Please enter a decimal number ')


    # Conclusions
    production = input('How productive were you today (1-10)? ')

    feelings = input('How did you feel today? ')

    additional_notes = input('Enter additional notes: ')


    c.execute("""INSERT INTO wellness_swe_DB(
        datetime, sleep_hours, rested_yes_no, exercise_hours, 
        water_cups, conclusion1_production, conclusion2_feeling, conclusion3_additional) 
        VALUES (?,?,?,?,?,?,?,?)""", 
        (date_time, sleep_float, rested_yn, exercise_float, water_float, production, feelings, additional_notes))

    # Commit changes
    con.commit()
    #Close connection
    con.close()
    print("Connection with database wellness_swe.db closed")

main()
