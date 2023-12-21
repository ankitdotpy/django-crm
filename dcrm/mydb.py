from mysql import connector

db = connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pswd1234'
)

cursor = db.cursor();

print('-'*20)
print('STARTING CREATE DATABASE')
cursor.execute('CREATE DATABASE neroai')
print('DONE SETTING UP')
print('-'*20)