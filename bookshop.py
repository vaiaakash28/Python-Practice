import pymysql

# Database connection
db = pymysql.connect(
    host="localhost",
    user="myuer",
    password="mypassword",
    database="bookshop_db"
)

cur = db.cursor()

# CREATE
def add_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    price = float(input("Enter price: "))

    query = "INSERT INTO bookshop_table (title, author, price) VALUES (%s, %s, %s)"
    values = (title, author, price)

    cur.execute(query, values)
    db.commit()
    print("✅ Book added successfully!")


# READ
def view_books():
    cur.execute("SELECT * FROM bookshop_table")
    result = cur.fetchall()

    print("\n📚 Book List:")
    for row in result:
        print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Price: ₹{row[3]}")


# UPDATE
def update_book():
    book_id = int(input("Enter book ID to update: "))
    new_price = float(input("Enter new price: "))

    query = "UPDATE bookshop_table SET price=%s WHERE id=%s"
    values = (new_price, book_id)

    cur.execute(query, values)
    db.commit()
    print("✏️ Book updated successfully!")


# DELETE
def delete_book():
    book_id = int(input("Enter book ID to delete: "))

    query = "DELETE FROM bookshop_table WHERE id=%s"
    values = (book_id,)

    cur.execute(query, values)
    db.commit()
    print("🗑️ Book deleted successfully!")


# MENU
def menu():
    while True:
        print("\n====== BookShop Menu ======")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

# Run app
menu()
