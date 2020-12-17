import sqlite3


# Run once only
# Create a database or connect to one
conn = sqlite3.connect('wellness_swe.db')
# Create cursor
c = conn.cursor()

##### Create table #####
##only have to do once 

c.execute("""CREATE TABLE wellness_swe_DB (
        datetime text,
        sleep_hours float,
        rested_yes_no text,
        exercise_hours float,
        water_cups float,
        conclusion1_production float,
        conclusion2_feeling text,
        conclusion3_additional text
        )""")

#####


# Commit changes
conn.commit()
#Close connection
conn.close()

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

