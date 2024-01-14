import sqlite3


# Making connection to database

connection = sqlite3.connect("student.db")


# Creating cursor

cursor = connection.cursor()


# Creating table

table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT);

"""

cursor.execute(table_info)

# Inserting data
cursor.execute(
    '''Insert Into STUDENT values('Shushil','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Sunil','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Roshan','Node.js','A',45)''')
cursor.execute('''Insert Into STUDENT values('Anil','Medical','A',89)''')
cursor.execute('''Insert Into STUDENT values('Hari','Java','A',96)''')
cursor.execute('''Insert Into STUDENT values('Amit','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Ram','Data Analyst','A',92)''')


# Displaying data

print("The inserted data")
data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()
