import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('SELECT id, first_name, last_name, email, role FROM users LIMIT 10')
users = cursor.fetchall()

print("Users in database:")
print("-" * 80)
for row in users:
    print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Email: {row[3]}, Role: {row[4]}")
print("-" * 80)
print(f"Total users: {len(users)}")

conn.close()
