def login(database, username, password):
    if username in database:
        if password == database[username]:
            print("Welcome Back:", username)
            return username
        print(" Incorrect password for:", username)
        return ""
    print("Username not found. Please register")
    return ""


def register(database, username):
    if username in database:
        print("Username already registered.")
        return ""
    else:
        print("The new username", username, "has been registerd")
        return username
