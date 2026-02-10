import sqlite3

# 1. Connect to SQLite database (file create avuthundi)
conn = sqlite3.connect("users.db")

# 2. Cursor create
cursor = conn.cursor()

# 3. Table create
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER
)
""")

print("Table created successfully")

# 4. Insert records (Parameterized Query – SQL Injection avoid cheyadaniki)
def insert_user(name, email, age):
    cursor.execute(
        "INSERT INTO users (name, email, age) VALUES (?, ?, ?)",
        (name, email, age)
    )
    conn.commit()
    print("User inserted successfully")

# Sample inserts
insert_user("Ravi", "ravi@gmail.com", 22)
insert_user("Sita", "sita@gmail.com", 21)

# 5. Fetch records
def fetch_users():
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    print("\nUser Records:")
    for row in rows:
        print(row)

fetch_users()

# 6. Update record
def update_user_age(user_id, new_age):
    cursor.execute(
        "UPDATE users SET age = ? WHERE id = ?",
        (new_age, user_id)
    )
    conn.commit()
    print("User updated successfully")

update_user_age(1, 23)

# 7. Delete record
def delete_user(user_id):
    cursor.execute(
        "DELETE FROM users WHERE id = ?",
        (user_id,)
    )
    conn.commit()
    print("User deleted successfully")

delete_user(2)

# Final fetch
fetch_users()

# 8. Close connection
conn.close()
print("\nDatabase connection closed")
