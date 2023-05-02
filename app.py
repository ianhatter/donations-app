from donations_pkg.homepage import show_homepage, donate, show_donations
from donations_pkg.user import login, register

database = {"Admin": "password123"}
donations = []
authorized_user = ""


while True:
    show_homepage()
    if authorized_user == "":
        print("You must be logged in to donate"),
    if authorized_user != "":
        print("Logged in as ", authorized_user)

    user1 = input("Choose an option: ")

    if user1 == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = login(database, username, password)
        print(authorized_user)

    elif user1 == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        authorized_user = register(database, username)
        if authorized_user != "":
            database[username] = password

    elif user1 == "3":
        if authorized_user == "":
            print("You are not logged in.")
        else:
            donation_string = donate(authorized_user)
            donations.append(donation_string)

    elif user1 == "4":
        show_donations(donations)

    elif user1 == "5":
        print("Leaving DonateMe...")
        exit()
