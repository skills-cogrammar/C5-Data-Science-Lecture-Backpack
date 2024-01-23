# Link to SQL example : https://www.mycompiler.io/view/7Bei1wmFRLX

# sqlite3 is built-in to python, no pip needed!
import sqlite3

db = sqlite3.connect('employee_db')
print('Connection Established!')

# Created Cursor Object
cursor = db.cursor()

cursor.execute(
    '''
        CREATE TABLE IF NOT EXISTS employee(id INTEGER UNIQUE NOT NULL,
                                first_name TEXT NOT NULL,
                                last_name TEXT,
                                contact_number TEXT);
    '''
)

db.commit()
print("Table Created!")

cursor.execute(
    '''
        INSERT INTO employee VALUES (3, 'John', 'Python', '000 000 0000');
    '''
)

db.commit()
print('Entry Added!')

cursor.execute(
    '''
        SELECT * FROM employee;
    '''
)
data = cursor.fetchone()
for row in cursor:
    print(f"{row}\n")