users_data_form = []
with sqlite3.connect("dtb.db") as connection:
    cursor = connection.cursor()
    users_data = cursor.execute("SELECT 'id', 'first_name', 'last_name', 'age', 'email', 'role', 'phone' FROM 'User'")
    for user in users_data:
        users_form = dict((y, x) for x, y in user)
        # User(user["id"], user["first_name"], user["last_name"], user["age"], user["email"], user["role"], user["phone"])
        # users_form = {"id" = user["id"], "first_name" = user["first_name"], "last_name" = user["last_name"], "age" = user["age"], "email" = user["email"], "role" = user["role"],"phone" = user["phone"]}
        users_data_form += users_form
    return users_data_form