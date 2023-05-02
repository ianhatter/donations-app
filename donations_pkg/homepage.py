
def show_homepage():
    print("------------------------------------------")
    print("| 1.    Login     | 2.   Register         |")
    print("------------------------------------------")
    print("| 3.    Donate    | 4.   Show Donations   |")
    print("------------------------------------------")
    print("|          5.    Exit                     |")
    return (" ------------------------------------------")


print("         === DonateMe Hompage ===    ")


def donate(username):
    donation_amt = input("Enter amount to donate:")
    donation_string = username, "Donated", donation_amt
    print("Thank you for your donation!")
    return donation_string


def show_donations(donations):
    print("\n--- All Donations ---")
    if donations == []:
        print("Currently, there are no donations.")
    else:
        for donation in donations:
            print(donation)
